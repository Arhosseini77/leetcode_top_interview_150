class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = len(nums) - 1
        max_reachable = 0

        for i, num in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + num)
            if max_reachable >= target:
                return True

        return False


# Create an instance of Solution
solution = Solution()

# Example test
nums = [2, 5, 0, 0, 4]
print(solution.canJump(nums))
