class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #compare the length of the two strings first always because a difference in length is an automatic indicator that the two strings are not anagrams
            return False

        return sorted(s) == sorted(t) #if two strings are anagrams of each other, they should be the exact same when sorted because they have the same letters. If they are the same it will be true and if not it will return false 