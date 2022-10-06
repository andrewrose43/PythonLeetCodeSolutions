from unittest import TestCase
from v1.search_2d_matrix_v1 import Solution as s1
from v2.search_2d_matrix_v2 import Solution as s2
from v3.search_2d_matrix_v3 import Solution as s3
from v4.search_2d_matrix_v4 import Solution as s4
from v5.search_2d_matrix_v5 import Solution as s5

class Search2DMatrixTests(TestCase):

    def setUp(self):
        self.s = s5() # Can easily substitute in whichever solution you're testing by editing this line

    def test_simple_true(self):
        self.assertTrue(self.s.searchMatrix(
            [[5], [6]],
            6
        ))

    def test_simple_false(self):
        self.assertFalse(self.s.searchMatrix(
            [[5], [6]],
            4
        ))

    def test_complex_true(self):
        self.assertTrue(self.s.searchMatrix(
            [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
            5
        ))

    def test_complex_false(self):
        self.assertFalse(self.s.searchMatrix(
            [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
            20
        ))
