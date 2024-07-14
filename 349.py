class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def findIntersection(set1,set2):
            return [ele for ele in set1 if ele in set2]
        set1=set(nums1)
        set2=set(nums2)

        if len(set1)<len(set2):
            return findIntersection(set1,set2)
        else:
            return findIntersection(set2,set1)
