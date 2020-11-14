class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        
        stack = []
        for cur in tokens:
            if cur in ['+','-','*','/']:
                a = int(stack.pop())
                b = int(stack.pop())
                if cur is '+':
                    stack.append(str(b + a))
                elif cur is '-':
                    stack.append(str(b - a))
                elif cur is '*':
                    stack.append(str(b * a))
                else:
                    stack.append(str(int((b / a))))
            else:
                stack.append(cur)

        return stack.pop()


val = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
tmp = Solution()
tmp.evalRPN(val)