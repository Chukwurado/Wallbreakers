def titleToNumber(self, s: str) -> int:
        n = len(s)
        col = ord(s[n-1]) - ord("A") + 1
        for i in range(n-2, -1, -1):
            char_col = ord(s[i]) - ord("A") + 1
            col += 26 ** (n-i-1) * char_col
        return col