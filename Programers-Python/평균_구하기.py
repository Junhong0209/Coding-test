# 문제 설명
# 정수를 담고 있는 배열 arr의 평균값을 return 하는 함수, solution을 완성해보세요.

# 제한 사항
# arr은 길이 1 이상 100이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

# 입출력 예
# +---------------------+
# |     arr    | return |
# |---------------------|
# | [1,2,3,4,] |  2.5   |
# |   [5, 5]   |  5.0   |
# +---------------------+

def solution(arr):
    answer = 0

    for i in range(0, len(arr)):    # 0부터 arr 배열의 길이 값만큼 for 문을 돌린다.
        answer += arr[i]            # answer에 arr[i]의 값을 더해준다.

    total = answer / len(arr)       # 평균 값을 구해야 하니 total에 (answer / arr 배열의 길이 값)을 넣어준다.

    return total