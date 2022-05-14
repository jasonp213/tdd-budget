from dataclasses import dataclass
from typing import List


@dataclass
class Budget:
    year_month: str  # Char(6) e.g. "202205"
    amount: int


class BudgetRepo:

    @classmethod
    def get_all(cls) -> List[Budget]:
        pass
