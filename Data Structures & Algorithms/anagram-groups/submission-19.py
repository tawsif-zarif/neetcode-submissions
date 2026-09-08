class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_decomp = {}

        for word in strs:
            wordlist = list(word)
            wordlist.sort()
            wordlist = tuple(wordlist)
            if wordlist not in word_decomp:
                word_decomp[wordlist] = []
                word_decomp[wordlist].append(word)
            else:
                word_decomp[wordlist].append(word)
        
        return list(word_decomp.values())
            


        
            