#Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
#Each product is guaranteed to fit in a 32-bit integer.
#Follow-up: Could you solve it in O(n) time without using the division operation?
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        length = len(nums)
        for i in range(1, length):
            prefix.append(prefix[-1] * nums[i - 1])
            postfix.insert(0, postfix[0] * nums[length - i])
        output = []
        for i in range(length):
            output.append(prefix[i] * postfix[i])
        return output
