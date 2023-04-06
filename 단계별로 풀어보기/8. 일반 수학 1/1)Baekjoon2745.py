# 진법 변환

# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)

# B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

# 출력
# 첫째 줄에 B진법 수 N을 10진법으로 출력한다.

# 예제 입력 1 
# ZZZZZ 36
# 예제 출력 1 
# 60466175


import math
# 알파벳 리스트
from string import ascii_lowercase
alphabet_list = [i.upper() for i in list(ascii_lowercase)]
# 10-26 리스트
Num_List = list(range(10,36))

# 입력값
N, B = input().split()
B = int(B)

D = []
for i in range(len(N)):
   D.append(N[i])

for i in range(len(N)):
   for j in range(len(alphabet_list)):
      if D[i] == alphabet_list[j]:
         D[i] = Num_List[j]
         break

A = 0
C = len(D) - 1
for i in range(len(D)):
   A = A + int(D[i])*math.pow(B, C)
   C = C - 1

print(int(A))