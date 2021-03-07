class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                c+=nums[i]==nums[j]
        return c