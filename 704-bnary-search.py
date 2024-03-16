class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search2(nums, target,len(nums)-1,0)
    def search2(self, nums: List[int], target: int, high, low) -> int:
        if low > high:
            return -1
        mid = (low+high) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.search2(nums,target,high,mid + 1)
        else:
            return self.search2(nums,target,mid - 1,low)
