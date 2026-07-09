import sys

data = []

for i in range(26):
    a = len(data)
    b = sys.getsizeof(data)
    
    print(f'Length: {a:3d}; Size in bytes: {b:4d}')
    data.append(None)

