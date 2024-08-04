from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Create a dictionary to count the occurrences of each number
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        max_length = 0
        # Iterate through the keys and check for consecutive keys
        for num in freq_map:
            if num + 1 in freq_map:
                curr_length = freq_map[num] + freq_map[num + 1]
                max_length = max(max_length, curr_length)
        
        return max_length

