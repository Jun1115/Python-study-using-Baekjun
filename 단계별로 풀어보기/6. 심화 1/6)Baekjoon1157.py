# 단어 공부

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 예제 입력 1 
# Mississipi
# 예제 출력 1 
# ?
# 예제 입력 2 
# zZa
# 예제 출력 2 
# Z
# 예제 입력 3 
# z
# 예제 출력 3 
# Z
# 예제 입력 4 
# baaa
# 예제 출력 4 
# A

# 문자 입력 받은 후 대문자로 변환
Str1 = input().upper()

# 입력 받은 문자 속 알파벳 리스트 화 및 알파벳 순서로 정렬
Str1_List = []
for i in range(len(Str1)):
    Str1_List.append(Str1[i])
# 중복 제거 리스트 생성
Str1_Set = set(Str1_List)
Str1_Set = list(Str1_Set)
Str1_Set.sort()

# 각각의 알파벳 개수 리스트화
# 카운트 함수 쓸걸
Num_List = []
for i in range(len(Str1_Set)):
    Num = 0
    for j in range(len(Str1_List)):
        if Str1_Set[i] == Str1_List[j]:
            Num = Num + 1
    Num_List.append(Num)

# 알파벳 개수 리스트 속 최대값과 비교하여 결과 리스트에 추가
Result = []
for i in range(len(Num_List)):
    if max(Num_List) == Num_List[i]:
        Result.append(Str1_Set[i])

# 결과 출력
if len(Result) > 1:
    print("?")
elif len(Result) == 1:
    print(*Result)