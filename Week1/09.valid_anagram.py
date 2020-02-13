def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for c in s:
            if freq.get(c):
                freq[c] += 1
            else:
                freq[c] = 1
        for c in t:
            if not freq.get(c):
                return False
            freq[c] -= 1
        return True