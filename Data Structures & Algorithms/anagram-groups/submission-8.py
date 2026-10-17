class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()

        for s in strs:
            key = "".join(sorted(s))
            if key not in anagram_dict:
                anagram_dict[key]= []
            anagram_dict[key].append(s)
        return list(anagram_dict.values())


