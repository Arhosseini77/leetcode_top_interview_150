class Solution:
    def longestCommonPrefix(self, strs):
        """
        Finds the longest common prefix string amongst an array of strings.

        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Iterate through the remaining strings
        for s in strs[1:]:
            # Compare the current prefix with the string s
            while not s.startswith(prefix):
                # Reduce the prefix by one character
                prefix = prefix[:-1]
                # If there's no common prefix
                if not prefix:
                    return ""

        return prefix


# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         index_min = 0
#         for i,words in enumerate(strs):
#             if len(words) < len(strs[index_min]):
#                 index_min = i
#
#         count = 0
#         counter = ""
#         for i in range(len(strs[index_min])):
#             for j in range(len(strs)):
#                 if j != index_min:
#                     if strs[index_min][i] == strs[j][i]:
#                         count += 1
#             if count == len(strs) - 1:
#                 counter += strs[index_min][i]
#                 count = 0
#             else:
#                 return counter
#         return counter


solution = Solution()

strs = ["flower","fkow"]
print(solution.longestCommonPrefix(strs))