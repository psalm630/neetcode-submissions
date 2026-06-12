class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums) 
        """
        In a set, duplicates are ignored so by converting the original list to a set, 
        if there are duplicates in the list, they will each only be added to the set once. 
        When you compare the length of the set and the list, it will be the same if it has no
        duplicates since every item in the list has been added to the set and return false for 
        the set not being shorter. If you compare the lengths and it does have duplicates, the 
        set will be shorter because it ignores any additonal items from the list that it already 
        contains, returning true.
        """