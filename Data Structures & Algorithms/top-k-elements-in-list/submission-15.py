class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}

        for num in nums:
            if num not in numsMap:
                numsMap[num] = 1
            else:
                numsMap[num] += 1
        
        count_nums = list(numsMap.keys())
        count_amount = list(numsMap.values())
        count_amount_copy = count_amount.copy()

        largest_counts = []
        for i in range(k):
            max_num = max(count_amount_copy)
            largest_counts.append(max_num)
            count_amount_copy.remove(max_num)

        indexes = []
        indexes_new_copy = []
        for item in largest_counts:
            indx = count_amount.index(item)
            if indx in indexes:
                indexes_new = [index for index, obj in enumerate(count_amount) if item == obj]
                indexes_new_copy.extend(indexes_new)
            else:
                indexes.append(indx)

        for item in indexes_new_copy:
            if item not in indexes:
                indexes.append(item)
            else:
                continue

        highest_count_num = []
        for index in indexes:
            number = count_nums[index]
            highest_count_num.append(number)

        return highest_count_num