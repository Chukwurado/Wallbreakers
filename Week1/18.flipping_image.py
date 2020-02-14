class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        new_image = []
        for row in A:
            new_row = []
            for c in row:
                new_row.append(1 if c == 0 else 0)
            new_image.append(new_row[::-1])
        return new_image