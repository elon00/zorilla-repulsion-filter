"""
Multiwallet Connection & Dynamic QR Code Payment Standard
Supports EIP-681, BIP-21 & Solana Pay Standards
"""

from typing import Optional

class MultiwalletQRGateway:
    @staticmethod
    def generate_qr_payment_uri(network: str, recipient: str, amount: float, token_address: Optional[str] = None) -> str:
        net = network.lower()
        if net in ("ethereum", "base", "polygon", "arbitrum", "optimism"):
            if token_address:
                # EIP-681 ERC-20
                return f"ethereum:{token_address}@1/transfer?address={recipient}&uint256={int(amount * 1e18)}"
            return f"ethereum:{recipient}?value={int(amount * 1e18)}"
        elif net == "solana":
            return f"solana:{recipient}?amount={amount}&label=QMOOSA%20Protocol&message=Payment"
        elif net == "bitcoin":
            return f"bitcoin:{recipient}?amount={amount}&label=QMOOSA"
        return f"web4://pay?chain={network}&recipient={recipient}&amount={amount}"
