from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque([])
        open_close={'(':')', '{': "}", '[':']'}
        for elem in s:
            if elem in open_close.keys():
                stack.append(elem)
            elif not stack:
                return False
            else:
                elem_cur=stack.pop()
                if elem!=open_close[elem_cur]:
                    return False
        return True if not stack else False