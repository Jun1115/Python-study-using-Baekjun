# 별 찍기 - 7

# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

# 예제 입력 1 
# 5
# 예제 출력 1 
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

N = int(input())

j = 2*N-1
b = N-1
for i in range(2*N-1):
    if i+1 <= N:
        a = " "*b + "*"*(2*(i+1)-1)
        print(a)
        b = b - 1
    else:
        if b == -1:
            b = 1
        print(" "*b + "*"*(2*(j)-1))
        b = b + 1
    j = j - 1
