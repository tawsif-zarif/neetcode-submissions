class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        already_multiplied = []
        final_list = []
        for index, num in enumerate(nums):
            if index == 0:
                already_multiplied.append(1)
            else:
                new_num = already_multiplied[-1] * nums[index - 1]
                already_multiplied.append(new_num)

        right_multiplier = 1
        for i in range(len(nums) - 1, -1, -1):
            final_ans = already_multiplied[i] * right_multiplier
            already_multiplied[i] = final_ans
            right_multiplier = right_multiplier * nums[i]

        return already_multiplied