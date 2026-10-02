class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(token)
            
            else:
                oper1, oper2 = int(stack.pop()), int(stack.pop())
                if token == "+":
                    stack.append(oper2 + oper1)
                
                elif token == "-":
                    stack.append(oper2 - oper1)
                
                elif token == "*":
                    stack.append(oper2 * oper1)
                
                elif token == "/":
                    stack.append(oper2 / oper1)
        
        return int(stack[0])
               
        
        