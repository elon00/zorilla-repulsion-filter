"""
x402 Bazaar Agent-to-Agent Payment & Resource Discovery Protocol
Official: https://x402.org/
Specs: https://github.com/x402-foundation/x402
"""

import time
import hashlib
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger("x402Bazaar")

class X402BazaarProtocol:
    def __init__(self, treasury_address: str = "0x71CQMOOSAUniversalTreasury999"):
        self.treasury_address = treasury_address
        self.invoices: Dict[str, Dict[str, Any]] = {}

    def issue_payment_challenge(self, resource_uri: str, price_tokens: float, chain_id: int = 1) -> Dict[str, Any]:
        challenge_id = hashlib.sha256(f"{resource_uri}:{price_tokens}:{time.time()}".encode()).hexdigest()[:16]
        invoice = {
            "status": 402,
            "status_text": "Payment Required",
            "protocol": "x402-bazaar/v2.0",
            "challenge_id": challenge_id,
            "resource": resource_uri,
            "recipient": self.treasury_address,
            "amount": price_tokens,
            "currency": "USDC/QMOOSA",
            "chain_id": chain_id,
            "expires_at": int(time.time()) + 300
        }
        self.invoices[challenge_id] = invoice
        return invoice

    def verify_payment_proof(self, challenge_id: str, tx_hash: str, payer_address: str) -> bool:
        if challenge_id not in self.invoices:
            logger.error("x402: Challenge expired or not found")
            return False
        if not tx_hash.startswith("0x") or len(tx_hash) != 66:
            logger.error("x402: Invalid transaction hash format")
            return False
        self.invoices[challenge_id]["settled"] = True
        self.invoices[challenge_id]["tx_hash"] = tx_hash
        self.invoices[challenge_id]["payer"] = payer_address
        return True
