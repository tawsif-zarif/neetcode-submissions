class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_pure = []
        for num in nums:
            if num not in nums_pure:
                nums_pure.append(num)
            else:
                return True
        return False
        