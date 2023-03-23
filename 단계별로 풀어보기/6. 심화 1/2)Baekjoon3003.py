N = list(map(int, input().split()))
M = [1, 1, 2, 2, 2, 8]
R = list()
for i in range(len(N)):
    if N[i] == M[i]:
        R.append(0)
    elif N[i] < M[i]:
        R.append(M[i] - N[i])
    else:
        R.append(M[i] - N[i])
print(' '.join(map(str,R)))