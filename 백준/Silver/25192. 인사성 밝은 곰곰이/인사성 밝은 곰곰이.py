import sys

N = int(sys.stdin.readline())
gom_set = set()
gom_cnt = 0

sys.stdin.readline()

for i in range(N - 1):
    chat = sys.stdin.readline().strip()
    if chat == "ENTER":
        gom_cnt += len(gom_set)
        gom_set.clear()
    else:
        gom_set.add(chat)
gom_cnt += len(gom_set)

print(gom_cnt)