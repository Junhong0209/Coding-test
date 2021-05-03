# 문제 설명
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

# 제한사항
# 문자열 s의 길이: 50 이하의 자연수
# 문자열 s는 알파벳으로만 이루어져 있습니다.

# 입출력 예
# +--------------------+
# |    s    |  answer  |
# |"pPoooyY"|   true   |
# |  "Pyy"  |   false  |
# +--------------------+

def solution(s):
    s = s.lower()                # lower함수를 사용하여 문자열에 있는 대문자를 모두 소문자로 바꾸어 준다.
    substring1 = 'p'
    substring2 = 'y'

    cnt_p = s.count(substring1)  # 위에서 substring1 변수에 'p'를 넣었는데, s라는 변수에서 substring1 변수에 있는 것을 찾아 개수를 반환한다.
    cnt_y = s.count(substring2)  # 위에서 substring2 변수에 'y'를 넣었는데, s라는 변수에서 substring2 변수에 있는 것을 찾아 개수를 반환한다.

    return (cnt_p == cnt_y)      # cnt_p == cnt_y일 경우 True를 반환하고, cnt_p == cnt_y가 아닐 경우 False를 반환한다.