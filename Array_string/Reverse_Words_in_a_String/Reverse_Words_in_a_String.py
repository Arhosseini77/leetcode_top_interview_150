class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        s = ""
        for word in words:
            s += word
            if word is not words[-1]:
                s += " "
        return s


solution = Solution()
s = "the sky is blue"
print(solution.reverseWords(s))