def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if past.get(diff):
                return [past[diff]-1, i]
            past[nums[i]] = i + 1