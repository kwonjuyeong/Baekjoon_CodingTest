T = int(input())

for _ in range(T):
    change = int(input())
    
    Quarter = Dime = Nickel = Penny = 0
    Quarter = change // 25
    change = change % 25
    Dime = change // 10
    change = change % 10
    Nickel = change // 5
    change = change % 5
    Penny = change
    
    print(Quarter, Dime, Nickel, Penny)
        
        
        
        