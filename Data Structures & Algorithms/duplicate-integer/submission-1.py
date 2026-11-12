class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = []
        nums3 = set()
        for i in nums:
            nums3.add(i)
            nums2.append(i)
        return len(nums2) != len(nums3)