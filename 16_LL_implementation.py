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
      # code here
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

# =============================================================================
# =============================================================================
# 117	Delete N nodes after M nodes	https://www.geeksforgeeks.org/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/1?page=3&category=Linked%20List&sortBy=submissions
# =============================================================================
# =============================================================================
# 118	Delete all occurence of node	
# =============================================================================
# =============================================================================
# 119	Clone a LL	https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1?page=1&category=Linked%20List&difficulty=Hard&sortBy=submissions
# =============================================================================
# =============================================================================
# 120	Length of longest palindrome in LL	https://www.geeksforgeeks.org/problems/length-of-longest-palindrome-in-linked-list/1?page=2&category=Linked%20List&difficulty=Medium&sortBy=submissions
# =============================================================================
# =============================================================================
# 121	Learn the basics of circular LL	
# =============================================================================
# =============================================================================
# Implementation probs		
# =============================================================================
# =============================================================================
# 122	Learn the basic representation of the nodes in LL	
# =============================================================================
# =============================================================================
# 123	Insert, Delete, Reverse DLL	https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1?page=1&category=doubly-linked-list&sortBy=submissions
# =============================================================================
# =============================================================================
# 124	Pairs with given sum in DLL	https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1?page=1&category=doubly-linked-list&difficulty=Easy&sortBy=submissions
# =============================================================================
# =============================================================================
