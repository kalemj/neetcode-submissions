class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i,n in enumerate(nums):
            addition = target - n
            if addition in arr:
                return [arr[addition],i ]
            arr[n] = i