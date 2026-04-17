#You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
#Return the integer that represents the evaluation of the expression.
#The operands may be integers or the results of other operations.
#The operators include '+', '-', '*', and '/'.
#Assume that division between integers always truncates toward zero.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(i))
        return stack[0]
