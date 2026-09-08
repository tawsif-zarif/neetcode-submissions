class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            pair_num = target - num
            if pair_num in nums:
                if pair_num == num:
                    indexes = [i for i, num in enumerate(nums) if num == pair_num]
                    if len(indexes) < 2:
                        continue
                    else:
                        return [indexes[0], indexes[1]]
                else:
                    indx1 = nums.index(num)
                    indx2 = nums.index(pair_num)
                    return [indx1, indx2]
            else:
                continue
        