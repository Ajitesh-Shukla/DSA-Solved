'''The expressions can be complicated, but you need an operator, 
and two numbers preceeding that each time
Tak the reversed token as a stack, add its elements to another stack,
'''
import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops=['+', '-', '*', '/']
        tokens=tokens[::-1]
        s2=[]
        while tokens:
            elem_cur=tokens.pop(-1)
            if elem_cur not in ops:
                s2.append(int(elem_cur))
            else:
                num1=s2.pop(-1)
                num2=s2.pop(-1)
                if elem_cur=='+':
                    s2.append(num1+num2)
                elif elem_cur=='-':
                    s2.append(num2-num1)   # earlier element is behind in 
                elif elem_cur=='*':
                    s2.append(num1*num2)
                elif elem_cur=='/':
                    s2.append(math.trunc(num2/num1))
        return s2[0]