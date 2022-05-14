import calendar
from datetime import date
from decimal import Decimal

from repo import BudgetRepo


class BudgetService:

    def query(self, start: date, end: date) -> Decimal:
        total = Decimal(0)
        if start > end:
            return total
        total_budget = BudgetRepo().get_all()

        for budget in total_budget:
            year, month = self.parse_year_month_str(budget.year_month)
            _, days = calendar.monthrange(year, month)
            had_days = self.get_days_between_budget(year, month, days, start, end)
            total += Decimal(budget.amount) * (Decimal(had_days) / Decimal(days))
        return total

    def get_days_between_budget(self, year, month, days, start, end) -> int:
        budget_start = date(year, month, 1)
        budget_end = date(year, month, days)
        if self.is_intersection(budget_start, budget_end, start, end):
            return (min(budget_end, end) - max(budget_start, start)).days + 1
        return 0

    @staticmethod
    def is_intersection(budget_start, budget_end, start, end):
        return budget_end > start or budget_start < end

    def parse_year_month_str(self, year_month):
        return int(year_month[:4]), int(year_month[-2:])
