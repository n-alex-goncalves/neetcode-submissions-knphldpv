class TimeMap:

    def __init__(self):
        self.dictionary = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.dictionary[key]
        l, r = 0, len(lst) - 1
        output = None
        while l <= r:
            mid = (l + r) // 2
            if lst[mid][0] <= timestamp:
                output = lst[mid]
                l = mid + 1
            else:
                r = mid - 1
        return output[1] if output else ""
        
