# =============================================================================
# 19_Shortest Path	
# =============================================================================
# =============================================================================
# 19_Shortest Path Find shortest path in UG(Once you learn this, try to solve other probs in this pattern by yourself)	https://www.codingninjas.com/studio/problems/shortest-path-in-an-unweighted-graph_981297
"""
	Time Complexity : O(N + M)
	Space Complexity : O( N + M ),

	where N is the number of nodes and M is number of edges.
"""
from queue import Queue

def shortestPath(edges, n, m, s, t):
    # We will store graph in an adjecency list.
    ADJ = [[] for _ in range(n + 1)]

    # Making adjacency list ADJ from edges.
    for i in range(m):
        X = edges[i][0]
        Y = edges[i][1]
        ADJ[X].append(Y)
        ADJ[Y].append(X)

    """
       Declaring visited array and parent array , visited will be used in dfs.
	   And parent will be use to recreate the path.
    """
    visited = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    visited[s] = 1

    """ 
        Starting BFS from node S.
	    Q is the queue used in bfs.
    """
    Q = Queue()
    Q.put(s)

    while (Q.qsize() > 0):

        # Selecting a node and traversing all its neighbours.
        currentNode = Q.get()

        for nextNode in ADJ[currentNode]:

            """
            	If the node is not already visited we will add it to the Q.
            	And we will set the currentNode the parent of nextNode.
            """
            if visited[nextNode] == -1:
                visited[nextNode] = 1
                Q.put(nextNode)
                parent[nextNode] = currentNode

    # Now we will backtrack and recreate the path from S to T using visited array.
    path = []
    currentNode = t

    # We will start from T and try to go back from here until we reaches S.
    path.append(t)

    while (currentNode != s):
        """
        	From current node we will find a neighbour who has distance equal to
            distance of current node - 1 , that node will be the parent of currentNode.
        """
        currentNode = parent[currentNode]
        path.append(currentNode)

    # We got path in from T to S , so we will reverse it and return it.
    path.reverse()
    return path

# =============================================================================
# =============================================================================
# 164	Subarray with given sum	https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&category=sliding-window&sortBy=submissions
#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        if((s == 0) and s in arr):  
            return [arr.index(0)+1,arr.index(0)+1]

        if(sum(arr) == s):
            return [1,n]
        start=0
        sum_c=0
        for i in range(0,n):
            sum_c=sum_c+arr[i]
            while(sum_c>s and i>start):
               sum_c=sum_c-arr[start]
               start=start+1
            if(sum_c==s):
                return (start+1,i+1)
        return [-1]
# =============================================================================
# =============================================================================
# 165	Longest subarray with given sum k(Same as above with slight modification)	https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?page=1&category=sliding-window&sortBy=submissions
class Solution:
    def lenOfLongSubarr (self, arr, nums, k) : 
        #Complete the function
        currsum = 0
        ans = 0
        prefix = {}
        prefix[0] = 0
        
        for i in range(n):
            currsum += arr[i]
            diff = currsum - k
            if diff in prefix:
                size = prefix[diff]
                ans = max(ans,i+1-size)
            if currsum in prefix:
                continue
            else:
                prefix[currsum] = i + 1
        return ans
# =============================================================================
# =============================================================================
# 166	Subarray with 0 sum	https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1?page=1&category=sliding-window&sortBy=submissions
  #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        set_sum=set()
        curr_sum=0
        for i in range(n):
            curr_sum+=arr[i]
            if curr_sum == 0 or curr_sum in set_sum:
                return 1
            set_sum.add(curr_sum)
                
        return 0
# =============================================================================
# =============================================================================
# 167	Smallest window of distinct elements	https://www.geeksforgeeks.org/problems/smallest-distant-window3132/1?page=1&category=sliding-window&sortBy=submissions
def findSubString(self, s):
        i=0
        j=0
        min1=1000000
        dict1={}
        for k in range(len(s)):
            if s[k] not in dict1:
                dict1[s[k]]=1
        count = len(dict1)
        # print(dict1)
        while j < len(s):
            if s[j] in dict1:
                dict1[s[j]]-=1
                if dict1[s[j]]==0:
                    count-=1
            if count==0:
                while s[i] not in dict1 or dict1[s[i]]<0 :
                    if s[i] in dict1:
                        dict1[s[i]]+=1
                    i+=1
                # print(f"i -> {i} and j -> {j}")
                min1=min(min1,j-i+1)
                dict1[s[i]]+=1
                count+=1
                i+=1
            j+=1
        return min1
# =============================================================================
# =============================================================================
# 168	Smallest window containing 0,1,2	https://www.geeksforgeeks.org/problems/smallest-window-containing-0-1-and-2--170637/1?page=2&category=sliding-window&sortBy=submissions
    def smallestSubstring(self, S):
        i=0
        j=3
        res=-1
        # main loop with index updates
        while j<=len(S):
            st=S[i:j]
            if ("0" in st) and ("1" in st) and ("2" in st):
                if res==-1: res=len(st)
                else: res=min(res,len(st))
                i+=1
            else: j+=1
        return res
# =============================================================================
# =============================================================================
# 169	Smallest window in string containing all chars of another string	https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1?page=1&category=sliding-window&sortBy=submissions
    def smallestSubstring(self, s):
        # Code here
        d = {}
        i = j = 0
        m = 100000
        while i < len(s):
            d[s[i]] = d.get(s[i],0) + 1
            if len(d) == 3:
                while len(d) == 3:
                    m = min(m,i-j+1)
                    d[s[j]] = d.get(s[j],0) - 1
                    if d[s[j]] == 0: d.pop(s[j])
                    j+=1
            i+=1
        return -1 if m >= 10**5 else m 
# =============================================================================
# =============================================================================
# 170	Length of longest substring	https://www.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1?page=1&category=sliding-window&sortBy=submissions
class Solution:
    def longestUniqueSubsttr(self, s):
        l = 0 
        r = 0 
        charSet = set()
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l = l + 1
            charSet.add(s[r])
            res = max(res,r-l + 1)
        return res 
# =============================================================================
# =============================================================================
# 171	Largest subarray of 0s and 1s	https://www.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1?page=1&category=sliding-window&sortBy=submissions
#maximum length of subarray having equal number of 0's and 1's is 4.
    def maxLen(self,arr, N):
        dic = {0:-1}
    
        ans= 0 
        cumulative_sum = 0 
        for i in range(N):
            cumulative_sum += 1 if arr[i]==1 else -1 
            
            if cumulative_sum in dic :
                length = i - dic[cumulative_sum]
                ans = max(ans , length)
            else :
                dic[cumulative_sum]= i 
                
        return ans
# =============================================================================
# =============================================================================
# 172	Count of anagram occurence(Super imp)	https://www.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1?page=1&category=sliding-window&sortBy=submissions
from collections import Counter
class Solution:
    def search(self,pat, txt):
        n=len(pat)
        m=len(txt)
        c=Counter(pat)
        data={}
        res=0
        for i in range(m):
            data[txt[i]]=data.get(txt[i],0)+1
            res+=data==c
            if i-n+1>=0:
                data[txt[i-n+1]]-=1
                if not data[txt[i-n+1]]: del data[txt[i-n+1]]
        return res
# =============================================================================
# =============================================================================
# 173	Max consecutive ones III	https://leetcode.com/problems/max-consecutive-ones-iii/
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1
# =============================================================================
# =============================================================================
# 174	Fruit into basket	https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        fruit1 = fruit2 = -1  # fruit2 is the latest fruit
        count1 = count2 = 0
        latest_streak = 0
        for fruit in fruits:
            if fruit == fruit1:
                count1 += 1
                fruit1, fruit2 = fruit2, fruit1
                count1, count2 = count2, count1
                latest_streak = 1
            elif fruit == fruit2:
                count2 += 1
                latest_streak += 1
            else:
                res = max(res, count1 + count2)
                fruit1 = fruit2
                count1 = latest_streak
                fruit2 = fruit
                count2 = 1
                latest_streak = 1
        res = max(res, count1 + count2)
        return res
#############
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        m, l = 0, len(fruits)
        f1, f2 = fruits[0], None ## fruit 1, fruit 2
        s1, s2 = 0, float('inf') ## pointers: start 1, start 2
        e1, e2 = 0, 0 ## pointers: end 1, end 2
        for i in range(1, l):
            curr, prev = fruits[i], fruits[i-1]
            if curr==f1:
                e1 = i
                continue
            elif curr==f2:
                e2 = i
                continue
            if f2==None: 
                f2, s2, e2 = curr, i, i
                continue

            m = max(m, i-min(s1,s2)) ## count the fruits
            
            if prev==f1: ## update pointers for new fruit 1 and 2
                s1 = e2+1
            else:
                f1, s1, e1 = f2, e1+1, i-1
            f2, s2, e2 = curr, i, i
        return max(m, l-min(s1,s2))   
# =============================================================================
# =============================================================================
# 175	Count number of nice subarrays	https://leetcode.com/problems/count-number-of-nice-subarrays/
# A continuous subarray is called nice if there are k odd numbers on it.
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        helper = [-1] + [i for i, el in enumerate(nums) if el % 2] + [len(nums)]

        for i in range(1, len(helper) - k):
            ans += (helper[i] - helper[i - 1]) * (helper[i + k] - helper[i + k - 1])

        return ans
#############
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total_count = 0
        current_count = 0
        L,R = 0,0
        n = len(nums)
        res = 0

        for R in range(n):
            if nums[R] % 2 != 0:
                current_count += 1
                total_count = 0
            if current_count == k:
                while L < n and nums[L] % 2 == 0:
                    total_count += 1
                    L += 1
                total_count += 1
                current_count -= 1
                L += 1
            res += total_count    
        return res
# =============================================================================
# =============================================================================
# 176	Longest repeating char replacement	https://leetcode.com/problems/longest-repeating-character-replacement
#Input: s = "AABABBA", k = 1
#Output: 4
#Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
#The substring "BBBB" has the longest repeating letters, which is 4.
#There may exists other ways to achieve this answer too.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        maxCount = 0
        l = 0
        for r, ch in enumerate(s):
            counter[ch] += 1
            if counter[ch] > maxCount:
                maxCount = counter[ch]
            elif maxCount + k < r - l + 1:
                counter[s[l]] -= 1
                l += 1
        return min(maxCount + k, len(s))
###################################
class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		visited = {}
		res = 0
		l = 0
		freq = 0

		for r in range(len(s)):
			visited[s[r]] = 1 + visited.get(s[r], 0)
			freq = max(freq, visited[s[r]])

			while (r - l + 1) - freq> k:
				visited[s[l]] -= 1
				l += 1

			res = max(res, r - l + 1)

		return res
# =============================================================================
# =============================================================================
# 177	Minimum window substring	https://leetcode.com/problems/minimum-window-substring/description/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        needstr = collections.defaultdict(int)
        for ch in t:
            needstr[ch] += 1
        needcnt = len(t)
        res = (0, float('inf'))
        start = 0
        for end, ch in enumerate(s):
            if needstr[ch] > 0:
                needcnt -= 1
            needstr[ch] -= 1
            if needcnt == 0:
                while True:
                    tmp = s[start]
                    if needstr[tmp] == 0:
                        break
                    needstr[tmp] += 1
                    start += 1
                if end - start < res[1] - res[0]:
                    res = (start, end)
                needstr[s[start]] += 1
                needcnt += 1
                start += 1
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]
# =============================================================================
# =============================================================================
# 178	Minimum window subsequence(Understand the diff between subarray and subsequence before starting this prob)	https://leetcode.com/problems/minimum-window-subsequence/
 
# Input: 
# str1: geeksforgeeks
# str2: eksrg
# eksforg

class Solution:
    def minWindow(self, str1, str2):
        window = ""
        i = 0
        j = 0
        min_window_length = len(str1) + 1

        while i < len(str1):
            if str1[i] == str2[j]:
                j += 1
            if j == len(str2):
                j -= 1
                end = i + 1
                while j >= 0:
                    if(str1[i] == str2[j]):
                        j -= 1
                    i -= 1
                    if(j < 0):
                        i += 1
                        current_window = str1[i:end]
                        if len(current_window) < min_window_length:
                            window = current_window
                            min_window_length = len(window)
                j +=1
            i += 1

        return window
# =============================================================================
# =============================================================================
# 179	Subarray with k diff integers	https://leetcode.com/problems/subarrays-with-k-different-integers/
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def f(counts=[0] * (len(nums) + 1), low=0, high=0, k=k):
            for num in nums:
                if not counts[num]:
                    if (k := k - 1) < 0:
                        counts[nums[high]] = 0
                        low = high = high + 1
                counts[num] += 1
                if k <= 0:
                    while counts[(a := nums[high])] > 1:
                        counts[a] -= 1
                        high += 1
                    yield high - low + 1

        return sum(f())     
# =============================================================================
# =============================================================================
