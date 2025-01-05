from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        leftHashMap = defaultdict(int)
        rightHashMap = defaultdict(int)

        unique_Palindromic_Strings = set()

        for char in s: rightHashMap[char] += 1

        for middle in range(len(s)):
            rightHashMap[s[middle]] -= 1
            for leftChar in leftHashMap.keys():
                if leftChar in rightHashMap and rightHashMap[leftChar] > 0:
                    unique_Palindromic_Strings.add(leftChar+s[middle]+leftChar)
            
            leftHashMap[s[middle]] += 1

        return len(unique_Palindromic_Strings)