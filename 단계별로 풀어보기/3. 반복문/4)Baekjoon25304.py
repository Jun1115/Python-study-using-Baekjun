X = int(input())
N = int(input())
R = 0
for i in range(N):
    A = list(map(int, input().split()))
    a = A[0] 
    b = A[1]
    R = R + a*b
if R == X:
    print("Yes")
else:
    print("No")