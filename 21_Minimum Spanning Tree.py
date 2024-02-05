# =============================================================================
# =============================================================================
# 21_Minimum Spanning Tree		
# 191	Insert node in a tree	
# =============================================================================
# =============================================================================
# 192	Height of the tree	https://www.geeksforgeeks.org/problems/height-of-binary-tree/1?page=1&category=Tree&sortBy=submissions
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    def height(self, root):
        def solve(root):
            if not root:
                return 0
            return max(solve(root.left) , solve(root.right)) + 1
        return solve(root)
# =============================================================================
# =============================================================================
# 193	Diameter of the tree	https://www.geeksforgeeks.org/problems/diameter-of-binary-tree/1?page=1&category=Tree&sortBy=submissions
#The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes.
Input:
         10
        /   \
      20    30
    /   \ 
   40   60
Output: 4
class Solution:
    def diameter(self,root):
        def findht(root):
            nonlocal maxi
            if root is None:
                return 0
            lh = findht(root.left)
            rh = findht(root.right)
            maxi = max(maxi, lh + rh+1)
            return 1 + max(lh, rh)
        
        maxi = float("-inf")
        findht(root)
        return maxi
# =============================================================================
# =============================================================================
# 194	Check if 2 trees are identical	https://www.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1?page=1&category=Tree&sortBy=submissions

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isIdentical(self,root1, root2):
    # Base case: If both roots are None, they are identical.
        if not root1 and not root2:
            return True
    # If one of the roots is None or their values are different, they are not identical.
        if not root1 or not root2 or root1.data != root2.data:
            return False
    # Recursively check the left and right subtrees.
        return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)
# =============================================================================
# =============================================================================
# 195	Check if subtree	https://www.geeksforgeeks.org/problems/check-if-subtree/1?page=2&category=Tree&sortBy=submissions
class Solution:
    def isSubTree(self, T, S):
        def dfs(root1):
            if not root1:
                return
            if check(S,root1):
                return True
            return dfs(root1.left) or dfs(root1.right)
        def check(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.data!=root2.data:
                return False
            return check(root1.left,root2.left) and check(root1.right,root2.right)
        return dfs(T)
# =============================================================================
# =============================================================================
# 196	Check for balanced tree	https://www.geeksforgeeks.org/problems/check-for-balanced-tree/1?page=1&category=Tree&sortBy=submissions
'''class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''


#Function to check whether a binary tree is balanced or not.
class Solution:
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right))+1
            
    def isBalanced(self,root):
        if root == None:
            return True
        if (abs(self.height(root.left)-self.height(root.right))<=1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

# =============================================================================
# =============================================================================
# 197	Lowest common Ancestor in BT	https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1?page=1&category=Tree&sortBy=submissions
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        # Code here
        if not root:
            return None
        if root.data == n1 or root.data == n2:
            return root
        left = self.lca(root.left,n1,n2)
        right = self.lca(root.right,n1,n2)
        if left and right:
            return root
        elif not left and right:
            return right
        elif left and not right:
            return left
        else:
            return Non
# =============================================================================
# =============================================================================
# 198	Sum tree	https://www.geeksforgeeks.org/problems/sum-tree/1?page=1&category=Tree&sortBy=submissions
Given a Binary Tree. Return true if, for every node X in the tree other than the leaves, 
#its value is equal to the sum of its left subtree's value and its right subtree's value. Else return false.
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# function should return True is Tree is SumTree else return False
class Solution:
    def is_sum(self, root):
        if root is None:
            return 0
            
        left = self.is_sum(root.left) + root.left.data if root.left else 0
        right = self.is_sum(root.right) + root.right.data if root.right else 0
        if left+right != root.data and root.left and root.right:
            return float("-inf")
        return left + right
        
    def isSumTree(self,root):
        # Code here
        if root.left is None and root.right is None:
            return 1
        ans = self.is_sum(root)
        if ans==float("-inf") or ans!=root.data:
            return 0
        
        return 1
# =============================================================================
# =============================================================================
# 199	Symmetric tree	https://www.geeksforgeeks.org/problems/symmetric-tree/1?page=2&category=Tree&sortBy=submissions
class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        def func(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None or root1.data !=root2.data:
                return False
            return func(root1.left,root2.right) and func(root1.right,root2.left)
        return func(root.left,root.right) if root else True
# =============================================================================
# =============================================================================
# 200	Mirror of a tree	https://www.geeksforgeeks.org/problems/mirror-tree/1?page=1&category=Tree&sortBy=submissions
'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        def dfs(root):
            if not root:
                return
            root.left,root.right=root.right,root.left
            dfs(root.left)
            dfs(root.right)
        dfs(root)
# =============================================================================
# =============================================================================
# 201	Check if isomorphic	https://www.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1?page=2&category=Tree&sortBy=submissions
#Two trees are called isomorphic if one can be obtained from another by a series of flips, i.e. by swapping left and right children of several nodes. Any number of nodes at any level can have their children swapped. Two empty trees are isomorphic.
class Solution:
    # Return True if the given trees are isomotphic. Else return False.
    def isIsomorphic(self, root1, root2): 
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.data != root2.data:
            return False
            
        return ((self.isIsomorphic(root1.left, root2.left) and 
        self.isIsomorphic(root1.right, root2.right)) or 
        (self.isIsomorphic(root1.left, root2.right) and 
        self.isIsomorphic(root1.right, root2.left)))
# =============================================================================
# =============================================================================
