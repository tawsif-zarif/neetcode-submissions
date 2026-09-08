class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charList = list(s)
        charMap = {}
        lenLongSub = 0
        right = 0
        left = 0

        while right != len(charList):
            if charList[right] not in charMap:
                charMap[charList[right]] = 1
                if (right - left + 1) - max(charMap.values()) <= k:
                    lenLongSub = (right - left + 1)
                else:
                    charMap[charList[left]] -= 1
                    left += 1
                right += 1
            else:
                charMap[charList[right]] += 1
                if (right - left + 1) - max(charMap.values()) <= k:
                    lenLongSub = (right - left + 1)
                else:
                    charMap[charList[left]] -= 1
                    left += 1
                right += 1
        
        return lenLongSub



        