class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0
        for op in operations:
            match op:
                case "+":
                    stack.append(stack[-1] + stack[-2])
                    result += stack[-1]
                case "D":
                    stack.append(stack[-1] * 2)
                    result += stack[-1]
                case "C":
                    result -= stack.pop()
                case _:
                    stack.append(int(op))
                    result += stack[-1]
        return result