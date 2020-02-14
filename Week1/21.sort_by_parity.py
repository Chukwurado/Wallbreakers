class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odds = [num for num in A if num % 2 == 1]
        evens = [num for num in A if num % 2 == 0]
        return sorted(evens) + sorted(odds)