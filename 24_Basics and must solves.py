# =============================================================================
# =============================================================================
# 24_Basics and must solves		
# 225	Construct Binary Tree from Preorder and Inorder Traversal ( First understand the concept of how to derive at the solution, then start coding it by yourself)	https://www.geeksforgeeks.org/problems/construct-tree-1/1?page=1&category=Tree&sortBy=submissions
class Solution:
    def buildtree(self, inorder, preorder, n):
        # code here
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = Node(inorder[ind])
            root.left = self.buildtree(inorder[0:ind], preorder, n)
            root.right = self.buildtree(inorder[ind+1:], preorder, n)
            return root
####In conclusion, although the time complexity is the same for both implementations in the worst case, the second code implementation is more efficient in the average case due to the optimized search operation.

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None
'''
class Solution:
    def buildtree(self, inorder, preorder, n):
        def search(inorder, l, r, val):
            for i in range(l, r + 1):
                if inorder[i] == val:
                    return i
            return -1

        def cal(inorder, preorder, l, r):
            nonlocal ind
            if l > r:
                return None

            ptr = Node(preorder[ind])
            ind += 1

            if l == r:
                ptr.left = None
                ptr.right = None
                return ptr

            inindex = search(inorder, l, r, ptr.data)
            ptr.left = cal(inorder, preorder, l, inindex - 1)
            ptr.right = cal(inorder, preorder, inindex + 1, r)

            return ptr

        ind = 0
        return cal(inorder, preorder, 0, n - 1)
# =============================================================================
# =============================================================================
# 226	Construct Binary Tree from Inorder and Postorder Traversal	https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
Example 1:
         3
        /  \
      9     20
           /   \
          15    7
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
# =============================================================================
# =============================================================================
# 227	Construct BST from given preorder traversal	https://www.geeksforgeeks.org/problems/construct-tree-from-preorder-traversal/1?page=7&category=Tree&sortBy=submissions
from collections import deque

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder = deque(postorder)
        inorder_index = {val:i for i,val in enumerate(inorder)}
        return self.constructTree(postorder, inorder_index, 0, len(postorder)-1)
    
    def constructTree(self, postorder, inorder_index, start, end):
        if start > end:
            return None
        
        val = postorder.pop()
        root = TreeNode(val)
        index = inorder_index[val]
        
        root.right = self.constructTree(postorder, inorder_index, index+1, end)
        root.left = self.constructTree(postorder, inorder_index, start, index-1)
        
        return root
# =============================================================================
# =============================================================================
# 228	Construct BT from parent array	https://www.geeksforgeeks.org/problems/construct-binary-tree-from-parent-array/1?page=5&category=Tree&sortBy=submissions
#User function Template for python3
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def construct(final,index):
    if(index[0]>=len(final)):
        return None
    if(final[index[0]][1]=='L'):
        node = Node(final[index[0]][0])
        index[0]+=1
        return node
    root = Node(final[index[0]][0])
    index[0]+=1
    root.left = construct(final,index)
    root.right = construct(final,index)
    return root
    
def constructTree(pre, preln, n):
    final = []
    index = [0]
    for i in range(len(pre)):
        dum = [pre[i],preln[i]]
        final.append(dum)
    return construct(final,index)
# =============================================================================
# =============================================================================
# Basic		
# 229	Serialize and deserialize BT	https://www.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1?page=4&category=Tree&sortBy=submissions
'''
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''
class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent,N):
        # your code here
        nodes=[]
        for i in range(N):
            nodes.append(Node(i))
        
        root=None
        for (i,value) in enumerate(parent):
            curr_node=nodes[i]
            if value==-1:
                root=curr_node
            else:
                parent_node=nodes[value]
                if not parent_node.left:
                    parent_node.left=curr_node
                else:
                    parent_node.right=curr_node
        return root       
# =============================================================================
# =============================================================================
# 230	Largest subtree sum in a tree	https://www.geeksforgeeks.org/problems/largest-subtree-sum-in-a-tree/1?page=6&category=Tree&sortBy=submissions
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def serialize(root, A):
    def inoder(root):
        if(root):
            inorder(root.left)
            print(root.data,end=" ")
            inorder(root.right)
    inorder(root)
    return []

#Function to deserialize a list and construct the tree.   
def deSerialize(A):
    return None
# =============================================================================
# =============================================================================
# 231	Maximum sum of non adjacent nodes	https://www.geeksforgeeks.org/problems/maximum-sum-of-non-adjacent-nodes/1?page=3&category=Tree&sortBy=submissions
class Solution:
    def __init__(self):
        self.mx = float('-inf')
    
    def solve(self,root):
        if root is None:
            return 0
        
        ls = self.solve(root.left) #left sum
        rs = self.solve(root.right)  # right sum
        s = ls+rs+root.data  # left sum + right sum + root's value
        self.mx = max(self.mx,s)
        return s
    
    def findLargestSubtreeSum(self, root : Optional['Node']) -> int:
        # code here
        self.solve(root)
        return self.mx
# =============================================================================
# =============================================================================
# 232	Duplicate subtree 	https://www.geeksforgeeks.org/problems/duplicate-subtrees/1?page=4&category=Tree&sortBy=submissions
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self,root):
        def helper(root):
            if not root:
                return [0,0]
            left=helper(root.left)
            right=helper(root.right)
            res=[0,0]
            res[0]=root.data+right[1]+left[1]
            res[1]=max(left[0],left[1])+max(right[0],right[1])
            return res
        return max(helper(root)[0],helper(root)[1])
# =============================================================================
# =============================================================================
# 233	Flatten BT to linked list	https://www.geeksforgeeks.org/problems/flatten-binary-tree-to-linked-list/1?page=5&category=Tree&sortBy=submissions
# =============================================================================
# =============================================================================
# 1D - Linear DP		
# 2D Grid DP		
# 234	Permutations of a string	https://www.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 235	Permutation II (You can solve on own once you solve above)	https://leetcode.com/problems/permutations-ii
# =============================================================================
# =============================================================================
# 236	Combination sum I	https://www.geeksforgeeks.org/problems/combination-sum-1587115620/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 237	Combination sum II(Once you solve combination I, you should be able to solve this and below 2 probs too easily)	https://leetcode.com/problems/combination-sum-ii
# =============================================================================
# =============================================================================
# 238	Combination sum III	https://leetcode.com/problems/combination-sum-iii
# =============================================================================
# =============================================================================
# 239	Rat in maze(Once above probs are solved, you can do this easily)	https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 240	Possible words from phone digits	https://www.geeksforgeeks.org/problems/possible-words-from-phone-digits-1587115620/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 241	Subsets	https://www.geeksforgeeks.org/problems/subsets-1613027340/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 242	Unique subset(Solving above, you will be able to solve this easily)	https://www.geeksforgeeks.org/problems/subsets-1587115621/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 243	N-Queen(Super imp)	https://www.geeksforgeeks.org/problems/n-queen-problem0315/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 244	N Queen II	https://leetcode.com/problems/n-queens-ii
# =============================================================================
# =============================================================================
# 245	Permutation with spaces	https://www.geeksforgeeks.org/problems/permutation-with-spaces3627/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 246	Generate parantheses	https://www.geeksforgeeks.org/problems/generate-all-possible-parentheses/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 247	Generate IP address	https://www.geeksforgeeks.org/problems/generate-ip-addresses/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 248	Solve the sudoku	https://www.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 249	kth permutation	https://www.geeksforgeeks.org/problems/find-kth-permutation/1?page=2&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 250	Word search	https://www.geeksforgeeks.org/problems/word-search/1?page=3&category=Graph&sortBy=submissions
# =============================================================================
# =============================================================================
# 251	Palindrome partition of string	https://www.geeksforgeeks.org/problems/find-all-possible-palindromic-partitions-of-a-string/1?page=2&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 252	Decode the string	https://www.geeksforgeeks.org/problems/decode-the-string2444/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 253	Letter case permutation	https://leetcode.com/problems/letter-case-permutation/
# =============================================================================
# =============================================================================
# 254	sum string	https://www.geeksforgeeks.org/problems/sum-string3151/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 255	word boggle	https://www.geeksforgeeks.org/problems/word-boggle4143/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 256	Largest number in k swaps	https://www.geeksforgeeks.org/problems/largest-number-in-k-swaps-1587115620/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
# 257	Partition array to k subsets	https://www.geeksforgeeks.org/problems/partition-array-to-k-subsets/1?page=1&category=Backtracking&sortBy=submissions
# =============================================================================
# =============================================================================
