from dataclasses import dataclass
from typing import List


@dataclass
class Budget:
    year_month: str
    amount: int


class BudgetRepo:

    def get_all(self) -> List[Budget]:
        pass
