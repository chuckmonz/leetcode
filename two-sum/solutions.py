from typing import List
class Solution(object):

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_needed = {}
        for i, x in enumerate(nums):
            if x in complement_needed:
                return [complement_needed[x], i]
            else:
                complement_needed[target - x] = i
        return False

examples = [
    {"nums":[2,7,11,15], "target":9},
    {"nums":[3,2,4], "target":6},
    {"nums":[3,3], "target":6},
]

sol = Solution()
for example in examples:
    print(sol.twoSum(example["nums"], example["target"]))
