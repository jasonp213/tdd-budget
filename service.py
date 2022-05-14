from datetime import date
from decimal import Decimal


class BudgetService:
    def __init__(self, repo):
        self.budget_repo = repo

    def query(self, start: date, end: date) -> Decimal:
        total = Decimal(0)
        for budget in self.budget_repo.get_all():
            total += Decimal(budget.amount)
        return total
