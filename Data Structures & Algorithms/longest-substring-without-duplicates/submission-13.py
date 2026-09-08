class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        letterList = list(s)
        compSet = {}
        longSubLen = 0

        while right != len(letterList):
            if letterList[right] not in compSet:
                compSet[letterList[right]] = right
                right += 1
            else:
                if compSet[letterList[right]] >= left:
                    left = compSet[letterList[right]] + 1
                compSet[letterList[right]] = right
                right += 1

            if right - left > longSubLen:
                longSubLen = right - left

        return longSubLen




        