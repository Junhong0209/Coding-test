"""
# 문자열 다루기 기본
* 문제 설명
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

* 제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
"""
# 입출력 예
# +-----------------+
# |   s    | return |
# |--------|--------|
# | "a234" |  false |
# | "1234" |  true  |
# +-----------------+

def solution(s):
    if len(s) != 4 and len(s) != 6:   # 만약 맞다면 이 if 문은 건너뛴다.
        return False                  # 만약 문자열 s의 길이가 4 또는 6이 아니라면, False를 return한다.

    if s.isdigit():                   # 만약 숫자로만 구성되어 있지 않다면 이 if 문은 건너뛴다.
        return True                   # 만약 s라는 문자열이 숫자로만 이루어져 있다면, True를 return한다.

    return False                      # 위 if 문을 한번도 걸리지 않았다면 문자열의 길이가 4이거나 6이지만, 숫자로만 구성되어 있지않기 때문에 False를 return한다.