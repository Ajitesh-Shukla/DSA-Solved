class Solution:
    def containsDuplicate(self, nums) -> bool:
        '''can use sort, or map'''
        # Map, O(n) for both  time and space
        dict_map=set()
        for elem in nums:
            if elem in dict_map:
                return True
            dict_map.add(elem)
            
        return False

