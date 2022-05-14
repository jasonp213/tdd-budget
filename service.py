import calendar
from datetime import date
from decimal import Decimal


class BudgetService:
    def __init__(self, repo):
        self.budget_repo = repo

    def query(self, start: date, end: date) -> Decimal:
        total = Decimal(0)
        if start > end:
            return total
        for budget in self.budget_repo.get_all():
            overlap_days = self.get_budget_overlap_days(budget, start, end)
            total += Decimal(budget.amount) * overlap_days
        return total

    def get_budget_overlap_days(self, budget, start, end):
        year, month = self.parse_budget_year_month(budget)
        _, the_month_total_days = calendar.monthrange(year, month)
        budget_start = date(year, month, 1)
        budget_end = date(year, month, the_month_total_days)

        overlap_days = (min(budget_end, end) - max(budget_start, start)).days + 1
        return Decimal(overlap_days) / Decimal(the_month_total_days)

    def parse_budget_year_month(self, budget):
        return int(budget.year_month[:4]), int(budget.year_month[-2:])
