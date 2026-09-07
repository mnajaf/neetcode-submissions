class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        a = {"}":"{","]":"[",")":"("}

        for char in s:
            if char in a:
                if not stack:
                    return False
                else:
                    if stack[-1] == a[char]:
                        stack.pop()
                    else:
                        return False
            else:
                
                stack.append(char)

        return stack == []



            

        