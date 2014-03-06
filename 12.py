def count_factors(n):
    sqrt = n ** 0.5
    count = 0
    if sqrt % 1 == 0:
        count -= 1
    for i in range(1, int(sqrt) + 1):
        if n%i == 0:
            count += 2
    return count

def is_triangle(n):
    n *= 2
    sqrt = int(n**0.5)
    return n / sqrt == sqrt + 1

#500 = 5 * 5 * 5 * 2 * 2
n = 2**4 * 3**4 * 5**4 * 7 * 11 #smallest number with 500 divisors

while not is_triangle(n): #find next triangle number
    n += 1

nth = int((n*2)**0.5) #get nth triangle number

while count_factors(n) < 500: #check subsequent triangle numbers
    nth += 1
    n += nth

print(n)
