import PermutationInString
c=PermutationInString.Solution()
# s ="KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
s1 ="trinitrophenylmethylnitramine"
s2="dinitrophenylhydrazinetrinitrophenylmethylnitramine"
ans=c.checkInclusion(s1, s2)
print(ans)