class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #Approach: sort array and simply add pairwise to find optimal sum
        add = 0
        sorted_nums = sorted(nums)
        for i in range(0,len(sorted_nums),2):
            add = add +min(sorted_nums[i], sorted_nums[i+1])
        return add

            
        
