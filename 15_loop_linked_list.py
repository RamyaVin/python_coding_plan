# =============================================================================
# Expressions		
# 100	Detect loop in LL(Once this is learnt, all the loop pattern probs below should be easy)	https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1?page=1&category=Linked%20List&sortBy=submissions
    def detectLoop(self, head):
        #code here
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
# 102	Find the starting point of loop	https://www.geeksforgeeks.org/problems/# =============================================================================
# =============================================================================
# =============================================================================
# find-the-first-node-of-loop-in-linked-list--170645/1
# =============================================================================
# =============================================================================
# 103	Remove the loop	https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1?page=1&category=Linked%20List&sortBy=submissions
# =============================================================================
# =============================================================================
# Reversing stack		
# =============================================================================
# =============================================================================
# 104	Sort 0s, 1s, 2s in LL	https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1?page=1&category=Linked%20List&sortBy=submissions
# =============================================================================
# =============================================================================
# 105	Pairwise swap elements	https://www.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1?page=2&category=Linked%20List&sortBy=submissions
# =============================================================================
# =============================================================================
# 106	Merge k sorted LL(Merge two sorted is easy version of this ques, if you are finding it diff to come up with logic, first solve that)	https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1?page=1&category=Linked%20List&sortBy=submissions
# =============================================================================
# =============================================================================
# 107	Merge sort in LL	https://www.geeksforgeeks.org/problems/sort-a-linked-list/1?page=2&category=Linked%20List&sortBy=submissions
# =============================================================================
# =============================================================================
# 108	Quick sort in LL	https://www.geeksforgeeks.org/problems/quick-sort-on-linked-list/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
# =============================================================================
# =============================================================================
# 109	Remove occurence of duplicates in sorted & unsorted LL	https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1?page=1&category=Linked%20List&difficulty=Easy&sortBy=submissions https://www.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1?page=1&category=Linked%20List&difficulty=Easy&sortBy=submissions
# =============================================================================
# =============================================================================
# 110	Seggregate even and odd nodes in LL	https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list5035/1
# 
# =============================================================================