"""
자연수 뒤집어 배열로 만들기
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
"""

# 입출력 예
# +---------------------+
# | n     | return      |
# |-------|-------------|
# | 12345 | [5,4,3,2,1] |
# +---------------------+

def solution(n):
    arr = list(str(n))          # arr 변수에 n을 string으로 바꾸어 list 자료형으로 넣는다.
    arr.reverse()               # reverse 함수를 사용하여 arr 변수에 있는 것을 뒤집는다.

    return list(map(int, arr))  # map 함수를 사용하여 문자열 형태로 들어 있는 arr 배열 안에 있는 값을 int 형으로 바꾸어서 return한다.