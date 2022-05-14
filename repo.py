from dataclasses import dataclass
from typing import List


@dataclass
class Budget:
    year_month: str  # Char(6) e.g. "202205"
    amount: int


class BudgetRepo:

    def get_all(self) -> List[Budget]:
        pass
