# every 3rd fibonacci number is even
s = 0
odd = 1
even = 2

while even < 4000000:
    s += even
    odd, even = odd + even * 2, even * 3 + odd * 2 # skip 2 terms ahead

print(s)
