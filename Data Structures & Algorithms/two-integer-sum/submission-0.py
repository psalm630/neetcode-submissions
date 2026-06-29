class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  #create a dictionary to hold explored items as keys and their indices as values

        for i, n in enumerate(nums): 
            diff = target - n #for each item in list find the difference between that and the target number
            if diff in prevMap: #check if the difference is already in the dictionary
                return [prevMap[diff], i] #return index of difference value and the seclected value
            prevMap[n] = i #if difference is not in the dictionary yet, add the selected value and continue through the list