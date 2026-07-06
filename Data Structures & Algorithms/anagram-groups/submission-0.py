class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #intialize default dictionary to hold elements inside a list assigned to an automatically generated key
        for s in strs:
            sortedS = ''.join(sorted(s)) #sort the word and join the letters together for 1 item
            res[sortedS].append(s) #add the unsorted word to the dict under the key of the sorted word
        return list(res.values())