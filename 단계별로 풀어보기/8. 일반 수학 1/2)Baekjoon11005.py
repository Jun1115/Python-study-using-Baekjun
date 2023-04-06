# 진법 변환 2

# 10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.

# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 10진법 수 N을 B진법으로 출력한다.

# 예제 입력 1 
# 60466175 36
# 예제 출력 1 
# ZZZZZ

# 알파벳 리스트
from string import ascii_lowercase
alphabet_list = [i.upper() for i in list(ascii_lowercase)]
# 10-26 리스트
Num_List = list(range(10,36))

#입력값
N, B = list(map(int,input().split()))

A = []
if N < B:
      A.append(N)
else:
   while True:
      A.append(N%B)
      N = N//B
      if B > N:
         A.append(N)
         break
A.reverse()

for i in range(len(A)): 
   for  j in range(len(alphabet_list)):
      if A[i] == Num_List[j]:
         A[i] = alphabet_list[j]
         break

print(''.join(list(map(str, A))))