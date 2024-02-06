# =============================================================================
# 19_Shortest Path	
# =============================================================================
# =============================================================================
# 19_Shortest Path Find shortest path in UG(Once you learn this, try to solve other probs in this pattern by yourself)	https://www.codingninjas.com/studio/problems/shortest-path-in-an-unweighted-graph_981297
"""	Time Complexity : O(N + M)
	Space Complexity : O( N + M ),
	where N is the number of nodes and M is number of edges."""
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
####################
from collections import deque
def shortestPath(edges, n, m, s, t):
    # We will store the graph in an adjacency list.
    adj = [[] for _ in range(n + 1)]
    
    # Making adjacency list from edges.
    for i in range(m):
        x = edges[i][0]
        y = edges[i][1]
        adj[x].append(y)
        adj[y].append(x)
    
    visited = [False] * (n + 1)
    distance = [float('inf')] * (n + 1)
    
    queue = deque()
    queue.append(s)
    visited[s] = True
    distance[s] = 0
    
    while queue:
        node = queue.popleft()

        for neighbor in adj[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                if neighbor == t:
                    return distance[t]
    
    return -1
# =============================================================================
# =============================================================================
# 164	Subarray with given sum	https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&category=sliding-window&sortBy=submissions
#Function to find a continuous sub-array which adds up to a given number. O(N),O(1)
class Solution:
    def subArraySum(self, arr, n, s):
        if s == 0 and 0 in arr:
            idx = arr.index(0) + 1
            return [idx, idx]

        cumulative_sum = {0: 0}
        current_sum = 0

        for i in range(n):
            current_sum += arr[i]
            if current_sum - s in cumulative_sum:
                start = cumulative_sum[current_sum - s] + 1
                end = i + 1
                return [start, end]
            cumulative_sum[current_sum] = i + 1

        return [-1]
# =============================================================================
# =============================================================================
# 165	Longest subarray with given sum k(Same as above with slight modification)	https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?page=1&category=sliding-window&sortBy=submissions 
#O(N),O(N)
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
  #Function to check whether there is a subarray present with 0-sum or not. O(N),O(N)
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
# 167	Smallest window of distinct elements	https://www.geeksforgeeks.org/problems/smallest-distant-window3132/1?page=1&category=sliding-window&sortBy=submissions O(N),O(1)
#User function Template for python3
class Solution:
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

		    min1=min(min1,j-i+1)
                dict1[s[i]]+=1
                count+=1
                i+=1
            j+=1
        return min1    
# =============================================================================
# =============================================================================
# 168	Smallest window containing 0,1,2	https://www.geeksforgeeks.org/problems/smallest-window-containing-0-1-and-2--170637/1?page=2&category=sliding-window&sortBy=submissions
#The time complexity of the smallestSubstring method is O(n^2), where n is the length of the input string S. This is because the code iterates through the string using two pointers, i and j, which move towards the right. The code checks if each substring between the two pointers contains the characters "0", "1", and "2". The check is performed using the in operator, which has a time complexity of O(m), where m is the length of the substring. As the pointers move, the code generates all possible substrings, resulting in a nested loop and a quadratic time complexity.
#The space complexity of the code is O(1), 
   class Solution:
    def smallestSubstring(self, S):
        i = 0
        j = 0
        res = float('inf')
        found = set()
        
        while j < len(S):
            found.add(S[j])
            
            while len(found) == 3:
                res = min(res, j - i + 1)
                found.remove(S[i])
                i += 1
            
            j += 1
        
        return res if res != float('inf') else -1

##################################
class Solution:
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
# 169	Smallest window in string containing all chars of another string	https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1?page=1&category=sliding-window&sortBy=submissions
#The time complexity of the smallestSubstring method is O(n), where n is the length of the input string s. This is because the code iterates through the string using two pointers, i and j, which move towards the right. The code uses a dictionary d to keep track of the count of each distinct character in the current window. The while loop inside the if condition and the while loop at the end both move the pointers i and j and update the dictionary d. Each character in the string is visited at most twice, once by each pointer.
#The space complexity of the code is O(1)
class Solution:
    def smallestWindow(self, s: str, p: str) -> str:
        if not s or not t:
            return ""
        
        countT = {}
        for char in p:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1

        required = len(countT)
        l, r = 0, 0
        formed = 0
        window = {}
        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            if character in window:
                window[character] += 1
            else:
                window[character] = 1

            if character in countT and window[character] == countT[character]:
                formed += 1

            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window[character] -= 1
                if character in countT and window[character] < countT[character]:
                    formed -= 1

                l += 1    
            r += 1    
        return -1 if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

######################################
class Solution:
    def smallestWindow(self, string, pat):
        no_of_chars = 256

        len1 = len(string)
        len2 = len(pat)

        if len1 < len2:
            return "-1"

        hash_pat = [0] * no_of_chars
        hash_str = [0] * no_of_chars

        for i in range(len2):
            hash_pat[ord(pat[i])] += 1

        start, start_index, min_len = 0, -1, float('inf')
        count = 0

        for j in range(len1):
            hash_str[ord(string[j])] += 1

            if hash_str[ord(string[j])] <= hash_pat[ord(string[j])]:
                count += 1

            if count == len2:
                while (hash_str[ord(string[start])] >
                       hash_pat[ord(string[start])] or
                       hash_pat[ord(string[start])] == 0):
                    if hash_str[ord(string[start])] > hash_pat[ord(string[start])]:
                        hash_str[ord(string[start])] -= 1
                    start += 1

                len_window = j - start + 1
                if min_len > len_window:
                    min_len = len_window
                    start_index = start

        if start_index == -1:
            return "-1"
        return string[start_index: start_index + min_len]
# =============================================================================
# =============================================================================
# 170	Length of longest substring	https://www.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1?page=1&category=sliding-window&sortBy=submissions
#The time complexity of the longestUniqueSubsttr method is O(n), where n is the length of the input string s. This is because the code iterates through the string using two pointers, l and r, which move towards the right. The code uses a set charSet to keep track of the unique characters in the current window. The while loop inside the main for loop checks if the current character is already present in the set, and if so, it removes the leftmost character from the set until the current character is no longer present. This ensures that the window only contains unique characters. The set operations, such as adding and removing elements, take constant time on average. Each character in the string is visited at most twice, once by each pointer.
#The space complexity of the code is O(k), where k is the number of unique characters in the input string s. This is because the code uses a set charSet to store the unique characters. The size of the set 
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
#The time complexity of the maxLen method is O(n), where n is the length of the input array arr. This is because the code iterates through the array once, calculating the cumulative sum at each index. For each cumulative sum, it checks if the sum exists in the dictionary dic and updates the length of the longest subarray if necessary. The dictionary operations, such as checking for existence and adding elements, take constant time on average.
#The space complexity of the code is O(n), where n is the length of the input array arr. 
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
#The time complexity of the search method is O(n + m), where n is the length of the pattern pat and m is the length of the text txt. This is because the code iterates through the text once, performing constant-time operations for each character. The Counter class is used to count the occurrences of each character in the pattern, which takes O(n) time. The code then compares the data dictionary, which contains the character counts of the current window in the text, with the c dictionary, which contains the character counts of the pattern. This comparison takes constant time. The code also updates the data dictionary when moving the window, which again takes constant time. Overall, the time complexity is linear with respect to the length of the text.
#The space complexity of the code is O(n), where n is the length of the pattern pat.
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
###################################leetocde fast code###########
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        
        return right - left + 1	

#####################	
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
#The time complexity of the totalFruit method is O(n), where n is the length of the input list fruits. This is because the code iterates through the list using a single pointer. The code keeps track of the two types of fruits in variables fruit1 and fruit2, and their corresponding counts in variables count1 and count2. The code also keeps track of the length of the latest streak of the same fruit in the variable latest_streak. The for loop iterates through each element in the list, and the code updates the variables accordingly. Each element in the list is visited exactly once.
#The space complexity of the code is O(1), as it uses a constant amount of extra space to store the variables res, fruit1, fruit2, count1, count2, and latest_streak.
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
#The time complexity of the totalFruit method is O(n), where n is the length of the input list fruits. This is because the code iterates through the list once, using a single pointer i. The code keeps track of the two types of fruits in variables f1 and f2, and their corresponding start and end pointers in variables s1, e1, s2, and e2. The code also updates the maximum count of fruits in the variable m. The for loop iterates through each element in the list, and the code updates the variables accordingly. Each element in the list is visited exactly once.
#The space complexity of the code is O(1), as it uses a constant amount of extra space to store the variables m, f1, f2, s1, e1, s2, and e2.
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
########leetcode best#################
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        helper = [-1] + [i for i, el in enumerate(nums) if el % 2] + [len(nums)]
        n = len(helper)
        for i in range(1, n - k):
            ans += (helper[i] - helper[i - 1]) * (helper[i + k] - helper[i + k - 1])

        return ans
# =============================================================================
# =============================================================================
# 176	Longest repeating char replacement	https://leetcode.com/problems/longest-repeating-character-replacement
#Input: s = "AABABBA", k = 1
#Output: 4
#Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
#The substring "BBBB" has the longest repeating letters, which is 4.
#There may exists other ways to achieve this answer too.
########################3leet code best #######################
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        freq_count = [0 for _ in range(26)]
        longest = 0
        m=0
        while right<len(s):
            freq_count[ord(s[right])-65] += 1
            m = max(freq_count[ord(s[right])-65],m)
            if (right-left+1)-m <= k:
                longest = right-left +1
                right+=1
            else:
                freq_count[ord(s[left])-65] -= 1
                left+=1
                right+=1
        return longest
###########################################################################	    
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        maxCount = 0
        maxLength = 0
        start = 0

        for end, ch in enumerate(s):
            counter[ch] += 1
            maxCount = max(maxCount, counter[ch])

            if end - start + 1 - maxCount > k:
                counter[s[start]] -= 1
                start += 1

            maxLength = max(maxLength, end - start + 1)

        return maxLength
###################################  remove visited dictionary and instead use a simpler array to store the count of characters.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        res = 0
        l = 0
        freq = 0

        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
            freq = max(freq, count[ord(s[r]) - ord('A')])

            while (r - l + 1) - freq > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
####################
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
##### optimised version as per leetcode
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

#### optimised version as per flowgpt
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        needstr = collections.Counter(t)
        needcnt = len(t)
        res = (0, float('inf'))
        left = 0

        for right, ch in enumerate(s):
            if needstr[ch] > 0:
                needcnt -= 1
            needstr[ch] -= 1

            while needcnt == 0:
                if right - left < res[1] - res[0]:
                    res = (left, right)
                needstr[s[left]] += 1
                if needstr[s[left]] > 0:
                    needcnt += 1
                left += 1

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
                    end = i + 1
                    while j > 0:
                        if str1[i] == str2[j-1]:
                            j -= 1
                        i -= 1
                    i += 1
                    current_window = str1[i:end]
                    if len(current_window) < min_window_length:
                        window = current_window
                        min_window_length = len(window)
            i += 1

        return window
###############
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
                    end = i + 1
                    while j > 0:
                        if str1[i] == str2[j-1]:
                            j -= 1
                        i -= 1
                    i += 1
                    current_window = str1[i:end]
                    if len(current_window) < min_window_length:
                        window = current_window
                        min_window_length = len(window)
            i += 1

        return window	    
# =============================================================================
# =============================================================================
# 179	Subarray with k diff integers	https://leetcode.com/problems/subarrays-with-k-different-integers/
###########################################
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def f(counts=[0] * (len(nums) + 1), low=0, high=0, k=k):
            for num in nums:
                if not counts[num]:
                    k -= 1
                    if k < 0:
                        counts[nums[high]] = 0
                        low = high = high + 1
                counts[num] += 1
                if k <= 0:
                    while counts[(a := nums[high])] > 1:
                        counts[a] -= 1
                        high += 1
                    yield high - low + 1

        return sum(f())     

#################leet code ###############3
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
