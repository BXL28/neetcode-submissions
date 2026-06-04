class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dup = {}
        out = []
        
        
        for num in nums:  
            if num in dup:
                dup[num] += 1
            else:
                dup[num] = 1

        
        for i in range(k):
            most = max(dup, key=dup.get)
            out.append(most)
            del dup[most]  
            
        return out
