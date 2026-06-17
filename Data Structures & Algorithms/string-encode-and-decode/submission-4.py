class Solution:
    def encode(self, strs: List[str]) -> str:
        str_encoded = ""
        str_encoded += str(len(strs)).rjust(2, "0")
        for s in strs:
            str_encoded += str(len(s)).rjust(3, "0")
            str_encoded += s
        return str_encoded

    def decode(self, s: str) -> List[str]:
        res = []
        counter = 2
        print(s)
        for i in range(0,int(s[0:2])):
            length = int(s[counter:counter+3])
            res.append(s[counter+3:counter+3+length])
            counter += (3 + length)
        return res
        