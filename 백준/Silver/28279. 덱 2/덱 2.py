from collections import deque
import sys

N = int(input())

is_queue = deque()


for _ in range(N):
	data = sys.stdin.readline().split()
	first_data = data[0]

	if first_data == "1":
		is_queue.appendleft(data[1])
	elif first_data == "2":
		is_queue.append(data[1])
	elif first_data == "3":
		if is_queue:
			print(is_queue.popleft())
		else:
			print("-1")
	elif first_data == "4":
		if is_queue:
			print(is_queue.pop())
		else:
			print("-1")
	elif first_data == "5":
		print(len(is_queue))
	elif first_data ==  "6":
		if is_queue:
			print("0")
		else:
			print("1")
	elif first_data == "7":
		if is_queue:
			print(is_queue[0])
		else:
			print("-1")
	else:
		if is_queue:
				print(is_queue[-1])
		else:
			print("-1")
