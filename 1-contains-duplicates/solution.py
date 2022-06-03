from typing import List

class Solution:
    def containsDuplicates(self, nums: List[int]) -> bool:
        already_seen = set()
        for i in nums:
            if i in already_seen:
                return True
            else:
                already_seen.add(i)
        
        return False

sol = Solution()

examples = [[1,2,3,1],
[1,2,3,4],
[1,1,1,3,3,4,3,2,4,2]
]

for i in range(3):
    print(sol.containsDuplicates(examples[i]))