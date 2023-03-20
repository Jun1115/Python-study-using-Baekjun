# 알파벳 찾기

# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

# 예제 입력 1 
# baekjoon
# 예제 출력 1 
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

# 알파벳 리스트 생성
from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)
Alphabet_Num = len(alphabet_list)

# 단어 입력
String = input()
Num_str = len(String)

# 결과 리스트 생성
Result_List = []
for i in range(Alphabet_Num):
    Result_List.append("-1")

# 결과 리스트 결과물 입력
for j in range(Num_str):
    for i in range(Alphabet_Num):
            if alphabet_list[i] == String[j]:
                if Result_List[i] != "-1":
                     break
                else:
                     Result_List[i] = str(j)
                     break

print(*Result_List)