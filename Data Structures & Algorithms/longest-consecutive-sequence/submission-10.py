class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count_len_final = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 in num_set:
                continue
            else:
                count_len = 1
                while num + 1 in num_set:
                    count_len += 1
                    num += 1
                if count_len > count_len_final:
                    count_len_final = count_len
                else:
                    continue


        return count_len_final
        