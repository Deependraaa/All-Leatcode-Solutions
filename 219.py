class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range (len(nums)):
            for j in range (len(nums)):
                if (i==j):
                    continue
                if (nums[i]==nums[j] and abs(i-j)<=k):
                    return True
            return False


                    
