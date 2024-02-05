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

#### using memoization to avoid redundant calculations.
class Solution:
    def height(self, root):
        memo = {}
        
        def solve(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            memo[root] = max(solve(root.left) , solve(root.right)) + 1
            return memo[root]
        
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
    def diameter(self, root):
        def findht(root, memo):
            if root is None:
                return 0
            if root in memo:
                return memo[root]
            lh = findht(root.left, memo)
            rh = findht(root.right, memo)
            memo[root] = 1 + max(lh, rh)
            return memo[root]
        
        def finddiameter(root, memo):
            if root is None:
                return 0
            lh = findht(root.left, memo)
            rh = findht(root.right, memo)
            diameter = lh + rh
            left_diameter = finddiameter(root.left, memo)
            right_diameter = finddiameter(root.right, memo)
            return max(diameter, left_diameter, right_diameter)
        
        memo = {}
        findht(root, memo)
        return finddiameter(root, memo)
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
############optimised
class Solution:
    def height(self, root, memo):
        if root is None:
            return 0
        if root in memo:
            return memo[root]
        
        left_height = self.height(root.left, memo)
        if left_height == -1:
            return -1
        right_height = self.height(root.right, memo)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        
        memo[root] = max(left_height, right_height) + 1
        return memo[root]
            
    def isBalanced(self, root):
        memo = {}
        return self.height(root, memo) != -1   
# =============================================================================
# =============================================================================
# 197	Lowest common Ancestor in BT	https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1?page=1&category=Tree&sortBy=submissions
class Solution:
    # Function to return the lowest common ancestor in a Binary Tree.
    def lca(self, root, n1, n2):
        # Base case: if the root is None or one of the nodes is found, return the root
        if root is None or root.data == n1 or root.data == n2:
            return root
        # Recursively find the LCA in the left and right subtrees
        left = self.lca(root.left, n1, n2)
        right = self.lca(root.right, n1, n2)
        # If both left and right subtrees have a valid LCA, the current root is the LCA
        if left and right:
            return root
        # Return the non-null subtree as the LCA
        return left if left else right

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

###optimised 
#Instead of calculating the sum of the left and right subtrees separately in the is_sum function, we can modify the function to return the sum of the subtree and the boolean value indicating if it is a Sum Tree. This way, we avoid redundant calculations of the sums.

#We can remove the separate check for root.left and root.right in the is_sum function since it is covered by the calculation of left and right.
class Solution:
    def is_sum(self, root):
        if root is None:
            return (0, True)
        
        left_sum, left_is_sum = self.is_sum(root.left)
        right_sum, right_is_sum = self.is_sum(root.right)
        
        current_sum = left_sum + right_sum
        
        if (root.left or root.right) and current_sum != root.data:
            return (current_sum, False)
        
        return (current_sum + root.data, left_is_sum and right_is_sum)
        
    def isSumTree(self, root):
        if root is None:
            return 1
        
        _, is_sum_tree = self.is_sum(root)
        
        if is_sum_tree:
            return 1
        else:
            return 0
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
