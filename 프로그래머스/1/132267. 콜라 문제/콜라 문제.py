def solution(a, b, n):
    answer = 0
    bottles = n # 남은 콜라 병 수
    while bottles >= a:
        new_cola = bottles // a * b
        answer += new_cola
        bottles = bottles % a + new_cola
    return answer

# 1. 콜라 빈병 2개를 주면 콜라 1병 준다.
# 2. 빈병 20개를 주면 몇 병의 콜라?
# 3. 조건 = 보유 중인 빈 병이 2개 미만이면, 콜라를 받을 수 없음
# 4. 빈병 a개를 가져다줄 때 콜라 b병을 주는 마트에 빈 병 n개를 가져가면 콜라가 몇병일까?

#1. 원래 빈 병 n개
#2. 받은 콜라 병 수 n // a개    남은 콜라 병 수 = n - (n % a) + n // a개
