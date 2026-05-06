#Design a class to find the kth largest integer in a stream of values, including duplicates.
#E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.
#Implement the following methods:
#constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
#int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
