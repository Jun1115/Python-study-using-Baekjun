# 소수 찾기

# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

# 예제 입력 1 
# 4
# 1 3 5 7
# 예제 출력 1 
# 3

N = int(input())
M = list(map(int, input().split(" ")))
A = 0
for i in range(N):
    O = []
    for j in range(M[i]+1):
        if M[i]/(j+1) == int(M[i]/(j+1)):
            O.append(j+1)
    if len(O) == 2:
        A = A + 1
print(A)