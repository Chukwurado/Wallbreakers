def isPalindrome(self, s: str) -> bool:
        import re
        new_s = "".join(re.split("[^a-zA-Z0-9]", s)).lower()
        return new_s == new_s[::-1]