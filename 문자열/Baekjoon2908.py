N = input().split()
A = N[0][::-1]
B = N[1][::-1]
if A > B:
    print(A)
else:
    print(B)