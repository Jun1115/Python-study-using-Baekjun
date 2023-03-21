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
