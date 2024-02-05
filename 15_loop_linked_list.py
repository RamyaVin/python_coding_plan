# =============================================================================
# Expressions		
# 100	Detect loop in LL(Once this is learnt, all the loop pattern probs below should be easy)	https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1?page=1&category=Linked%20List&sortBy=submissions
    def detectLoop(self, head):
        slow=head
        fast=head
        x=0
        while fast!=None and fast.next!=None:
            if fast==slow and x==1:
                return True
            fast=(fast.next).next
            slow=slow.next
            x=1
        return False
# =============================================================================
# =============================================================================
# 101	Find length of loop in LL	https://www.geeksforgeeks.org/problems/find-length-of-loop/1?page=1&category=Linked%20List&difficulty=Easy&sortBy=submissions
def countNodesinLoop(head):
    #Your code here
    fast = head
    slow = head
    if fast==None or fast.next==None:
        return 0
    while fast and fast.next:
        slow=slow.next
        fast = fast.next.next
        if fast==None or fast.next==None:
            return 0
        if fast==slow:
            break
    #loop is there, so count the nodes
    fast=fast.next
    size=1
    while fast!=slow:
        fast=fast.next
        size+=1
    
    return size
# =============================================================================
# =============================================================================
# 102	Find the starting point of loop	https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1
    def findFirstNode(self, head):
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow.data
        return -1
# =============================================================================
# =============================================================================
# 103	Remove the loop	https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1?page=1&category=Linked%20List&sortBy=submissions

    def removeLoop(self, head):
        # remove the loop without losing any nodes
        if not head:
            return head
        # It has to be in this order only
        slow = head
        fast = head
        prev = None
        
        # checking for loop
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if fast and fast.next:
            fast = head
            
            while slow != fast:
                prev = slow
                slow = slow.next
                fast = fast.next
            
            prev.next = None
            
        return head
# =============================================================================
# =============================================================================
# Reversing stack	

# =============================================================================
# =============================================================================
# 104	Sort 0s, 1s, 2s in LL	https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1?page=1&category=Linked%20List&sortBy=submissions
def segregate(self, head):
        dummyZero = Node(-1)
        zero = dummyZero
        dummyOne = Node(-1)
        one = dummyOne
        dummyTwo = Node(-1)
        two = dummyTwo
        temp = head
        while temp != None:
            if temp.data == 0:
                zero.next = temp
                zero = temp
            elif temp.data == 1:
                one.next = temp
                one = temp
            elif temp.data == 2:
                two.next = temp
                two = temp
            temp = temp.next
        if dummyOne.next != None:
            zero.next = dummyOne.next
        else:
            zero.next = dummyTwo.next
        one.next = dummyTwo.next
        two.next = None
        return dummyZero.next
# =============================================================================
# =============================================================================
# 105	Pairwise swap elements	https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1?page=2&category=Linked%20List&sortBy=submissions
    def pairWiseSwap(self, head):
        current = head
        previous = None
        count = 0
        while current and count<2:
            following = current.next
            current.next = previous
            previous = current
            current = following
            count+=1
        if current!=None:
            head.next=self.pairWiseSwap(current)
        return previous
# =============================================================================
# =============================================================================
# 106	Merge k sorted LL(Merge two sorted is easy version of this ques, if you are finding it diff to come up with logic, first solve that)	https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1?page=1&category=Linked%20List&sortBy=submissions
def sortedMerge(head1, head2):
    dummyNode = Node(0)
    tail = dummyNode
    while True:
        if head1 is None:
            tail.next = head2
            break
        if head2 is None:
            tail.next = head1
            break
        
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        
        tail = tail.next
    return dummyNode.next
# =============================================================================
# =============================================================================
# 107	Merge sort in LL	https://www.geeksforgeeks.org/problems/sort-a-linked-list/1?page=2&category=Linked%20List&sortBy=submissions
class Solution:
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        mid = self.find_middle(head)
        next_to_mid = mid.next
        mid.next = None
        left_sorted = self.mergeSort(head)
        right_sorted = self.mergeSort(next_to_mid)
        sorted_list = self.merge(left_sorted, right_sorted)
        return sorted_list
    def find_middle(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, left, right):
        dummy = Node(0)
        current = dummy
        while left is not None and right is not None:
            if left.data < right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        if left is not None:
            current.next = left
        elif right is not None:
            current.next = right
        return dummy.next
# =============================================================================
# =============================================================================
# 108	Quick sort in LL	https://www.geeksforgeeks.org/problems/quick-sort-on-linked-list/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
def quickSort(head):
#return head after sorting
#User function Template for python3
    if not head or not head.next:
        return head
    pivot = head
    smallhead = small = Node(-1)
    largehead = large = Node(-1)
    curr = head.next#because head is pivot
    while curr:
        if curr == pivot:
            curr = curr.next
        elif curr.data<pivot.data:
            small.next = curr
            curr = curr.next
            small = small.next
        else:
            large.next = curr
            curr = curr.next
            large = large.next
    small.next = None
    large.next = None
    small = quickSort(smallhead.next)
    pivot.next = None#after sorting the half of linked list
    large = quickSort(largehead.next)
    temp = small
    while temp and temp.next:
        temp = temp.next
    if temp:
        temp.next =pivot#for more elements in linked list
    else:
        small = pivot#for less elements in the linked list
    pivot.next = large#joining both the list
    return small
# =============================================================================
# =============================================================================
# 109	Remove occurence of duplicates in sorted & unsorted LL	https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1?page=1&category=Linked%20List&difficulty=Easy&sortBy=submissions 

#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    curr=head
    while(curr and curr.next):
        if curr.data==curr.next.data:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return head
#https://www.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1?page=1&category=Linked%20List&difficulty=Easy&sortBy=submissions
    def removeDuplicates(self, head):
        # return head after editing list
         dict1={}
         dummy_node=Node(-1)
         curr1=dummy_node
         if head is None or head.next is None:
             return head
         curr=head
         while curr is not None:
             if curr.data not in dict1:
                 dict1[curr.data]=1
                 new_node=Node(curr.data)
                 curr1.next=new_node
                 curr1=curr1.next
             curr=curr.next
         return dummy_node.next
# =============================================================================
# =============================================================================
# 110	Seggregate even and odd nodes in LL	https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list5035/1
# 
def divide(self, N, head):
        head1 = even = node()
        head2 = odd = node()
        
        while head :
            if head.data % 2 == 0 :
                even.next = head
                even = even.next
            else :
                odd.next = head
                odd = odd.next
            
            head = head.next
        
        odd.next = None
        even.next = head2.next
        return head1.next
# =============================================================================
