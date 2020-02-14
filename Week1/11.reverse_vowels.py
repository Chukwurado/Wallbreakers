def reverseVowels(self, s: str) -> str:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        vowels_arr = [v for v in s if v.lower() in vowel_set]
        new_s = ""
        for c in s:
            if c.lower() in vowel_set:
                new_s += vowels_arr.pop()
            else:
                new_s += c
        return new_s