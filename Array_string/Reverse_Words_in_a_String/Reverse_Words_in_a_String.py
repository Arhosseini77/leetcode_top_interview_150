class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])


solution = Solution()
s = "the sky is blue"
print(solution.reverseWords(s))