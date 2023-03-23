N = int(input())
Star = 0
for i in range(1, N+1):
    Star = i
    print(str("*"*Star).rjust(N))