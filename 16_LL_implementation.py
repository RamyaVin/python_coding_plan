# =============================================================================
# Implementation probs		
# 111	Add 1 to a number represented as LL	https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
# directly perform the addition operation on the linked list without converting it to a string. Iterate through the linked list while keeping track of the carry value. Add 1 to the least significant digit and propagate the carry if needed. Return the head of the modified linked list.
def addOne(self, head):
    curr = head
    carry = 1
    while curr:
        carry += curr.data
        curr.data = carry % 10
        carry //= 10
        if curr.next is None and carry:
            curr.next = Node(carry)
            break
        curr = curr.next
    return head
############
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
#This optimized implementation directly performs the addition operation on the linked lists without converting them to strings and lists of integers.
def addTwoLists(self, first, second):
    dummy = Node(0)
    curr = dummy
    carry = 0
    while first or second or carry:
        if first:
            carry += first.data
            first = first.next
        if second:
            carry += second.data
            second = second.next
        curr.next = Node(carry % 10)
        carry //= 10
        curr = curr.next
    return dummy.next
######################
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
    dummy = Node(0)
    curr = dummy
    borrow = 0
    while l1 or l2:
    diff = borrow + (l1.data if l1 else 0) - (l2.data if l2 else 0)
    borrow = 1 if diff < 0 else 0
    curr.next = Node(diff % 10)
    curr = curr.next
    if l1:
        l1 = l1.next
    if l2:
        l2 = l2.next

return dummy.next
#######################
def subLinkedList(l1, l2): 
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
    #we can improve the time complexity by reducing redundant computations and improving the memory usage. Here's an optimized version of the code:
def merge(self, a, b):
    if a is None:
        return b
    if b is None:
        return a
    
    ans = None
    if a.data < b.data:
        ans = a
        a.bottom = self.merge(a.bottom, b)
    else:
        ans = b
        b.bottom = self.merge(a, b.bottom)
    
    return ans

def flatten(self, root):
    if root is None or root.next is None:
        return root
    
    merged_ll = self.merge(root, self.flatten(root.next))
    
    return merged_ll
    ###################################
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
#the reverse method, we simplified the logic by eliminating unnecessary variables. Instead of assigning n = head.next and updating n in each iteration, we directly assign next_node = curr.next and use it to update curr.next. This reduces redundant computations and improves code readability.
def compute(self, head):
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

def reverse(self, head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
#############################################
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
#cloning process in three passes, we can create a clone of the linked list while maintaining the original list's structure.
def copyList(self, head):
    if not head:
        return None

    # First pass: Insert clone nodes
    curr = head
    while curr:
        next_node = curr.next
        curr.next = Node(curr.data)
        curr.next.next = next_node
        curr = next_node

    # Second pass: Connect the .arb pointers
    curr = head
    while curr:
        if curr.arb:
            curr.next.arb = curr.arb.next
        curr = curr.next.next

    # Third pass: Separate original and cloned lists
    head_clone = head.next
    curr = head
    while curr:
        clone = curr.next
        curr.next = curr.next.next
        if clone.next:
            clone.next = clone.next.next
        curr = curr.next
    return head_clone

# =============================================================================
# =============================================================================
# 120	Length of longest palindrome in LL	https://www.geeksforgeeks.org/problems/length-of-longest-palindrome-in-linked-list/1?page=2&category=Linked%20List&difficulty=Medium&sortBy=submissions
def maxPalindrome(self, head):
    prev = None
    cur = head
    result = 0

    while cur:
        temp = cur.next
        cur.next = prev
        x = self.checkmax(prev, temp) + 1  # palindrome length = 2 * common + 1 (e.g., 25452)
        y = self.checkmax(cur, temp)
        result = max(result, x, y)
        prev = cur
        cur = temp

    return result

def checkmax(self, h1, h2):
    count = 0
    while h1 and h2 and h1.data == h2.data:
        count += 1
        h1 = h1.next
        h2 = h2.next
    return 2 * count
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
#In the optimized code, we simplified the logic by using two pointers - curr and prev. We also updated the curr.prev pointer to next_node and curr.next pointer to prev to reverse the linked list.
def reverseDLL(self, head):
    if not head:
        return None

    curr = head
    prev = None

    while curr:
        next_node = curr.next
        curr.next = prev
        curr.prev = next_node
        prev = curr
        curr = next_node

    return prev
###################
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
def findPairsWithGivenSum(self, target: int, head: Optional['Node']) -> List[List[int]]:
    ans = []
    if head is None:
        return ans

    left = head
    right = self.findTail(head)

    while left.data < right.data:
        current_sum = left.data + right.data
        if current_sum == target:
            ans.append([left.data, right.data])
            left = left.next
            right = right.prev
        elif current_sum < target:
            left = left.next
        else:
            right = right.prev
    return ans

def findTail(self, head):
    tail = head
    while tail.next is not None:
        tail = tail.next
    return tail
# =============================================================================
# =============================================================================
