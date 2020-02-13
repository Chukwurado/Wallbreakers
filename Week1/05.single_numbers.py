def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if freq.get(n): freq[n] += 1
            else:
                freq[n] = 1
        for n in freq:
            if freq[n] == 1:
                return n