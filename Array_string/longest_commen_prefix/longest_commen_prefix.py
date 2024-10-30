class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        index_min = 0
        for i,words in enumerate(strs):
            if len(words) < len(strs[index_min]):
                index_min = i

        count = 0
        counter = ""
        for i in range(len(strs[index_min])):
            for j in range(len(strs)):
                if j != index_min:
                    if strs[index_min][i] == strs[j][i]:
                        count += 1
            if count == len(strs) - 1:
                counter += strs[index_min][i]
                count = 0
            else:
                return counter
        return counter


solution = Solution()

strs = ["flower","fkow"]
print(solution.longestCommonPrefix(strs))