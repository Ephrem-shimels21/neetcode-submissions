class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToopen = {")": "(", "]": "[", "}":"{"}

        for p in s:
            if p in closeToopen:
                if stack and stack[-1] == closeToopen[p]:
                    stack.pop()
                
                else:
                    return False
            else:
                stack.append(p)
        
        return True if not stack else False


                


        