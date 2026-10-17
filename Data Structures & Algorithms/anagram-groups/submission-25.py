class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)
            if key not in anagram_dict:
                anagram_dict[key] = []
            anagram_dict[key].append(string)
        return list(anagram_dict.values())
    


