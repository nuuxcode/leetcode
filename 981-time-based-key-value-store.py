class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap: #if key doesnt exist in hashmap:
            self.hashmap[key] = [] # create key, with empty array
        self.hashmap[key].append([value,timestamp]) # add value and timestamp to the array

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashmap:
            data = self.hashmap[key]
            if data[0][1] > timestamp:
                return ""
            if data[-1][1] <= timestamp:
                return data[-1][0]
            left = 0
            right = len(data) - 1
            while left < right:
                mid = (left + right) // 2
                if data[mid][1] == timestamp:
                    return data[mid][0]
                if data[mid][1] > timestamp:
                    right = mid
                else:
                    if data[mid+1][1] > timestamp:
                        return data[mid][0]
                    left = mid + 1
        return ""
