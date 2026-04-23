#You are given an array of non-negative integers height which represent an elevation map.
#Each value height[i] represents the height of a bar, which has a width of 1.
#Return the maximum area of water that can be trapped between the bars.
class Solution:
    def trap(self, height: List[int]) -> int:
        area, max_l, max_r, l, r =0, height[0], height[-1],  0, len(height) - 1
        while l < r:
            if max_l <= max_r:
                l += 1
                area += max(0, max_l - height[l])
                max_l = max(max_l, height[l])
            else:
                r -= 1
                area += max(0, max_r - height[r])
                max_r = max(max_r, height[r])
        return area
