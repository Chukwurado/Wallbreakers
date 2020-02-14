class Solution:
    def isHappy(self, n: int) -> bool:
        prev_nums = set()
        while n != 1:
            square_sum = self.digitSquareSum(n)
            if square_sum in prev_nums:
                return False
            prev_nums.add(square_sum)
            n = square_sum
        return True
        
    def digitSquareSum(self, n):
        sum_ = 0
        for d in str(n):
            sum_ += int(d) ** 2
        return sum_