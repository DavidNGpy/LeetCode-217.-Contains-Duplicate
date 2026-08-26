#FIRST AND FASTER SOLUTION
from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

#SECOND AND SLOWER SOLUTION
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
