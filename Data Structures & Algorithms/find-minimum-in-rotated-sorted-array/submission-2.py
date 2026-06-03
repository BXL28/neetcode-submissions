class Solution:
    def findMin(self, nums: List[int]) -> int:
        least=1000000000
        for i in nums:
            if i<least:
                least=i
        return least
            