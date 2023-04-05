# Python-study-using-Baekjun


## 1
sort 함수 안에 int, float 안넣어주면 맨 앞 숫자만 보고 판단함
ex) [13, 35, 46,67, 2,5 7,75] → [13, 2, 35 ....]

## 2
~~~
>>> a = range(10)
>>> a
range(0, 10)
~~~

range(10)은 0부터 10 미만의 숫자를 포함하는 range 객체를 만들어 준다.

시작 숫자와 끝 숫자를 지정하려면 range(시작 숫자, 끝 숫자) 형태를 사용하는데, 이때 끝 숫자는 포함되지 않는다.

## 3
리스트 요소 한 줄 쓰기
https://yeomss.tistory.com/160

## 4
set(집합)
set은 수학에서 이야기하는 집합과 비슷합니다.
순서가 없고, 집합안에서는 unique한 값을 가집니다.
그리고 mutable 객체입니다

## 5
arr[A:B:C]의 의미는, index A 부터 index B 까지 C의 간격으로 배열을 만들어라는 말입니다.
만약 A가 None 이라면, 처음부터 라는 뜻이고
B가 None 이라면, 할 수 있는 데까지 (C가 양수라면 마지막 index까지, C가 음수라면 첫 index까지가 되겠습니다.)라는 뜻입니다.
마지막으로 C가 None 이라면 한 칸 간격으로 라는 뜻입니다.

## 6
리스트 요소들의 각 개수를 세려고

~~~
Num_List = []
for i in range(len(Str1_Set)):
    Num = 0
    for j in range(len(Str1_List)):
        if Str1_Set[i] == Str1_List[j]:
            Num = Num + 1
    Num_List.append(Num)
~~~

이렇게 뻘짓 했는데
count() 를 사용했으면 간단하게 됐을 거였음..

## 7
VSCODE Ctrl 과 Alt 키를 누른 상태에서 키보드 방향키로 다중 선택이 가능

## 8 
~~~
사용법
값 가져오기 : result = df.at['행', '열']
값 설정하기 : df.at['행', '열'] = value

예시
먼저 아래와 같이 기본적인 2x2 행렬을 만듭니다.

df = pd.DataFrame([[1,2], [3,4]], index=['row1', 'row2'], columns=['col1', 'col2'])
print(df)
>>
     col1 col2
row1   1    2 
row2   3    4
~~~

## 9
이차원 배열 색종이 문제가 진짜 

## 10
Ctrl + Shift + L (같은 단어 한번에 모두 선택)
Ctrl + Shift + L 단축키를 누르면, 선택한 단어와 같은 단어가 모두 선택됩니다.


## 11
에라토스테네스의 체 알고리즘
-범위 속 소수 찾기
~~~
https://freedeveloper.tistory.com/392
~~~
- 1은 소수도 합성수도 아니다

## 12
삼각수 

~~~
http://sjoh.hannam.ac.kr/mathhis/triang/#:~:text=%EC%82%BC%EA%B0%81%EC%88%98%203%E8%A7%92%E6%95%B8%5Btriangular%20number%5D&text=%EB%8F%8C%EC%9D%84%20%EB%82%98%EB%9E%80%ED%9E%88%20%EB%86%93%EC%95%98%EC%9D%84,%EC%B4%9D%EC%88%98%EB%A5%BC%20%EB%82%98%ED%83%80%EB%82%B4%EB%8A%94%20%EC%88%98%EC%97%B4%EC%9D%B4%EB%8B%A4.&text=%EC%B4%88%ED%95%AD%EC%9D%B4%201%2C%20%EA%B3%B5%EC%B0%A8%EA%B0%80,n%ED%95%AD%EC%9C%BC%EB%A1%9C%20%ED%95%98%EB%8A%94%20%EC%88%98%EC%97%B4.
~~~

## 13
리스트 출력할떄 join을 많이 쓰는데 문자열 함수이기 떄문에 정수나 실수 등 다른 형태라면 문자열로 형변환을 해주어야 함

~~~
TypeError: sequence item 0: expected str instance, int found
~~~

## 14
시간복잡도에 대하여
~~~
https://hanamon.kr/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-time-complexity-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84/
~~~


## 15
시간복잡도 알고리즘 문제 이해가 안됨
~~~
https://www.acmicpc.net/problem/24267
~~~
