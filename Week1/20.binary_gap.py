class Solution:
    def binaryGap(self, N: int) -> int:
        binary = bin(N)[2:]
        if binary.count("1") < 2: return 0
        max_gap = 0
        i = 0
        while i < len(binary):
            j = i + 1
            if binary[i] == '1':
                while j < len(binary) and binary[j] == '0':
                    j+= 1
            if j < len(binary):
                max_gap = max(max_gap, j - i)
            i = j
        return max_gap