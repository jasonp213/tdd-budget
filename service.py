from datetime import date
from decimal import Decimal


class BudgetService:
    def query(self, start: date, end: date) -> Decimal:
        raise NotImplementedError
