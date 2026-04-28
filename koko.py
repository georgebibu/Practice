#You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
#You are also given an integer h, which represents the number of hours you have to eat all the bananas.
#You may decide your bananas-per-hour eating rate of k.
#Each hour, you may choose a pile of bananas and eats k bananas from that pile.
#If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
#Return the minimum integer k such that you can eat all the bananas within h hours.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low <= high:
            k = (low + high) // 2
            time = 0
            for i in piles:
                time += math.ceil(i / k)
            if time <= h:
                res = min(res, k)
                high = k - 1
            else:
                low = k + 1
        return res
