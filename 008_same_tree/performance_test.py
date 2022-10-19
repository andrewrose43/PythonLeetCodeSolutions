import timeit

if __name__ == "__main__":

    for v in ("v1", "v2", "v3"):
        setup = f'''
from {v}.same_tree_{v} import Solution as {v}
from {v}.same_tree_{v} import TreeNode
from collections import deque
import random

q = deque()
random.seed(123)  # Same seed every time, so the same tree is created every time
n = TreeNode(val=random.random())
q.append(n)

num_nodes = 10000

# Add num_nodes random-value nodes to the tree
for i in range(0, num_nodes, 2):
    curr = q.popleft()
    curr.left = TreeNode(val=random.random())
    curr.right = TreeNode(val=random.random())
    # Add to queue only what will actually be used
    if len(q) < num_nodes - i:
        q.append(curr.left)
        q.append(curr.right)
'''
        code = f'''
solution = {v}()
solution.isSameTree(p=n, q=n)
'''
        print(f"isSameTree {v}: {timeit.timeit(stmt=code, setup=setup, number=100)} seconds")


