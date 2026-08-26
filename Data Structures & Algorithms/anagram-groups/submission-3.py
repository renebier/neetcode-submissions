class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        def stringCounts(st):
            st = st.lower()
            items = [0]*26
            for s in st:
                items[ord(s) - ord("a")] += 1
            return items

        for s in strs:
            d[tuple(stringCounts(s))].append(s)
        return list(d.values())

            
            