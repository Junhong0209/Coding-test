"""
# 나누어 떨어지는 숫자 배열
* 문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

* 제한사항
arr은 자연수를 담은 배열입니다.
정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
divisor는 자연수입니다.
array는 길이 1 이상인 배열입니다.
"""

# 입출력 예
# +-----------------------------------------+
# | arr           | divisor | return        |
# |---------------|---------|---------------|
# | [5, 9, 7, 10] | 5       | [5, 10]       |
# | [2, 36, 1, 3] | 1       | [1, 2, 3, 36] |
# | [3,2,6]       | 10      | [-1]          |
# +-----------------------------------------+

def solution(arr, divisor):
    answer = []                  # 비어있는 answer 배열 생성

    for num in arr:              # arr 배열의 값을 num에 한번씩 넣어 for 문을 돌린다.
        if num % divisor == 0:   # num / divisor의 나머지가 0일 경우
            answer.append(num)   # answer에 num 값을 넣는다.

    if not answer:               # answer이 비어 있을 경우
        answer = [-1]            # answer 배열에 -1을 넣어준다.
    else:
        answer.sort()            # 위 if 문에 걸리지 않았다면, 배열 안의 값을 순서대로 정리 해준다.

    return answer