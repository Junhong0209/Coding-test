"""
# 핸드폰 번호 가리기

* 문제 설명
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

* 제한 조건
s는 길이 4 이상, 20이하인 문자열입니다.
"""

# 입출력 예
# +-------------------------------+
# | phone_number  |    return     |
# |---------------|---------------|
# | "01033334444" | "*******4444" |
# |  "027778888"  |  "*****8888"  |
# +-------------------------------+

def solution(phone_number):
   phone_number_len = len(phone_number)      # phone_number_len이라는 변수에 phone_number의 길이를 넣어준다.
   phone_number_list = list(phone_number)    # phone_number_list라는 변수에 phone_number를 리스트로 변환하여 넣는다.

   for i in range(0, phone_number_len - 4):  # 전화번호 뒷 네자리는 남겨둬야 하므로 0부터 phone_number의 길이에서 4를 뺀것 만큼 for문을 돌려준다.
      phone_number_list[i] = '*'             # for문을 돌면서 phone_number_list의 0번째 위치부터 숫자를 *로 바꾸어준다.

   answer = ('').join(phone_number_list)     # phone_number_list에 는 숫자가 *로 바뀌어진 list가 있으므로 join함수를 사용하여 list를 공백 없이 하나의 문자열로 합쳐준다.

   return answer
