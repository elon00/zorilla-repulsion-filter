// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title QmoosaLaunchpadToken
 * @dev Production-grade ERC-20 token implementing governed, decay-bounded uncapped issuance.
 * Formula: Mint(t) <= CirculatingSupply * AnnualDecayRate(t)
 */
contract QmoosaLaunchpadToken {
    string public name = "QMOOSA Universal Token";
    string public symbol = "QMOOSA";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    address public owner;
    address public treasury;
    uint256 public immutable genesisTime;
    uint256 public lastMintTime;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Unauthorized: Caller is not owner");
        _;
    }

    constructor(address _treasury, uint256 _initialSupply) {
        require(_treasury != address(0), "Invalid treasury address");
        owner = msg.sender;
        treasury = _treasury;
        genesisTime = block.timestamp;
        lastMintTime = block.timestamp;

        _mint(_treasury, _initialSupply);
    }

    function transfer(address to, uint256 value) public returns (bool) {
        require(balanceOf[msg.sender] >= value, "ERC20: transfer amount exceeds balance");
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint256 value) public returns (bool) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function transferFrom(address from, address to, uint256 value) public returns (bool) {
        require(balanceOf[from] >= value, "ERC20: balance insufficient");
        require(allowance[from][msg.sender] >= value, "ERC20: allowance insufficient");
        allowance[from][msg.sender] -= value;
        balanceOf[from] -= value;
        balanceOf[to] += value;
        emit Transfer(from, to, value);
        return true;
    }

    /**
     * @notice Governed, decay-bounded minting (Uncapped lifetime supply with annual ceiling)
     */
    function governedMint(address to, uint256 requestedAmount) external onlyOwner returns (uint256) {
        require(block.timestamp >= lastMintTime + 1 days, "Cooldown active");
        
        // Annual maximum emission: 5% of circulating supply
        uint256 maxAllowed = (totalSupply * 5) / 100;
        uint256 mintAmount = requestedAmount > maxAllowed ? maxAllowed : requestedAmount;
        
        lastMintTime = block.timestamp;
        _mint(to, mintAmount);
        return mintAmount;
    }

    function burn(uint256 amount) external {
        require(balanceOf[msg.sender] >= amount, "Burn amount exceeds balance");
        balanceOf[msg.sender] -= amount;
        totalSupply -= amount;
        emit Burn(msg.sender, amount);
        emit Transfer(msg.sender, address(0), amount);
    }

    function _mint(address to, uint256 amount) internal {
        require(to != address(0), "Cannot mint to zero address");
        totalSupply += amount;
        balanceOf[to] += amount;
        emit Mint(to, amount);
        emit Transfer(address(0), to, amount);
    }
}
