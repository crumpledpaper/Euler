def gcd(x,y): #Euclid's algorithm
    while y != 0:
        x,y = y, x%y
    return x

ans = 1
for i in range(1,21):
    ans *= i/gcd(i,ans)
print(ans)
