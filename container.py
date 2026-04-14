#You are given an integer array heights where heights[i] represents the height of the ith bar.
#You may choose any two bars to form a container. Return the maximum amount of water a container can store.
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_a = 0
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            max_a = max(area, max_a)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return max_a
