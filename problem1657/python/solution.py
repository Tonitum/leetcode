class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        hashmap1: dict[str,int] = {}
        hashmap2: dict[str,int] = {}
        for c in word1:
            hashmap1[c] = hashmap1.get(c, 0) + 1
        for c in word2:
            hashmap2[c] = hashmap2.get(c, 0) + 1

        if hashmap1.keys() != hashmap2.keys():
            return False
        
        values_map1: dict[int,int] = {}
        values_map2: dict[int,int] = {}

        for v in hashmap1.values():
            values_map1[v] = values_map1.get(v, 0) + 1
        for v in hashmap2.values():
            values_map2[v] = values_map2.get(v, 0) + 1

        if values_map1 != values_map2:
            return False

        return True
        
