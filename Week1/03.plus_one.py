def plusOne(self, digits: List[int]) -> List[int]:
        rev_digits = digits[::-1]
        sum_ = rev_digits[0] + 1
        carry = sum_ // 10
        rev_digits[0] = sum_ % 10
        for i in range(1, len(rev_digits)):
            sum_ = rev_digits[i] + carry
            carry = sum_ // 10
            rev_digits[i] = sum_ % 10
        if carry > 0:
            rev_digits.append(carry)
        return rev_digits[::-1]