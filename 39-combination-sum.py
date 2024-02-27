class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(comb,start,sum):
            if sum > target:
                return
            elif sum == target:
                result.append(comb.copy())
                return
            for i in range(start, len(candidates)):
                if sum+candidates[i] > target:
                    continue
                comb.append(candidates[i])
                dfs(comb,i,sum+candidates[i])
                comb.pop()
        dfs([],0,0)
        return result
