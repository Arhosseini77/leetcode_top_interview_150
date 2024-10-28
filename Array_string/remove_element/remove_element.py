class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = len(nums)
        indexes = []
        for i, v in enumerate(nums):
            if v == val:
                counter -= 1
                indexes.append(i)
        for index in sorted(indexes, reverse=True):
            del nums[index]
        print(nums)
        return counter


solution = Solution()

A = [2,3,4,5,5,6,5,6]
val = 5

print(solution.removeElement(A, val))
