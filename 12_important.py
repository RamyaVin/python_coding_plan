# =============================================================================
# Must solve other probs(Try to solve these probs on own, brute force atleast you can come up for most of them after solving above)		
# =============================================================================
# 74	Aggressive cows	https://www.geeksforgeeks.org/problems/aggressive-cows/1?page=1&category=Binary%20Search&sortBy=submissions
    def solve(self,n,k,stalls):
        pass
        stalls.sort()
        l , h = 1 , stalls[-1] - stalls[0]
        def cowsAccomodated(m): #m no. of cows
            prev = stalls[0]
            temp = 1
            for i in range(1,len(stalls)):
                if stalls[i] - prev >= m:
                    temp += 1
                    prev = stalls[i]
                if temp == k: return True
            return False
      
        ret = 0
        while l <= h:
            m = (l + h) // 2
            if(cowsAccomodated(m)):
                ret = m
                l = m + 1
            else: h = m - 1
        return ret
# =============================================================================
# =============================================================================
# 75	Allocate minimum pages	https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article
# =============================================================================
# =============================================================================
# 76	Painter partition	https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1?page=1&category=Binary%20Search&sortBy=submissions
# =============================================================================
# =============================================================================
# 77	Split array largest sum	https://www.geeksforgeeks.org/problems/split-array-largest-sum--141634/1?page=2&category=Binary%20Search&sortBy=submissions
# =============================================================================
# =============================================================================
# 78	Minimum num of days to make m bouquets	https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
# =============================================================================
# =============================================================================
# 79	Capacity to ship packages within D days	https://www.geeksforgeeks.org/problems/capacity-to-ship-packages-within-d-days/1?page=2&category=Binary%20Search&sortBy=submissions
# =============================================================================
# =============================================================================
# 80	koko eating bananas	https://leetcode.com/problems/koko-eating-bananas/
# =============================================================================
# =============================================================================
# 81	kth smallest number in matrix multiplication table	https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
# =============================================================================
# =============================================================================
# 82	kth smallest pair distance	https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# =============================================================================
# =============================================================================
# 83	Ugly number II	https://leetcode.com/problems/ugly-number-ii/
# =============================================================================
# =============================================================================
# 84	Median of 2 sorted arrays	Median of 2 Sorted Arrays of Different Sizes | Practice | GeeksforGeeks
# =============================================================================
# =============================================================================
# 85	Find smallest divisor given threshold	Find the Smallest Divisor Given a Threshold - LeetCode
# 
# =============================================================================
