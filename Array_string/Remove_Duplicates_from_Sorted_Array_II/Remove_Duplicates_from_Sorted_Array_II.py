class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        temp = nums[0]
        count = -1
        for index, value in enumerate(nums):
            if value == temp and count <1:
                nums[counter] = nums[index]
                counter += 1
                count +=1
            elif value != temp:
                nums[counter] = nums[index]
                counter += 1
                temp = value
                count = 0

        print(nums[:counter])
        return counter

solution = Solution()

nums = [0,0,1,1,1,1,2,3,3]
print(solution.removeDuplicates(nums))