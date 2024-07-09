class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_dublicate_list=[]
        for i in nums:
            if i not in no_dublicate_list:
                no_dublicate_list.append(i)
            else:
                no_dublicate_list.remove(i)
        return no_dublicate_list.pop()
