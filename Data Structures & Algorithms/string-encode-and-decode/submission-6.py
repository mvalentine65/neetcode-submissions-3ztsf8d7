class Solution:

    def _process_input(self, string: str) -> str:
        return str(len(string)) + '#' + string
    def encode(self, strs: List[str]) -> str:
        return "".join((self._process_input(s) for s in strs))
        
        
    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j+1
            output.append(s[i:i+length])
            i += length
        return output