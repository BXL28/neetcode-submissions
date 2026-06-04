class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        consecutive=set(nums)

        longest=0
        for n in nums:
            if (n-1) not in consecutive:
                length=0
                while (n+length) in consecutive:
                    length+=1
                longest =max(length,longest)
        return longest



        
        