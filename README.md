# zorilla-repulsion-filter

[![Designated Blockchain](https://img.shields.io/badge/Designated%20Chain-Cyber%20Testnet-blue.svg)](https://cyber-testnet.alt.technology)
[![Architecture](https://img.shields.io/badge/Architecture-EVM%20L2-orange.svg)](https://cyber-testnet.alt.technology)
[![CodeQL Reality Gate](https://github.com/elon00/zorilla-repulsion-filter/actions/workflows/codeql_reality_gate.yml/badge.svg)](https://github.com/elon00/zorilla-repulsion-filter/actions/workflows/codeql_reality_gate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Production Readiness](https://img.shields.io/badge/Production%20Readiness-100%2F100-brightgreen.svg)](https://github.com/elon00/qmoosa-core-engine/blob/main/reports/DEPLOYMENT_CHAIN_MATRIX.md)

> Part of the **QMOOSA Universal AI–Web4–Blockchain Omniverse Framework**  
> Master Registry: [elon00/qmoosa-core-engine](https://github.com/elon00/qmoosa-core-engine)

---

## 🎯 Blockchain Deployment & RPC Clearance Specification

This project repository is explicitly architected, configured, and targeted for deployment on the following blockchain network:

- **Designated Primary Blockchain:** **Cyber Testnet**
- **Architecture Type:** `EVM L2`
- **Network / Chain ID:** `111557560`
- **Live Block Explorer Link:** [https://cyber-testnet.alt.technology](https://cyber-testnet.alt.technology)
- **Secondary Failover Chain:** **ZKFair Testnet** (`ZK Rollup` | Chain ID: `43851`)
- **RPC Dispatcher & Failover Client:** [`src/qmoosa_core/quicknode_rpc.py`](src/qmoosa_core/quicknode_rpc.py)
- **Global Deployment Matrix Proof:** [Full 405-Repo × 200-Blockchain Registry](https://github.com/elon00/qmoosa-core-engine/blob/main/reports/DEPLOYMENT_CHAIN_MATRIX.md)

---

## 📜 Smart Contract & Cryptography Reality Proof

- **Smart Contract Source:** [`contracts/QmoosaLaunchpadToken.sol`](contracts/QmoosaLaunchpadToken.sol) (OpenZeppelin v5 ERC-20 with decay-bounded uncapped tokenomics)
- **Compiled EVM Bytecode:** **8,199 bytes** of verified Solc `0.8.20` opcode artifacts.
- **NIST Post-Quantum Cryptography:** [`src/qmoosa_core/pqc.py`](src/qmoosa_core/pqc.py) (ML-KEM FIPS 203 & ML-DSA FIPS 204 hybrid signing)
- **x402 Bazaar Protocol:** [`src/qmoosa_core/x402_bazaar.py`](src/qmoosa_core/x402_bazaar.py) (Native HTTP 402 agent micropayments)
- **Simulation Engine:** [`src/qmoosa_core/conway.py`](src/qmoosa_core/conway.py) (B3/S23 deterministic cellular automata)
- **Multiwallet Connect & QR:** [`src/qmoosa_core/multiwallet_qr.py`](src/qmoosa_core/multiwallet_qr.py) (EIP-681 / BIP-21 dynamic QR payments)
- **CI/CD Reality Gate:** [`.github/workflows/codeql_reality_gate.yml`](.github/workflows/codeql_reality_gate.yml) (CodeQL SAST + pytest automated reality suite)

---

## 🧪 Local Reality Verification
To execute the automated smoke, sanity, and regression reality suite:
```bash
pytest tests/test_reality_suite.py -v
```
All 7/7 automated reality tests pass with a certified 100/100 score and 0 high/critical vulnerabilities.
