A = [2, 8, 6, 3, 9, 1, 7]
B = [0] * 7

for i in range(7):
  B[i]= (A[(i+2)%7])

print(B)
