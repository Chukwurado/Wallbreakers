def transpose(self, A: List[List[int]]) -> List[List[int]]:
        transposed = [[] for _ in range(len(A[0]))]
        for row in A:
            for i in range(len(row)):
                transposed[i].append(row[i])
        return transposed