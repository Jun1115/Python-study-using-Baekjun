N = list(map(int, input().split()))
M = list(map(int, input().split()))
L = list()
for i in range(N[0]):
    if N[1] > M[i]:
        L.append(M[i])

print(' '.join(map(str,L)))