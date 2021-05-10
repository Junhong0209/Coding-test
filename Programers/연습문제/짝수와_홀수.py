"""
# 짝수와 홀수
* 문제 설명
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

* 제한 조건
num은 int 범위의 정수입니다.
0은 짝수입니다.
"""

# 입출력 예
# +--------------+
# | num | return |
# |-----|--------|
# |  3  | "Odd"  |
# |  4  | "Even" |
# +--------------+

def solution(num):

    if num % 2 == 0:   # num을 2로 나누었을 때 나머지가 0이라면
        return "Even"  # "Even"을 리턴
    return "Odd"       # 위의 if 문에 걸리지 않았다면 "Odd"을 리턴
