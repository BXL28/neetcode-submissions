class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            n=nums[i]
            if n==nums[i+1]:
                return True
        return False