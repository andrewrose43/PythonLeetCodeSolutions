from unittest import TestCase
from validate_bst_v1 import Solution, TreeNode

class ValidateBSTV1Test(TestCase):

    def setUp(self):
        self.s = Solution()

    def test_none(self):
        n = None
        self.assertTrue(self.s.isValidBST(n))

    def test_one(self):
        n = TreeNode()
        self.assertTrue(self.s.isValidBST(n))

    def test_two_true_left(self):
        n = TreeNode(2)
        n.left = TreeNode(1)
        self.assertTrue(self.s.isValidBST(n))

    def test_two_false_left(self):
        n = TreeNode(2)
        n.left = TreeNode(9001)
        self.assertFalse(self.s.isValidBST(n))

    def test_two_true_right(self):
        n = TreeNode(2)
        n.right = TreeNode(3)
        self.assertTrue(self.s.isValidBST(n))

    def test_two_false_right(self):
        n = TreeNode(2)
        n.right = TreeNode(1)
        self.assertFalse(self.s.isValidBST(n))

    def test_three_true(self):
        n = TreeNode(2)
        n.left = TreeNode(1)
        n.right = TreeNode(3)
        self.assertTrue(self.s.isValidBST(n))

    def test_three_false_left(self):
        n = TreeNode(2)
        n.left = TreeNode(5)
        n.right = TreeNode(3)
        self.assertFalse(self.s.isValidBST(n))

    def test_three_false_right(self):
        n = TreeNode(2)
        n.left = TreeNode(1)
        n.right = TreeNode(0)
        self.assertFalse(self.s.isValidBST(n))

    def test_complex_1(self):
        n = TreeNode(5)
        n.left = TreeNode(4)
        n.right = TreeNode(6)
        n.right.left = TreeNode(3)
        n.right.right = TreeNode(7)
        self.assertFalse(self.s.isValidBST(n))
