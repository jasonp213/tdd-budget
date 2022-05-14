import unittest
from datetime import date
from decimal import Decimal
from unittest.mock import patch

from repo import Budget
from service import BudgetService


class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.service = BudgetService()
        self.fake_get_all = patch("repo.BudgetRepo.get_all").start()

    def tearDown(self) -> None:
        patch.stopall()

    def test_invalid_input_when_end_before_start(self):
        start = date(2022, 5, 10)
        end = date(2022, 4, 10)
        self.assertEqual(Decimal(0), self.service.query(start, end))

    def test_whole_month(self):
        self.fake_get_all.return_value = [Budget("202205", 10000)]
        start = date(2022, 5, 1)
        end = date(2022, 5, 31)
        self.assertEqual(Decimal(10000), self.service.query(start, end))


if __name__ == '__main__':
    unittest.main()
