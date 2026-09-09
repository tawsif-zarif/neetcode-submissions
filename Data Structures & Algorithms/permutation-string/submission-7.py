class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        left = 0
        right = 0

        for c in s1:
            if c in s1Map:
                s1Map[c] += 1
            else:
                s1Map[c] = 1
        
        s1Maptemp = s1Map.copy()
        while right < len(s2):
            if s2[right] not in s1Map:
                left = right + 1
                s1Maptemp = s1Map.copy() 
                right += 1
            else:
                s1Maptemp[s2[right]] -= 1
                if s1Maptemp[s2[right]] < 0:
                    left += 1                
                    right = left             
                    s1Maptemp = s1Map.copy() 
                    continue
                if sum(s1Maptemp.values()) == 0:
                    return True
                right += 1
        return False 




        