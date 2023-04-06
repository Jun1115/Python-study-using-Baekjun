import math

N = list(map(int, input().split()))
A = N[0]
B = N[1]
V = N[2]

R = math.ceil((V - B)/(A - B))
print(R)