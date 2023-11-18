
T = int(input())
for test_case in range(1, T + 1):
	n = int(input())
	speed = 0
	move = 0
	for i in range(n):
		command = list(map(int, input().split()))
		if command[0] == 0:	#유지
			move += speed
		elif command[0] == 1: #가속
			speed += command[1]
			move += speed
		else:	#감속
			if speed < command[1]:
				speed = 0
			else:
  				speed -= command[1]
			move += speed
            

	print(f'#{test_case} {move}')
