class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        for i in nums:
            count=0
            for j in nums:
                if i==j:
                    count+=1
            if count>n//2:
                return i        
        