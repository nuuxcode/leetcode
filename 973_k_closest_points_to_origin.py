class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []

        for i in points:
            dist = sqrt(pow(i[0], 2) + pow(i[1], 2))

            if len(arr) < k:
                heapq.heappush(arr, (-dist, i))
            elif dist < abs(arr[0][0]):
                heapq.heapreplace(arr, (-dist, i))

        return [point for _, point in arr]
