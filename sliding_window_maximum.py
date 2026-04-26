#You are given an array of integers nums and an integer k.
#There is a sliding window of size k that starts at the left edge of the array.
#The window slides one position to the right until it reaches the right edge of the array.
#Return a list that contains the maximum element in the window at each step.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = collections.deque()
        l = 0
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if l > queue[0]:
                queue.popleft()
            if i + 1 >= k:
                res.append(nums[queue[0]])
                l += 1
        return res
