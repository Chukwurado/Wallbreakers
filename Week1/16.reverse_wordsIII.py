def reverseWords(s: str) -> str:
        s_arr = s.split()
        for i, word in enumerate(s_arr):
            s_arr[i] = word[::-1]
        return " ".join(s_arr)