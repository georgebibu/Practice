#You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#The input string s is valid if and only if:
#Every open bracket is closed by the same type of close bracket.#Open brackets are closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.
#Return true if s is a valid string, and false otherwise.
class Solution:
    def isValid(self, s: str) -> bool:
        k = {')' : '(', ']' : '[', '}' : '{'}
        stack = []
        for i in s:
            if i not in k:
                stack.append(i)
            else:
                if stack == [] or k[i] != stack.pop():
                    return False
        if stack != []:
            return False
        return True
