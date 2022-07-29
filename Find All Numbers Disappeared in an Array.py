#Approach - 1
#TC :O(n)
#SC :O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = [i + 1 for i in range(n)]
        return list(set(a) - set(nums))

#Approach - 1
#TC :O(n)
#SC :O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        mn = []
        for num in nums:
            d[num] = 1
            
        for num in range(1,len(nums)+1):
            if num not in d:
                mn.append(num)
        return mn