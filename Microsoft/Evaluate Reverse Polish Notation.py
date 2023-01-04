class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ''' Make use of stack; 2 cases -
                > If operand, push to stack
                > If operator; pop last 2 operands, perform respective operation and push result back onto stack
        
        In case of '/'; perform int(x1 / x2). If stack is ['24', '12'] and we encounter '/'; pop '24' and '12' and perform int(24 / 12) = 2, and push '2' to stack => stack = ['2']
        '''

        stack = []
        for token in tokens:
            if token.isdigit() or len(token) > 1:
                stack.append(token)
            else:
                n2 = stack.pop()
                n1 = stack.pop()

                if token == "+":
                    n = str(int(n1) + int(n2))
                    stack.append(n)
                elif token == "-":
                    n = str(int(n1) - int(n2))
                    stack.append(n)
                elif token == "*":
                    n = str(int(n1) * int(n2))
                    stack.append(n)
                else:
                    n = str(int(int(n1) / int(n2)))
                    stack.append(n)
        
        return int(stack[0])