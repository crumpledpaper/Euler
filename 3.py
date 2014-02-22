n = 600851475143
sqrtn = n ** 0.5
divisor = 2

while divisor < sqrtn: # limit divisor as all other factors will be found by then
    while n % divisor == 0: # divsor divides n
        copy = n # get answer before dividing n until 1
        n /= divisor
    divisor += 1

print(copy)
