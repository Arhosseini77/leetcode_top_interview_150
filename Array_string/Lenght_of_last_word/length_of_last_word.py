class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])


solution = Solution()

s = "   fly me   to   the moon  "
print(solution.lengthOfLastWord(s))

