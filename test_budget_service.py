import unittest
from datetime import date
from decimal import Decimal

from service import BudgetService


class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.service = BudgetService()

    def test_invalid_input_when_end_before_start(self):
        start = date(2022, 5, 10)
        end = date(2022, 4, 10)

        self.assertEqual(Decimal(0), self.service.query(start, end))


if __name__ == '__main__':
    unittest.main()
