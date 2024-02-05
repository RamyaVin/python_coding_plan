# =============================================================================
# =============================================================================
#20_Topological sort		
# Multi Source		
# Topological sort		
# 180	PreOrder Traversal	https://www.geeksforgeeks.org/problems/preorder-traversal/1?page=1&category=Tree&sortBy=submissions
#User function Template for python3
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Function to return a list containing the preorder traversal of the tree.
def preorder(root):
    if not root:
        return []
    return [root.data] + preorder(root.left) + preorder(root.right)
####reduce the memory usage by using an iterative approach instead of recursion.
def preorder(root):
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

# =============================================================================
# =============================================================================
# 181	InOrder Traversal	https://www.geeksforgeeks.org/problems/inorder-traversal/1?page=2&category=Tree&sortBy=submissions

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def InOrder_help(self,root,res):
        if root:
            self.InOrder_help(root.left,res)
            res.append(root.data)
            self.InOrder_help(root.right,res)            
        return res
    def InOrder(self,root):
        # code here
        res = []
        return self.InOrder_help(root, res)
# =============================================================================
# =============================================================================
# 182	PostOrder Traversal	https://www.geeksforgeeks.org/problems/postorder-traversal/1?page=2&category=Tree&sortBy=submissions
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the postorder traversal of the tree.
def postOrder(root):
        def solve(root):
            # code here
            if not root:
                return []
            return  solve(root.left)  + solve(root.right)+[root.data]
        return solve(root)
# =============================================================================
# =============================================================================
# 183	Level Order Traversal	https://www.geeksforgeeks.org/problems/level-order-traversal/1?page=1&category=Tree&sortBy=submissions
#Level order traversal of a tree is breadth-first traversal for the tree.
    def levelOrder(self,root ):
        r= []
        if not root:
            return r
        q = [root]
        while q:
            cur_node = q.pop(0)
            r.append(cur_node.data)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        return r
# =============================================================================
# =============================================================================
# 184	Boundary Traversal(Once level traversal is learnt, this you can solve)	https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1?page=1&category=Tree&sortBy=submissions
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        boundary_view = []

        def print_leaves(node):
            if node:
                print_leaves(node.left)
                if not node.left and not node.right:
                    boundary_view.append(node.data)

                print_leaves(node.right)

        def print_left_boundary(node):
            if node:
                if node.left:
                    boundary_view.append(node.data)
                    print_left_boundary(node.left)
                elif node.right:
                    boundary_view.append(node.data)
                    print_left_boundary(node.right)

        def print_right_boundary(node):
            if node:
                if node.right:
                    print_right_boundary(node.right)
                    boundary_view.append(node.data)
                elif node.left:
                    print_right_boundary(node.left)
                    boundary_view.append(node.data)

        if root:
            boundary_view.append(root.data)
            print_left_boundary(root.left)
            print_leaves(root.left)
            print_leaves(root.right)
            print_right_boundary(root.right)

        return boundary_view
# =============================================================================
# =============================================================================
# 185	Vertical Traversal(Once level traversal is learnt, this you can solve, lil extra logic is needed)	https://www.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1?page=1&category=Tree&sortBy=submissions
Input:
           1
         /   \
       2       3
     /   \   /   \
   4      5 6      7
              \      \
               8      9           
Output: 
4 2 1 5 6 3 8 7 9 

from collections import defaultdict 
class Solution:
        
    def verticalOrder(self, root): 
        out_dict = {}
        
        def helper(node, h_dist=0, v_dist=0):
            if node is None:
                return
            
            if h_dist in out_dict:
                out_dict[h_dist].append((v_dist, node.data))
            else:
                out_dict[h_dist] = [(v_dist, node.data)]
                
            helper(node.left, h_dist-1, v_dist+1)
            helper(node.right, h_dist+1, v_dist+1)
        
        helper(root)
        
        result_list = []
        for k,val in sorted(out_dict.items()):
            val_sorted = sorted(val, key= lambda x :x[0])
            for x, y in val_sorted:
                result_list.append(y) 
        return result_list
# =============================================================================
# =============================================================================
# 186	Top View of BT(Once you have mastered level traversal, this should be easy)	https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1?page=1&category=Tree&sortBy=submissions
Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100
# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        res =[]
        if root == None:
            return res
            
        my_map = {}
        queue = []
        queue.append((root, 0))
        
        while len(queue) >0 :
            n = len(queue)
            
            for i in range(n):
                node, hd = queue.pop(0)
                val = node.data
                if hd not in my_map:
                    my_map[hd] = val
                if node.left != None:
                    queue.append((node.left, hd-1))
                if node.right != None:
                    queue.append((node.right, hd+1))
                    
        for key, val in sorted(my_map.items()):
            res.append(val)
            
        return res

# =============================================================================
# =============================================================================
# 187	Bottom View of BT(Once you have mastered level traversal, this should be easy)	https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1?page=1&category=Tree&sortBy=submissions
                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14
For the above tree the output should be 5 10 4 14 25.

    def bottomView(self, root):

        mapp = {}
        ans = []
    
        self.helper(root, 0, 0, mapp)
        for hd, node in sorted(mapp.items()):
            ans.append(node[0])
    
        return ans

    def helper(self, root, hdist, vdist, mapp):
        
        if root is None:
            return
        if hdist in mapp:
            if vdist >= mapp[hdist][1]:
                mapp[hdist] = [root.data, vdist]
        else:
            mapp[hdist] = [root.data, vdist]
        self.helper(root.left, hdist - 1, vdist + 1, mapp)
        self.helper(root.right, hdist + 1, vdist + 1, mapp)
        return
                    
# =============================================================================
# =============================================================================
# 188	Left View of BT(Once you have mastered vertical traversal, this should be easy)	https://www.geeksforgeeks.org/problems/left-view-of-binary-tree/1?page=1&category=Tree&sortBy=submissions
Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    / \
  4     5   6    7
   \
     8
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    if root == None:
        return []
    queue = []
    ans = []
    isAns = True
    queue.append(root)
    while queue:
        count = len(queue)
        isLeft = True
        while count > 0:
            node = queue.pop(0)
            if isLeft == True:
                ans.append(node.data)
                isLeft = False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            count -= 1
            
    return ans 
# =============================================================================
# =============================================================================
# 189	Right View of BT(Once you have mastered vertical traversal, this should be easy)	https://www.geeksforgeeks.org/problems/right-view-of-binary-tree/1?page=1&category=Tree&sortBy=submissions
Input:
     10
    /   \
  20     30
 /   \
40  60 
Output: 10 30 60
    def rightView(self,root):
        if root is None:
            return []
        
        ans = []
        q = [root]
        
        while len(q)!=0:
            count = len(q)
            for i in range(count):
                curr = q[0]
                q.pop(0)
                if i == count-1:
                    ans.append(curr.data)
                
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
        
        return ans
# =============================================================================
# =============================================================================
# 190	Diagonal Traversal	https://www.geeksforgeeks.org/problems/diagonal-traversal-of-binary-tree/1?page=3&category=Tree&sortBy=submissions
class Solution:
    def diagonal(self,root):
        d={}
        def traversal(root,lvl):
            if not root:
                return
            if lvl not in d:
                d[lvl]=[]
            d[lvl].append(root.data)
            traversal(root.left,lvl+1)
            traversal(root.right,lvl)
        traversal(root,0)
        # print(d)
        i=0
        res=[]
        while i in d:
            res.extend(d[i])
            i+=1
        return res
# =============================================================================
# =============================================================================
