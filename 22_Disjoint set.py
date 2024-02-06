# =============================================================================
# =============================================================================
# 22_Disjoint set		
# 202	Root to leaf paths	https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1?page=4&category=Tree&sortBy=submissions
"""Input:
         10
       /    \
      20    30
     /  \
    40   60
Output: 10 20 40 #10 20 60 #10 30 #"""
def search(r, p, ans):
    if r is None:
        return
    p.append(r.data)
    if r.left is None and r.right is None:
        ans.append(list(p))
        
    search(r.left, p, ans)
    search(r.right, p, ans)
    p.pop()

def Paths(r):
    ans = []
    if r is None:
        return ans
    search(r, [], ans)
    return ans
# =============================================================================
# =============================================================================
# 203	Root to leaf path sum (Once the root to leaf path is solved, this should be easy)	https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1?page=4&category=Tree&sortBy=submissions same link as above
# =============================================================================
# =============================================================================
# 204	Maximum path sum from any node(Once the root to leaf path is solved, this should be easy)	https://www.geeksforgeeks.org/problems/maximum-path-sum-from-any-node/1?page=3&category=Tree&sortBy=submissions
"""Input:
     10
   /    \
  2      5
          \
          -2
Output: 17
Explanation: Path in the given tree goes like 2 , 10 , 5 which gives the max sum as 17."""
#Instead of using a mutable list max_sum to store the maximum sum, we can use a nonlocal variable max_sum inside the set_max_sum function.
class Solution:
    def findMaxSum(self, root):
        max_sum = float('-inf')
        
        def set_max_sum(root):
            nonlocal max_sum
            
            if not root:
                return 0
            
            lsum = set_max_sum(root.left)
            rsum = set_max_sum(root.right)
            
            max_side_sum = max(lsum + root.data, rsum + root.data)
            all_sum = max(lsum + rsum + root.data, root.data)
            
            max_sum = max(max_sum, max(all_sum, max_side_sum))
            return max(root.data, max_side_sum)
        
        set_max_sum(root)
        return max_sum
# =============================================================================
# =============================================================================
# 205	K Sum Paths (Once the root to leaf path is solved, this should be easy)	https://www.geeksforgeeks.org/problems/k-sum-paths/1?page=3&category=Tree&sortBy=submissions
"""Input:      
Tree = 
          1                               
        /   \                          
       2     3
K = 3
Output: 2
Explanation:Path 1 : 1 + 2 = 3 Path 2 : only leaf node 3"""
class Solution:
    def __init__(self):
        self.c=0
        
    def sumK(self,r,k):
        # code here
        f={0:1}
        def call(r,k,f,x):
            if r==None:
                return
            x=x+r.data
            if (x-k) in f:
                self.c=self.c+f[x-k]
            f[x]=1+f.get(x,0)
            
            call(r.left,k,f,x)
            call(r.right,k,f,x)
            f[x]=f[x]-1
        call(r,k,f,0)
        return self.c
# =============================================================================
# =============================================================================
# 206	Nodes at given distance	https://www.geeksforgeeks.org/problems/nodes-at-given-distance-in-binary-tree/1?page=3&category=Tree&sortBy=submissions
"""Input:      
          20
        /    \
      8       22 
    /   \
   4    12 
       /   \
      10    14
Target Node = 8 , K = 2
Output: 10 14 22 , Explanation: The three nodes at distance 2 from node 8 are 10, 14, 22."""
from collections import deque
class Solution:
    def find_target(self,root,target):
        if root:
            left=self.find_target(root.left,target)
            if root.data==target:
                return root
            right=self.find_target(root.right,target)
            return left or right
        return None
    
    def find_parent(self,root):
        parent_of=dict()
        q=deque()
        q.append(root)
        while q:
            u=q.popleft()
            if u.left:
                q.append(u.left)
                parent_of[u.left]=u
            if u.right:
                q.append(u.right)
                parent_of[u.right]=u
        return parent_of

    def KDistanceNodes(self,root,target,k):
        parent_of=self.find_parent(root)
        target_pointer=self.find_target(root,target)
        visited=set()
        q=deque()
        q.append(target_pointer)
        visited.add(target_pointer.data)
        distance=0
        while q:
            if distance==k:
                break
            for i in range(len(q)):
                u=q.popleft()
                if u.left and (u.left.data not in visited):
                    q.append(u.left)
                    visited.add(u.left.data)
                if u.right and (u.right.data not in visited):
                    q.append(u.right)
                    visited.add(u.right.data)
                if u in parent_of and (parent_of[u].data not in visited):
                    q.append(parent_of[u])
                    visited.add(parent_of[u].data)
            distance+=1
        result=[item.data for item in q]
        result.sort()
        return result
# =============================================================================
# =============================================================================
# 207	Range sum of BST(Solving nodes at given distance, will make this easy)	
# =============================================================================
# =============================================================================
# 208	Minimum distance between 2 nodes(Solving nodes at given distance, will make this easy)	https://www.geeksforgeeks.org/problems/min-distance-between-two-given-nodes-of-a-binary-tree/1?page=2&category=Tree&sortBy=submissions
"""Input:
        1
      /  \
     2    3
a = 2, b = 3 , Output: 2
Explanation: We need the distance between 2 and 3. Being at node 2, we need to take two steps ahead in order to reach node 3. The path followed will be: 2 -> 1 -> 3. Hence, the result is 2."""
class Solution:
    def findDist(self,root,n1,n2):
        # ans=
        def f(root):
            if(root==None or root.data==n1 or root.data==n2):
                return root
                
            leftval=f(root.left)
            rightval=f(root.right)
            
            if(leftval==None):
                return rightval
            if(rightval==None):
                return leftval
            else:
                return root
        root= f(root)
        l=[0,0]
        def f(root,c,val,i):
            if(root):
                if(root.data==val):
                    l[i]=max(l[i],c)
                else:
                    f(root.right,c+1,val,i)
                    f(root.left,c+1,val,i)
        f(root,0,n1,0)            
        f(root,0,n2,1)
        return l[0]+l[1]
# =============================================================================
# =============================================================================
# 209	Maximum distance between node and ancestor(Must solve though distance pattern is covered)	https://www.geeksforgeeks.org/problems/maximum-difference-between-node-and-its-ancestor/1?page=3&category=Tree&sortBy=submissions
#Instead of using a list ans to store the maximum difference, we can use a single variable max_diff. This eliminates the need for a list and simplifies the code. Instead of returning a sentinel value 10**9 for leaf nodes, we can return the actual value of the leaf node itself.
def maxDiff(root):
    max_diff = -10**9

    def find_min_value(root):
        nonlocal max_diff

        if root is None:
            return float('inf')

        if root.left is None and root.right is None:
            return root.data

        left_val = find_min_value(root.left)
        right_val = find_min_value(root.right)
        max_diff = max(max_diff, root.data - min(left_val, right_val))
        return min(root.data, left_val, right_val)

    find_min_value(root)
    return max_diff
# =============================================================================
# =============================================================================
# 210	Min time to burn a tree(Using distance logic, this can be sovled)	https://www.geeksforgeeks.org/problems/burning-tree/1?page=4&category=Tree&sortBy=submissions
"""Input:      
          1
        /   \
      2      3
    /  \      \
   4    5      6
       / \      \
      7   8      9
                   \
                   10
Target Node = 8
Output: 7
Explanation: If leaf with the value 
8 is set on fire. 
After 1 sec: 5 is set on fire.
After 2 sec: 2, 7 are set to fire.
After 3 sec: 4, 1 are set to fire.
After 4 sec: 3 is set to fire.
After 5 sec: 6 is set to fire.
After 6 sec: 9 is set to fire.
After 7 sec: 10 is set to fire.
It takes 7s to burn the complete tree."""
class Solution:
    def minTime(self, root,target):
        parent={}
        res=[root]
        while res:
            a=res.pop(0)
            if a.left:
                parent[a.left]=a
                res.append(a.left)
            if a.right:
                parent[a.right]=a
                res.append(a.right)
        queue=[]
        def inorder(root):
            if root and root.data==target:
               queue.append([root,0])
            else:
                if root:
                    inorder(root.left)
                    inorder(root.right)
        inorder(root)
        vis={queue[0][0]:1}
        maxi=0
        while queue:
            for i in range((len(queue))):
                a=queue.pop(0)
                node=a[0]
                count=a[1]
                maxi=max(maxi,count)
                if node in parent and parent[node] not in vis:
                    vis[parent[node]]=1
                    queue.append([parent[node],count+1])
                if node.left and node.left not in vis:
                    vis[node.left]=1
                    queue.append([node.left,count+1])
                if node.right and node.right not in vis:
                    vis[node.right]=1
                    queue.append([node.right,count+1])
        return maxi
# =============================================================================
# =============================================================================
