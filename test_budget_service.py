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

    def test_one_day(self):
        self.fake_get_all.return_value = [Budget("202205", 310)]
        start = date(2022, 5, 1)
        end = start
        self.assertEqual(Decimal(10), self.service.query(start, end))

    def test_cross_month(self):
        self.fake_get_all.return_value = [
            Budget("202205", 310),
            Budget("202204", 6000),
        ]
        start = date(2022, 4, 30)
        end = date(2022, 5, 2)
        self.assertEqual(Decimal(1 * 200 + 2 * 10), self.service.query(start, end))

    def test_repo_not_amount(self):
        self.fake_get_all.return_value = [
            Budget("202204", 6000),
        ]
        start = date(2022, 5, 1)
        end = date(2022, 5, 2)
        self.assertEqual(Decimal(0), self.service.query(start, end))

    def test_parse_year_month(self):
        year, month = self.service.parse_year_month_str('202205')
        self.assertEqual(2022, year)
        self.assertEqual(5, month)


if __name__ == '__main__':
    unittest.main()
