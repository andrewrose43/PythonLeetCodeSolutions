from unittest import TestCase
from v1.nqueens_v1 import Solution as v1
from v2.nqueens_v2 import Solution as v2
from v3.nqueens_v3 import Solution as v3

class NQueensTests(TestCase):

    def setUp(self):
        self.s = v3()  # Test any version by altering this line

    def test_1(self):
        self.assertEqual(1, self.s.totalNQueens(1))

    def test_2(self):
        self.assertEqual(0, self.s.totalNQueens(2))

    def test_3(self):
        self.assertEqual(0, self.s.totalNQueens(3))

    def test_4(self):
        self.assertEqual(2, self.s.totalNQueens(4))

    def test_5(self):
        self.assertEqual(10, self.s.totalNQueens(5))

    def test_6(self):
        self.assertEqual(4, self.s.totalNQueens(6))

    def test_7(self):
        self.assertEqual(40, self.s.totalNQueens(7))

    def test_8(self):
        self.assertEqual(92, self.s.totalNQueens(8))

    def test_9(self):
        self.assertEqual(352, self.s.totalNQueens(9))
