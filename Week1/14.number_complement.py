def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        compl = ""
        for b in binary:
            compl += '1' if b == '0' else '0'
        return int(compl, 2)