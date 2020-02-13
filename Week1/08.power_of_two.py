def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True
        return n > 0 and int(bin(n)[3:], 2) == 0