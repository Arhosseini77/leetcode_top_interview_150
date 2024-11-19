def match_index(index, nums):
    match_idx = []
    for i in range(1, nums[index] + 1):
        if index + i < len(nums):
            match_idx.append(index + i)
    return match_idx


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = len(nums) - 1
        if target == 0 and nums:
            return True

        match_idx = match_index(0, nums)

        while match_idx:
            if target in match_idx:
                return True
            else:
                match_idx_tmp = []
                for elm in match_idx:
                    match_idx_tmp += (match_index(elm, nums))
            match_idx = list(set(match_idx_tmp))
        return False


# Create an instance of Solution
solution = Solution()

# Example test
nums = [3,2,1,0,4]
print(solution.canJump(nums))
