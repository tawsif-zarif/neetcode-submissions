class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = -1

        while True:
            if numbers[i] + numbers[j] == target:
                return [i + 1, len(numbers) + j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
        