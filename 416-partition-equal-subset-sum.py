class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        if len(nums) == 2:
            return nums[0] == nums[1]
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dps = set()
        dps.add(0)
        nums.sort(reverse=True)
        for num in nums:
            copy = dps.copy()
            for dp in copy:
                total = num + dp
                if total == target:
                    return True
                dps.add(total)
        return False
