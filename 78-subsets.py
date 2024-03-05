class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        end = len(nums)
        def backtracking(start,comb):
            res.append(comb.copy())
            for i in range(start,end): # 0 1 2
                if i+1 >= end:
                    res.append(comb+[nums[i]].copy())
                    return
                backtracking(i+1,comb+[nums[i]]) # 3
        res = []
        backtracking(0,[])
        return res
