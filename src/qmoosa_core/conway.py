"""
Conway Automaton Engine (B3/S23 Deterministic State Transitions & Hashing)
"""

import hashlib
from typing import List

class ConwayAutomaton:
    def __init__(self, width: int = 32, height: int = 32):
        self.width = width
        self.height = height
        self.grid: List[List[int]] = [[0 for _ in range(width)] for _ in range(height)]
        self.generation: int = 0

    def spawn_glider(self, x: int = 1, y: int = 1):
        coords = [(x, y+1), (x+1, y+2), (x+2, y), (x+2, y+1), (x+2, y+2)]
        for r, c in coords:
            if 0 <= r < self.height and 0 <= c < self.width:
                self.grid[r][c] = 1

    def count_neighbors(self, r: int, c: int) -> int:
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = (r + dr) % self.height, (c + dc) % self.width
                count += self.grid[nr][nc]
        return count

    def evolve(self) -> str:
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for r in range(self.height):
            for c in range(self.width):
                neighbors = self.count_neighbors(r, c)
                if self.grid[r][c] == 1:
                    new_grid[r][c] = 1 if neighbors in (2, 3) else 0
                else:
                    new_grid[r][c] = 1 if neighbors == 3 else 0
        self.grid = new_grid
        self.generation += 1
        return self.compute_state_hash()

    def compute_state_hash(self) -> str:
        serialized = "".join("".join(str(cell) for cell in row) for row in self.grid)
        return hashlib.sha256(f"CONWAY:{self.generation}:{serialized}".encode("utf-8")).hexdigest()
