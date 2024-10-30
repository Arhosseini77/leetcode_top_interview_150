class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            if haystack[i:].startswith(needle):
                return i
        return -1


solution = Solution()
haystack = "hello"
needle = "ll"
print(solution.strStr(haystack, needle))
