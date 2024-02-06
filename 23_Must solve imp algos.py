# =============================================================================
# =============================================================================
# 23_Must solve imp algos		
# 211	Insert a node in BST	https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs (root,val):
            if not root:
                return TreeNode(val)
            if val > root.val:
                root.right = dfs(root.right,val)
            else:
                root.left = dfs(root.left,val)
            return root
        return dfs(root,val)               
# =============================================================================
# =============================================================================
# 212	Search a value in BST(Learn efficient algo to do it, since this can be handled efficiently in BST than BT)	https://practice.geeksforgeeks.org/problems/search-a-node-in-bst/1
    def search(self, root, x):
        while root != None:
            if root.data == x:
                return True
            elif root.data > x:
                root = root.left
            elif root.data < x:
                root = root.right
        
        return False 
# =============================================================================
# =============================================================================
# 213	Find minimum and maximum in BST	https://www.geeksforgeeks.org/problems/max-and-min-element-in-binary-tree/1?page=5&category=Tree&sortBy=submissions
class Solution:
    def search(self):
        mx = self.findMax(self,root)
        mi = self.findMin(self, root)
        return [mx , mi]
        
    def findMax(self,root):
        if root == None:
            return -1
        curr = root
        while curr.right:
            curr = curr.right
        return curr.data
        #code here
    def findMin(self,root):
        if root== None:
            return -1
        curr = root
        while curr.left:
            curr = curr.left
        return curr.data
# =============================================================================
# =============================================================================
# 214	Find the Kth largest element/kth Smallest in BST(Try to solve it without looking for soln, once you have mastered all the above patterns, this should be easy)	https://www.geeksforgeeks.org/problems/kth-largest-element-in-bst/1?page=2&category=Tree&sortBy=submissions
# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        arr = []
        def inorder(root):
            if not root:
                return 0
            inorder(root.left)
            arr.append(root.data)
            inorder(root.right)
        inorder(root)
        N = len(arr)
        return arr[N-k]
# =============================================================================
# =============================================================================
# 215	Check for BST(Try solving probs in this pattern by yourself till LCA once above are solved)	https://www.geeksforgeeks.org/problems/check-for-bst/1?page=1&category=Tree&sortBy=submissions
class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        return self.isBSTU(root,float("-inf"),float("inf"))
    def isBSTU(self,node,min_val,max_val):
        if node is None:
            return True
        if node.data<=min_val or node.data >= max_val:
            return False
        return (self.isBSTU(node.left,min_val,node.data)) and (self.isBSTU(node.right,node.data,max_val))
# =============================================================================
# =============================================================================
# 216	Find the closest element in BST	https://www.geeksforgeeks.org/problems/find-the-closest-element-in-bst/1?page=3&category=Tree&sortBy=submissions
class Solution:
    def minDiff(self,root, K):
        mini=[10**9]
        def f(root):
            if(root):
                mini[0]=min(mini[0],abs(K-root.data))
                f(root.left)
                f(root.right)
        f(root)
        return mini[0]
# =============================================================================
# =============================================================================
# 217	Count BST nodes in the given range	https://www.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1?page=3&category=Tree&sortBy=submissions
#Function to count number of nodes in BST that lie in the given range.
class Solution:
    
    def getCount(self,root,low,high):
        
        if root == None: 
            return 0
              
        #if data at current node is equal to lower and upper range, we return 1.
        if root.data == high and root.data == low:  
            return 1
      
        #if data at current node is within range then we include it in count 
        #and call function recursively for its left and right children.
        if root.data <= high and root.data >= low:  
            return (1+self.getCount(root.left,low,high)+self.getCount(root.right,low,high)) 
      
        #else if data at current node is smaller than lower range then
        #we call function recursively only for right child.
        elif root.data < low:  
            return self.getCount(root.right, low, high) 
      
        #else we call function recursively only for left child. 
        else: 
            return self.getCount(root.left, low, high) 
# =============================================================================
# =============================================================================
# 218	Largest BST in BT(Super imp - Must solve)	https://www.geeksforgeeks.org/problems/largest-bst/1?page=2&category=Tree&sortBy=submissions

class NodeValue:
    def __init__(self, minNode, maxNode, maxSize):
        self.minNode = minNode
        self.maxNode = maxNode
        self.maxSize = maxSize

class Solution:
    def largestBstHelper(self, root):
        # an empty tree is a BST of size zero
        if root is None:
            return NodeValue(float('inf'), float('-inf'), 0)
        # traverse left and right subtree    
        left = self.largestBstHelper(root.left)
        right = self.largestBstHelper(root.right)
        # check for BST condition for current node
        if (root.data > left.maxNode and root.data < right.minNode):
            return NodeValue(min(root.data, left.minNode), max(root.data, right.maxNode), left.maxSize + right.maxSize + 1)
        return NodeValue(float('-inf'), float('inf'), max(left.maxSize, right.maxSize))
    
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        return self.largestBstHelper(root).maxSize
# =============================================================================
# =============================================================================
# 219	Lowest Common Ancestor in BST	https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1?page=1&category=Tree&sortBy=submissions
#Function to find the lowest common ancestor in a BST. 
def LCA(root, n1, n2):
    def check(node,no1,no2):
        if node is None:
            return None
        if (no1<node.data and no2<node.data):
            return check(node.left,no1,no2)
        elif (no1>node.data and no2>node.data):
            return check(node.right,no1,no2)
        else:
            return node
    return check(root,n1,n2)
# =============================================================================
# =============================================================================
# 220	Merge two BST(Super imp - Must solve)	https://www.geeksforgeeks.org/problems/merge-two-bst-s/1?page=4&category=Tree&sortBy=submissions
class Solution:    
    #Function to return a list of integers denoting the node 
    #values of both the BST in a sorted order.
    def inOrder(self,root,ans):
        if root is None:
            return
        self.inOrder(root.left,ans)
        ans.append(root.data)
        self.inOrder(root.right,ans)
        
    def merge(self, root1, root2):
        ans=[]
        self.inOrder(root1,ans)
        self.inOrder(root2,ans)
        return sorted(ans)
# =============================================================================
# =============================================================================
# 221	Inorder successor and predecessor	https://www.geeksforgeeks.org/problems/predecessor-and-successor/1?page=2&category=Tree&sortBy=submissions
class Solution:
    def findPreSuc(self, root, pre, suc, key):
        if not root:
            return None
        
        q, ans = deque([root]), []
        
        while q:
            node = q.popleft()
            if node:
                ans.append(node.key)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        if key not in ans:
            ans.append(key) 
        ans.sort()
        
        for i in range(len(ans)):
            if ans[i] == key:
                pre.key, suc.key = ans[i-1] if i-1 >= 0 else -1, ans[i+1] if i+1 < len(ans) else -1
                return(pre.key, suc.key)
# =============================================================================
# =============================================================================
# 222	Populate inorder successor for all nodes	https://www.geeksforgeeks.org/problems/populate-inorder-successor-for-all-nodes/1?page=5&category=Tree&sortBy=submissions

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next=None

class Solution:
    
    def inorder(self, root, ds):
        if not root:
            return
        
        self.inorder(root.left, ds)
        ds.append(root)
        self.inorder(root.right, ds)
    
    def populateNext(self,root):
        ds = []
        self.inorder(root, ds)
        V = len(ds)
        for i in range(V-1):
            ds[i].next = ds[i+1]
# =============================================================================
# =============================================================================
# 223	BST to greater sum tree	https://www.geeksforgeeks.org/problems/bst-to-greater-sum-tree/1?page=8&category=Tree&sortBy=submissions

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''

class Solution:
    def transformTree(self, root):
        def f(root, inc):
            if root is None:
                return inc
            
            inc = f(root.right, inc)
            new_val = inc
            inc = root.data + inc
            root.data = new_val
            inc = f(root.left, inc)
            return inc
            
        f(root, 0)
# =============================================================================
# =============================================================================
# 224	Delete given node from BST	https://leetcode.com/problems/delete-node-in-a-bst/
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if not root:
            return None
            
        if root.val > key:
		    # Target node is smaller than currnet node, search left subtree
			
            root.left = self.deleteNode( root.left, key )

        elif root.val < key:
		    # Target node is larger than currnet node, search right subtree
			
            root.right = self.deleteNode( root.right, key )

        else:
            # Current node is target node
			
            if (not root.left) or (not root.right):
                # At least one child is empty
                # Target node is replaced by either non-empty child or None
                root = root.left if root.left else root.right

            else:
                # Both two childs exist
                # Target node is replaced by smallest element of right subtree
                cur = root.right

                while cur.left:
                    cur = cur.left

                root.val = cur.val
                root.right = self.deleteNode( root.right, cur.val )
                    
        return root
# =============================================================================
# =============================================================================
