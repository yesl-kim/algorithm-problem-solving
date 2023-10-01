from bisect import bisect_left

class MedianFinder:
    def __init__(self):
        self.middle = -1
        self.arr = []
        
    
    def is_even_size(self):
        return len(self.arr) % 2 == 0
        

    def addNum(self, num: int) -> None:
        if self.is_even_size():
            self.middle += 1
        self.arr.insert(bisect_left(self.arr, num), num)
        

    def findMedian(self) -> float:
        i = self.middle
        if self.is_even_size():
            return sum(self.arr[i:i+2]) / 2
        else:
            return self.arr[i]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()