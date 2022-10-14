from unittest import TestCase
from v1.combinations_v1 import Solution as s1
from v2.combinations_v2 import Solution as s2
from v3.combinations_v3 import Solution as s3

class CombinationsTests(TestCase):

    def setUp(self):
        self.s = s3()  # Edit this line to test any version

    def test_k1(self):
        self.assertEqual(99, len(self.s.combine(99, 1)))

    def test_n4k3(self):
        self.assertEqual(
            [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]],
            self.s.combine(4, 3)
        )
