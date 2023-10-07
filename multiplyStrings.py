'''Shorter solution'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))   # Max length possible
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit                   # Main keypoint, i, j will effect the (i+j)th digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10
        print(res[::-1])

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:   #Remove leading zeros
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)



# class Solution:
#     def mult_single(self, num, a):
#         '''multiply num by a (single digit)'''
#         carry=0
#         ans=0
#         for i in range(len(num)-1, -1, -1):
#             cur_res=(int(num[i])*a+carry)%10
#             carry=(int(num[i])*a+carry)//10
#             ans+=pow(10, len(num)-1-i)*cur_res
#         if carry!=0:
#             ans+=pow(10, len(num))*carry
#         return ans
    
#     def single_sum(self, a, b):
#         '''sums two strings, and returns a string'''
#         min_ab=a if len(a)<len(b) else b
#         max_ab=b if len(a)<len(b) else a
#         i=0
#         carry=0
#         ans=''
#         while i<len(min_ab):
#             cur_res=str((int(min_ab[len(min_ab)-i-1])+int(max_ab[len(max_ab)-i-1])+carry)%10)
#             carry=(int(min_ab[len(min_ab)-i-1])+int(max_ab[len(max_ab)-i-1])+carry)//10
#             ans=cur_res+ans
#             i+=1
#         while i<len(max_ab):
#             cur_res=str((int(max_ab[len(max_ab)-i-1])+carry)%10)
#             carry=(int(max_ab[len(max_ab)-i-1])+carry)//10
#             ans=cur_res+ans
#             i+=1
#         if carry!=0:
#             ans=str(carry)+ans
#         return ans


#     def multiply(self, num1: str, num2: str) -> str:
#         '''Try to return a string itself, to save the headache of storing a very big int
#         Not possible in many languages'''
#         all_sum='0'
#         for i in range(len(num2)-1, -1, -1):
#             cur_sum=str((pow(10, len(num2)-1-i))*self.mult_single(num1, int(num2[i])))
#             print(cur_sum)
#             all_sum=self.single_sum(all_sum, cur_sum)
#         return all_sum
