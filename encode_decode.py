#Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            encoded_str += f"{len(i)}#{i}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            decoded_str = ""
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i : j])
            strs.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return strs
