"""
Uncapped Sustainable Tokenomics & Launchpad Engine
Mathematical Issuance Formula:
M(t) = min(R(t), EmissionCap(t))
where EmissionCap(t) = InitialSupply * AnnualDecayRate^t
"""

import math
import time
import logging

logger = logging.getLogger("TokenomicsLaunchpad")

class SustainableTokenomicsEngine:
    def __init__(self, initial_supply: float = 1_000_000_000.0, annual_decay: float = 0.85):
        self.circulating_supply = initial_supply
        self.annual_decay = annual_decay
        self.genesis_time = time.time()
        self.burned_total = 0.0

    def compute_capped_mint(self, requested_mint: float, elapsed_years: float) -> float:
        rate = 0.05 * (self.annual_decay ** math.floor(elapsed_years))
        annual_cap = self.circulating_supply * rate
        mint_approved = min(requested_mint, annual_cap)
        self.circulating_supply += mint_approved
        logger.info(f"Tokenomics: Requested {requested_mint}, Approved {mint_approved}. New Circulating: {self.circulating_supply}")
        return mint_approved

    def execute_burn(self, amount: float):
        qty = min(amount, self.circulating_supply)
        self.circulating_supply -= qty
        self.burned_total += qty
        logger.info(f"Tokenomics: Burned {qty} tokens.")
