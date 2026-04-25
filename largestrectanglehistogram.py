#You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.
#Return the area of the largest rectangle that can be formed among the bars.
#Note: This chart is known as a histogram.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [[0, heights[0]]]
        length = len(heights)
        for i in range(1, length):
            if heights[i] >= stack[-1][1]:
                start = i
            while stack and heights[i] < stack[-1][1]:
                max_area = max(max_area, stack[-1][1] * (i - stack[-1][0]))
                start = stack[-1][0]
                stack.pop()
            stack.append([start, heights[i]])
        while stack:
            max_area = max(max_area, stack[-1][1] * (length - stack[-1][0]))
            stack.pop()
        return max_area
