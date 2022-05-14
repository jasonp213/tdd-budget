import unittest
from datetime import date
from decimal import Decimal
from unittest.mock import patch

from repo import Budget, BudgetRepo
from service import BudgetService


class TestBudgetService(unittest.TestCase):
    def setUp(self):
        patcher = patch('repo.BudgetRepo.get_all')
        self.fake_repo_all = patcher.start()

        self.service = BudgetService(BudgetRepo())

    def test_invalid_input_when_end_before_start(self):
        start = date(2022, 5, 10)
        end = date(2022, 4, 10)

        self.assertEqual(Decimal(0), self.service.query(start, end))

    def test_exact_a_whole_month(self):
        self.given_repo_budgets([Budget('202205', 31000)])

        start = date(2022, 5, 1)
        end = date(2022, 5, 31)

        self.assertEqual(Decimal(Decimal(31000)), self.service.query(start, end))

    def test_a_day_exact_month(self):
        self.given_repo_budgets([Budget('202205', 31000)])

        start = date(2022, 5, 1)
        end = date(2022, 5, 1)

        self.assertEqual(Decimal(Decimal(1000)), self.service.query(start, end))

    def given_repo_budgets(self, budgets):
        self.fake_repo_all.return_value = budgets


if __name__ == '__main__':
    unittest.main()
