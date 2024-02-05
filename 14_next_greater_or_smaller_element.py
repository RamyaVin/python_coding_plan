# =============================================================================
# Next smallest element(Once above pattern is covered, try to solve this on own)		
# 90	Create, Insert, Delete Operations in LL	
#O(n)
class Solution:
    def searchKey(self, n, head, key):
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
#O(n)   
def reverseList(self, head):
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
    def isPalindrome(self, head):
        temp=head
        # length=0
        lst=[]
        while(temp):
            lst.append(temp.data)
            temp=temp.next    
        n= len(lst)
        for i in range(int(n/2)):
            if lst[i]!=lst[n-i-1]:
                return False
        return True
# =============================================================================
# =============================================================================
# 94	Middle element of LL (Learn efficient approach)	https://www.geeksforgeeks.org/problems/insert-in-middle-of-linked-list/1?page=2&category=Linked%20List&sortBy=submissions
##tortoise and hare algo
def insertInMid(head,node):
    slow=head
    fast=head
    while fast.next!=None and fast.next.next!=None:
        slow=slow.next
        fast=fast.next.next # fast travels 2 times more than fast 
    node.next=slow.next
    slow.next=node
    return head
# =============================================================================
# =============================================================================
# 95	Find the intersection point of Y LL(Once you know traversal, apply node logic to solve this)	https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1?page=1&category=Linked%20List&sortBy=submissions
def intersetPoint(head1,head2):
    a,b = head1,head2
    while a != b:
        a = a.next if a is not None else head2
        b = b.next if b is not None else head1
    if a is not None:
        return a.data
    return -1
# =============================================================================
# =============================================================================
# 96	Union and Intersection of LL	https://www.geeksforgeeks.org/problems/union-of-two-linked-list/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
###create a set and add both lists there and then createa ll and move data from set to LL 
    def union(self, head1,head2):
        # return head of resultant linkedlist
        u = set()
        while head1:
            u.add(head1.data)
            head1 = head1.next
        while head2:
            u.add(head2.data)
            head2 = head2.next
        l =  linkedList()
        v = sorted(u)
        for i in v:
            l.insert(i)
    ###
#this code is timed out in Geek4geeks, but code is working need to find optimal solution
    def merge(ll1,ll2):
	if ll1 is None:
		return ll2
	if ll2 is None:
		return ll1
	if ll1.data==ll2.data:
		head=ll1
		tail=ll1
		ll1=ll1.next
		ll2=ll2.next
	elif ll1.data>ll2.data:
		head=ll2
		tail=ll2
		ll2=ll2.next
	else:
		head=ll1
		tail=ll1
		ll1=ll1.next
	while ll1 is not None and ll2 is not None:
		if ll1.data==ll2.data:
			tail.next=ll1
			tail=ll1
			ll1=ll1.next
			ll2=ll2.next
		elif ll1.data>ll2.data:
			tail.next=ll2
			tail=ll2
			ll2=ll2.next
		else:
			tail.next=ll1
			tail=ll1
			ll1=ll1.next
	if ll1 is not None:
		tail.next=ll1			
	if ll2 is not None:
		tail.next=ll2
	return head

def mid_point_2(head):
	if head is None:
		return None
	slow=head
	fast=head
	while fast.next is not None and fast.next.next is not None:
		slow=slow.next
		fast=fast.next.next
	return slow 	
def merge_sort(head):
	if head is None or head.next is None:
		return head
	mid=mid_point_2(head)
	head2=merge_sort(mid.next)
	mid.next=None
	head1=merge_sort(head)
	final_head=merge(head1,head2)
	return final_head
def union(head1,head2):
	# return head of resultant linkedlist	
	head1=merge_sort(head1)
	head2=merge_sort(head2)
	return merge(head1,head2)
	
# Driver Code Starts
#Initial Template for Python 3
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
def print_ll(head):
	while head is not None:
		print(head.data,end='-->')
		head=head.next
	print('None')
	
def take_input(l):
	if len(l)==0 or l[0]==-1:
		return
	head,tail=None,None
	for i in l:
		if i ==-1:
			break
		new_node=Node(i)
		if head is None:
			head=new_node
			tail=new_node
		else:
			tail.next=new_node
			tail=new_node
	return head
head1=take_input([10,20,30,40,50,60,70])
head2=take_input([10,30,50,80,90])
print_ll(union(head1,head2))
# =============================================================================
# =============================================================================
# 97	Delete without head pointer	https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1?page=1&category=Linked%20List&sortBy=submissions
def deleteNode(self,curr_node):
        curr_node.data=curr_node.next.data
        curr_node.next=curr_node.next.next
# =============================================================================
# =============================================================================
# 98	Count pairs with given sum	https://www.geeksforgeeks.org/problems/count-pairs-whose-sum-is-equal-to-x/1?page=2&category=Linked%20List&sortBy=submissions
class Solution:
    def countPair(self,h1,h2,n1,n2,x):
        res=0
        d={}
        for i in range(n1):
            if h1.data in d:
                d[h1.data]+=1
            else:
                d[h1.data]=1
            h1=h1.next
        #print(d)
        for j in range(n2):
            if x-h2.data in d:
                res+=1
            h2=h2.next
        return res
# =============================================================================
# =============================================================================
# 99	Reverse LL in groups of given size(Once you learn reverse of LL's efficient approach, you can try this)	https://www.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1?page=1&category=Linked%20List&sortBy=submissions
# 
    def reverse(self,head, k):
        current = head
        previous = None
        count = 0
        while current and count<k:
            following = current.next
            current.next = previous
            previous = current
            current = following
            count+=1
        if current!=None:
            head.next=self.reverse(current, k)
        return previous
# =============================================================================
