from typing import List
class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low_index = 0
        high_index = len(nums) - 1

        while low_index < high_index:
            middle_index = (high_index + low_index) // 2
            if nums[middle_index] > target:
                high_index = middle_index - 1
            elif nums[middle_index] < target:
                low_index = middle_index + 1
            else:
                return middle_index
        
        return -1
        

examples = [
    {"nums": [-1,0,3,5,9,12], "target":9},
    {"nums": [-1,0,3,5,9,12], "target": 2}
]

sol=Solution()
for x in examples:
    print(sol.search(x["nums"], x["target"]))