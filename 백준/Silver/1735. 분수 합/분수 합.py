f_a, f_b = map(int, input().split())
l_a, l_b = map(int, input().split())

lcm = f_b * l_b
new_a = f_a * (lcm // f_b) + l_a * (lcm // l_b)
new_b = lcm

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd = find_gcd(new_a, new_b)

new_a //= gcd
new_b //= gcd

print(new_a, new_b)