T = int(input())
for test_case in range(1, T + 1):
	money = int(input())
	moneys = [0]*8
	how = 50000
	for i in range(len(moneys)):    
		if money // how >= 1:
			moneys[i] += money//how
			money -= how * moneys[i]          
		if i % 2 == 0:
			how //= 5
		else:
			how //= 2
	print(f'#{test_case}')
	print(f'{" ".join(map(str, moneys))}')
		
        
         