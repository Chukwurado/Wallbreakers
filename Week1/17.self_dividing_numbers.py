def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numbers = []
        for i in range(left, right+1):
            if self.isSelfDividing(i):
                numbers.append(i)
        return numbers
                
    
    def isSelfDividing(self, num):
        str_num = str(num)
        if str_num.count('0') > 0: return False
        return all(num % int(c) == 0 for c in str_num)