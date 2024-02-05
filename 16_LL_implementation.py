# =============================================================================
# Implementation probs		
# 111	Add 1 to a number represented as LL	https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
    def addOne(self,head):
        #Returns new head of linked List.
        string = ""
        temp = head
        while(temp != None):
            string += str(temp.data)
            temp = temp.next
        link = LinkedList()
        while(temp != None):
            link.insert(temp.data)
            temp = temp.next
        link.insert(int(string)+1)
        return link.head
# =============================================================================
# =============================================================================
# 112	Add 2 numbers represented as LL	https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1
     def addTwoLists(self, first, second):
      # return head of sum list
      f=''
      s=''
      while first:
          f=f+str(first.data)
          first=first.next
      while second:
          s=s+str(second.data)
          second=second.next
      
      res=map(int,list(str(abs(int(f)+int(s))))) # convert string to list
      
      p=None
      r=None
      for i in res:
          n=Node(i)
          if p==None:
              p=n
              r=p
          else:
              p.next=n
              p=p.next
      return r
# =============================================================================
# =============================================================================
# 113	Subtraction on LL(Comes under hard but should be solvable once the above ones are solved)	https://www.geeksforgeeks.org/problems/subtraction-in-linked-list/1?page=1&category=Linked%20List&difficulty=Hard&sortBy=submissions
def subLinkedList(l1, l2): 
    # Code here
    # return head of difference list
        #Returns new head of linked List.
    f=''
    s=''
    while l1:
        f=f+str(l1.data)
        l1=l1.next
    while l2:
        s=s+str(l2.data)
        l2=l2.next
    
    res=map(int,list(str(abs(int(f)-int(s))))) # convert string to list
    
    p=None
    r=None
    for i in res:
        n=Node(i)
        if p==None:
            p=n
            r=p
        else:
            p.next=n
            p=p.next
    return r
# =============================================================================
# =============================================================================
# Basic pattern		
# =============================================================================
# =============================================================================
# 114	Rotate LL	https://www.geeksforgeeks.org/problems/reorder-list/1?page=3&category=Linked%20List&sortBy=submissions
def reverse(head):
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

def merge(head1, head2):
    h1 = head1
    h2 = head2
    while h1 and h2:
        temp1 = h1.next
        h1.next = h2
        temp2 = h2.next
        h2.next = temp1
        h1 = temp1
        h2 = temp2
    return head1

def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return [slow.next, slow]

#Back-end complete function Template for Python 3
class Solution:
    def reorderList(self,head):
        if head.next == None:
            return head
        cur = head
        mid = find_middle(cur)
        mid[1].next = None
        rev = reverse(mid[0])
        head = merge(cur, rev)
# =============================================================================
# =============================================================================
# 115	Flattening a LL(make sure to learn the efficient approach)	https://www.geeksforgeeks.org/problems/flattening-a-linked-list--170645/1?page=4&category=Linked%20List&sortBy=submissions
# bottom pointer to a linked list where this node is head.
def merge(self, a, b):
        if a is None :
            return b
        if b is None :
            return a
        ans = None
        if a.data<b.data:
            ans = a
            a.bottom = self.merge(a.bottom, b)
        else:
            ans = b
            b.bottom = self.merge(a, b.bottom)
        return ans
        
    def flatten(self,root):
        #Your code here
        if root is None:
            return None
        mergedll = None
        mergedll = self.merge(root,self.flatten(root.next))
        return mergedll

# =============================================================================
# =============================================================================
# 116	Delete nodes having greater value on right	https://practice.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1
#leaders in an array 
#reverse --> left is greater than right --> reverse
def compute(self,head):
        head = self.reverse(head)
        max_ptr = head
        ptr = head.next
        while ptr:
            if ptr.data >= max_ptr.data:
                max_ptr.next = ptr
                max_ptr = max_ptr.next
            else:
                max_ptr.next = None
            ptr = ptr.next
            
        return self.reverse(head)
        
    def reverse(self,head):
        prev = None        #previous
        curr = head        #current
        n = head.next   #Next
        while n:
            curr.next = prev
            prev = curr
            curr = n
            n = n.next
        curr.next = prev
        return curr
# =============================================================================
# =============================================================================
# 117	Delete N nodes after M nodes	https://www.geeksforgeeks.org/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/1?page=3&category=Linked%20List&sortBy=submissions
#copy next node data to current node and point to next.next
    def skipMdeleteN(self, head, M, N):
        # Code here
        if not head or not head.next:
            return       
        i = M
        j = N       
        if N == 0:
            return        
        curr = head
        prev = None
        while curr != None:
            if i > 0 and j > 0:
                prev = curr
                i -=1
                curr = curr.next
            elif i == 0 and j > 0: # skip Mth LL
                curr = curr.next
                j -=1
            else:
                prev.next = curr # restart counter 
                i = M
                j = N
        prev.next = None
        return head
# =============================================================================
# =============================================================================
# 118	Delete all occurence of node

# =============================================================================
# =============================================================================
# 119	Clone a LL	https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1?page=1&category=Linked%20List&difficulty=Hard&sortBy=submissions
    def copyList(self, head):
        # code here
        curr = head                      
        while curr:                             # First while loop to insert clone nodes
            next = curr.next
            curr.next = Node(curr.data)
            curr.next.next = next
            curr = next
        
        curr = head
        while curr:                             # Second while loop to connect arb
            curr.next.arb = None if (curr.arb == None ) else curr.arb.next
            curr = curr.next.next
        
        head2 = head.next                       # Head of clone LL
        clone = head2                           # Temp of clone LL
        curr = head
        while curr:
            curr.next = curr.next.next
            clone.next = None if (clone.next == None) else clone.next.next
            clone = clone.next
            curr = curr.next
        
        return head2
# =============================================================================
# =============================================================================
# 120	Length of longest palindrome in LL	https://www.geeksforgeeks.org/problems/length-of-longest-palindrome-in-linked-list/1?page=2&category=Linked%20List&difficulty=Medium&sortBy=submissions
def maxPalindrome(self,head):
        # Code here
        prev = None
        cur = head
        maxi = 0
        while cur:
            temp = cur.next
            cur.next = prev 
            x = self.checkmax(prev,temp)+1 # pal len = 2 * common+1 eg 25452 
            y = self.checkmax(cur,temp)
            maxi=max(x,y,maxi)
            prev = cur
            cur = temp
        return maxi
    def checkmax(self,h1,h2):
        # Code here
        count = 0
        while h1 and h2:
            if h1.data == h2.data:
                count += 1
            else:
                break
            h1 = h1.next
            h2 = h2.next
        return 2*count
# =============================================================================
# =============================================================================
# 121	Learn the basics of circular LL	https://www.geeksforgeeks.org/circular-linked-list/
# =============================================================================
# =============================================================================
# Implementation probs		
# =============================================================================
# =============================================================================
# 122	Learn the basic representation of the nodes in LL	
# =============================================================================
# =============================================================================
# 123	Insert, Delete, Reverse DLL	https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1?page=1&category=doubly-linked-list&sortBy=submissions
 def reverseDLL(self, head):
        if not head:
            return None
        curr = head
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
            head = temp.prev
        return head
# =============================================================================
# =============================================================================
# 124	Pairs with given sum in DLL	https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1?page=1&category=doubly-linked-list&difficulty=Easy&sortBy=submissions
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        ans = []
        if head is None:
            return ans
    
        left = head
        right = self.findTail(head)
    
        while left.data < right.data:
            if left.data + right.data == target:
                ans.append((left.data, right.data))
                left = left.next
                right = right.prev
            elif left.data + right.data < target:
                left = left.next
            else:
                right = right.prev
    
        return ans
    
            
    def findTail(self,head):
        tail = head
        while tail.next is not None:
            tail = tail.next
        return tail

# =============================================================================
# =============================================================================
