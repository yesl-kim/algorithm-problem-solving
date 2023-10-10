from bisect import bisect_left

class MedianFinder:
    def __init__(self):
        self.middle = -1
        self.arr = []
        

    def addNum(self, num: int) -> None:
        if len(self.arr) % 2 == 0:
            self.middle += 1
        self.arr.insert(bisect_left(self.arr, num), num)
        

    def findMedian(self) -> float:
        i = self.middle
        if len(self.arr) % 2 == 0:
            return (self.arr[i] + self.arr[i+1]) / 2
        else:
            return self.arr[i]