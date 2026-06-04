class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out={}
        for i,num in enumerate(nums):
            complement= target -num
            if complement in out:
                return [out[complement],i]
            out[num]=i
            
