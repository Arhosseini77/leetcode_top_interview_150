class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        for index, value in enumerate(nums):
            if value != val:
                nums[counter]=nums[index]
                counter += 1
        print(nums[:counter])
        return counter


solution = Solution()

A = [2,3,4,5,5,6,5,6]
val = 5

print(solution.removeElement(A, val))
