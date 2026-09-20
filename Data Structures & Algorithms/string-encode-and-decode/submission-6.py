class Solution:

    def encode(self, strs):
        enc = ""

        for s in strs:
            enc += str(len(s)) + "#" + s

        return enc

    def decode(self, s: str) -> List[str]:
        #The output
        dec = []
        i = 0
        while i < len(s):
            pos = s.index("#",i)
            n = int(s[i:pos])
            i = pos + 1
            word = s[i:i+n]
            dec.append(word)
            i += n
        return dec;
