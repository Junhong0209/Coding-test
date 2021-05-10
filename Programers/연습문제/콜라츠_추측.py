"""
# 콜라츠 추측

* 문제 설명
1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.

1-1. 입력된 수가 짝수라면 2로 나눕니다.
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
예를 들어, 입력된 수가 6이라면 6→3→10→5→16→8→4→2→1 이 되어 총 8번 만에 1이 됩니다. 위 작업을 몇 번이나 반복해야하는지 반환하는 함수, solution을 완성해 주세요. 단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.

* 제한 사항
입력된 수, num은 1 이상 8000000 미만인 정수입니다.
"""
# 입출력 예
# +---------------+
# |   n  | result |
# |------|--------|
# |   6  |   8    |
# |  16  |   4    |
# |626331|   -1   |
# +---------------+

def solution(num):
    cnt = 0

    while num > 1:                # num이 1보다 클 동안만 while을 반복한다.
        if num % 2 == 0:          # num을 2로 나누었을때 나머지가 0이라면
            num = num / 2         # num에 num 나누기 2의 값을 넣어준다.
        else:                     # num을 2로 나우었을때 나머지가 0이 아니라면
            num = (num * 3) + 1   # num에 (num * 3) + 1의 값을 넣어준다.
        cnt += 1                  # 위 반복문이 몇번 실행 되었는지 알아야 하므로 cnt라는 변수에 1씩 더 해준다.

        if cnt >= 500:            # 만약 cnt 변수의 값이 500이 넘어간다면
            return -1             # -1을 리턴해준다.

    return cnt                    # cnt 변수의 값을 리턴 해준다.
