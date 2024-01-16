# =============================================================================
# Next smallest element(Once above pattern is covered, try to solve this on own)		
# 90	Create, Insert, Delete Operations in LL	
class Solution:
    def searchKey(self, n, head, key):
        #Code here
    #Function to search for a key in a linked list.
        current = head
        #Looping through the linked list.
        while current:
            #Checking if the current node's data matches the key.
            if current.data == key:
                return 1
            #Moving to the next node.
            current = current.next
        #Returning 0 if the key is not found in the linked list.
        return 0
# =============================================================================
# =============================================================================
# 91	Search for an element in LL(Once create, insert is done, this should be easy)	https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1
   def reverseList(self, head):
        # Code here
        prev=None
        current=head
        
        while current is not None:
            nextnode=current.next
            current.next=prev
            prev=current
            current=nextnode
        return prev
# =============================================================================
# =============================================================================
# 92	Reverse a LL(Learn the O space approach, learn recursive & iterative soln)	https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1?page=1&category=Linked%20List&sortBy=submissions
     def reverseList(self, head):
        # Code here
        prev=None
        current=head
        
        while current is not None:
            nextnode=current.next
            current.next=prev
            prev=current
            current=nextnode
        return prev  
# =============================================================================
# =============================================================================
# 93	Check if LL is a Palindrome(Once reversing is learnt, this should be easy)	https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1?page=1&category=Linked%20List&sortBy=submissions
# =============================================================================
# =============================================================================
# 94	Middle element of LL (Learn efficient approach)	https://www.geeksforgeeks.org/problems/insert-in-middle-of-linked-list/1?page=2&category=Linked%20List&sortBy=submissions
# =============================================================================
# =============================================================================
# 95	Find the intersection point of Y LL(Once you know traversal, apply node logic to solve this)	https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1?page=1&category=Linked%20List&sortBy=submissions
# =============================================================================
# =============================================================================
# 96	Union and Intersection of LL	https://www.geeksforgeeks.org/problems/union-of-two-linked-list/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
# =============================================================================
# =============================================================================
# 97	Delete without head pointer	https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1?page=1&category=Linked%20List&sortBy=submissions
# =============================================================================
# =============================================================================
# 98	Count pairs with given sum	https://www.geeksforgeeks.org/problems/count-pairs-whose-sum-is-equal-to-x/1?page=2&category=Linked%20List&sortBy=submissions
# =============================================================================
# =============================================================================
# 99	Reverse LL in groups of given size(Once you learn reverse of LL's efficient approach, you can try this)	https://www.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1?page=1&category=Linked%20List&sortBy=submissions
# 
# =============================================================================
