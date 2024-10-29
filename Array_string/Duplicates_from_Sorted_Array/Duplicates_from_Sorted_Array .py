class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        temp = None
        for index, value in enumerate(nums):
            if value != temp:
                nums[counter] = nums[index]
                counter += 1
                temp = value
        print(nums[:counter])
        return counter

solution = Solution()

nums = [1,1,2,2,2,2,3,3]
print(solution.removeDuplicates(nums))
