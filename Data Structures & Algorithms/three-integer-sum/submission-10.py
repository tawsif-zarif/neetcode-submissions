class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        for i, num in enumerate(nums):
            # Skip duplicate anchor numbers
            if i > 0 and nums[i - 1] == num:
                continue
            
            # Use standard positive pointers
            left = i + 1
            right = len(nums) - 1
            
            # The loop safely stops the exact moment pointers cross
            while left < right:
                current_sum = num + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Match found: append it
                    triplets.append([num, nums[left], nums[right]])
                    
                    # Move BOTH pointers inward to search for more valid pairs
                    left += 1
                    right -= 1
                    
                    # Skip duplicate inner numbers to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                elif current_sum > 0:
                    # Total is too big, shrink from the right
                    right -= 1
                else:
                    # Total is too small, grow from the left
                    left += 1
                    
        return triplets

        