class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        count = [0]*(n+1)
        
        # Mark the ranges in difference array
        for l, r in queries:
            count[l] += 1
            if r+1 < n:
                count[r+1] -= 1
        
        # Prefix sum to get coverage per index
        for i in range(1, n):
            count[i] += count[i-1]
        
        # Check if each element can be decremented enough times
        for i in range(n):
            if count[i] < nums[i]:
                return False
        return True
