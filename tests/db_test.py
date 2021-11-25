import os
import sys
sys.path.append(os.getcwd()) # add current directory in path

import unittest

import db
import datetime
from common.info_test import text_insert1, text_insert2


class Db_for_test(db.Main):
    def __init__(self):
        super().__init__(path_db="db_for_test.db")



class Main(unittest.TestCase):
    def setUp(self) -> None:
        self.db_test = Db_for_test()
        self.db_test._del_all_data()
        return super().setUp()

    def test_select_last(self):
        self.db_test._inset(text_insert1)
        self.assertEqual(self.db_test._select_stats_last()[0], (str(datetime.date.today()), 10, 3, 2, 1, 4, 9))

    def test_select_stats_all_prep(self):
        self.db_test._inset(text_insert1)
        self.assertEqual(self.db_test.select_stats_all_prep(), {str(datetime.date.today()): (10, 3, 2, 1, 4, 9)})

        self.db_test._inset(text_insert2)
        self.assertEqual(self.db_test.select_stats_all_prep(), {str(datetime.date.today()): (20.0, 3.5, 1.5, 5.5, 8.0, 11.5)})

        self.assertEqual(self.db_test.select_stats_all_prep(last=True), {str(datetime.date.today()): (30, 4, 1, 10, 12, 14)})

        

    def tearDown(self) -> None:
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()