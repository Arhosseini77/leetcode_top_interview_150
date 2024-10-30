class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        final_int = 0
        for index, roman in enumerate(s):
            value = dic.get(roman)
            if index == len(s) - 1 or dic.get(s[index + 1]) <= value:
                final_int += value
            else:
                final_int -= value
        return final_int


solution = Solution()

s = "LVIII"
print(solution.romanToInt(s))
