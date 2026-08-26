class Solution:
    def encode(self, strs: List[str]) -> str:
        delkey = "#"
        newStr = ""
        for s in strs:
            delimiter = str(len(s)) + delkey
            newStr += delimiter + s
        return newStr

    def decode(self, s: str) -> List[str]:
        delkey = "#"
        l = list()
        while s:
            delimiter, entry = s.split(delkey, 1)
            length = int(delimiter)
            l.append(entry[:length])
            s = entry[length:]
        return l