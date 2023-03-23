C = int(input())
for i in range(1, C+1):
    L = list(map(int, input().split()))
    del L[0]
    U = sum(L)/len(L)
    D = []
    for i in range(len(L)):
        if U < L[i]:
            D.append(i)
    X = len(D)/len(L)*100
    print('%.3f'%X + "%")