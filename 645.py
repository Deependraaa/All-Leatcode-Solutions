class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x, y = 0, 0
        tmp = 0
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        s = set()

        for i in nums:
            if i in s:
                y = i
            else:
                s.add(i)
                tmp += i

        x = expected_sum - tmp
        return [y, x]
