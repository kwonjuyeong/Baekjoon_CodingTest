N = int(input())
arr_list = list(map(int, input().split()))
v = int(input())

# 정수 v가 리스트 integers 안에 몇 개 있는지 count 함수를 사용하여 구하기
count_v = arr_list.count(v)

print(count_v)