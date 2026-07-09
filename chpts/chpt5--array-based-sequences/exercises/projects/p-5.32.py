# Write a python func that takes two 3-d num data sets and adds them componentwise
from typing import List

def t_dim_add(A: List, B: List):
    res = [[0] * 3 for _ in range(len(A))]
    # A = [[1, 2, 3], [...]]
    # B = [[1, 2, 3], [...]]
    
    if len(A) != len(B):
        raise ValueError("Unequal length")
    
    for i in range(len(A)):
        res[i][0] = A[i][0] + B[i][0]
        res[i][1] = A[i][1] + B[i][1]
        res[i][2] = A[i][2] + B[i][2]
    
    return res

if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[2, 4, 6], [8, 10, 12]]
    
    res = t_dim_add(A, B)
    
    print(res)