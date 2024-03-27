S1, S2, S3 = map(int, input().split())
sum_list = [0] * 100

for one in range(1, S1+1):
	for two in range(1, S2+1):
		for three in range(1, S3 + 1):
			sum_list[one+two+three] += 1
print(sum_list.index(max(sum_list)))