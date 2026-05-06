#You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.
#Return the k closest points to the origin (0, 0).
#The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
#You may return the answer in any order.
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minheap.append([dist, x, y])
        heapq.heapify(minheap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minheap)
            res.append([x, y])
            k -= 1
        return res
