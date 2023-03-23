# 그룹 단어 체커

# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 
# 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

# 예제 입력 1 
# 3
# happy
# new
# year
# 예제 출력 1 
# 3
# 예제 입력 2 
# 4
# aba
# abab
# abcabc
# a
# 예제 출력 2 
# 1

# 입력받을 단어의 개수
Num = input()
Result_List = []
for i in range(int(Num)):
    Str = input()
    # 그룹 단어가 아닐 경우 for 문을 바로 나오기 위한 변수 선언
    TrueOrFalue = True
    # 그룹 단어 탐색 2중 for 문
    for j in range(len(Str)-2): # 그룹 단어인 것을 확인하는데 만약 해당 인덱스 뒤에 0개 혹은 1개 밖에 남지 않았다면 굳이 비교할 필요없음 고로 -2
        for h in range(j+2, len(Str)): # 해당 인덱스보다 작은 것을 확인할 필요 없기 때문에 시작 인덱스 j+2
            if Str[j] != Str[j+1] and Str[j] == Str[h]: #연달아 같은 알파벳이 나온다면 그룹 단어이기 때문에 그렇지 않을 조건 부여
                Result_List.append("0") # 만약 그룹 단어가 아니라면 결과 리스트에 "0" 추가
                TrueOrFalue = False # 그룹 단어가 아닌 것을 학인했음으로 바로 탈출
                break
        if(TrueOrFalue == False):
            break

print(int(Num) - Result_List.count("0")) # 총 단어의 개수와 그룹 단어가 아닌 단어의 개수를 빼서 그룹 단어의 개수 출력
