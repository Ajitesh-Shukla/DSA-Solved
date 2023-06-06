class Solution:
    def get_primes(self, n):
        primes=[True]*151
        primes[0], primes[1]=False, False
        for i in range(2, int(151**0.5)):
            for j in range(i*i, 151, i):
                primes[j]=False
        all_primes=[]
        for i, b in enumerate(primes):
            if b==True:
                all_primes.append(i)
            if len(all_primes)==n:
                return all_primes
        
    def groupAnagrams(self, strs):
        '''create a map for every word and compare: Time: max(O(N*l), O(N^2*l)), Space O(N*l);
        Use prime number allotment for each character, anagrams will have same value when 
        characters are multiplied, Time O(O(N*l)): Space O(N*l)'''
        primes_26=self.get_primes(26)
        map={}
        for i, elem in enumerate(strs):
            prime_mult=1
            for charac in elem:
                prime_mult*=primes_26[ord(charac)-ord('a')]
            try:
                map[prime_mult].append(elem)
            except:
                map[prime_mult]=[elem]

        return [i for i in map.values()]
