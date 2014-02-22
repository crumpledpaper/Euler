def check_palindrome(n):
    return n == int(str(n)[::-1]) #reverse n

high = 0
for i in range(1000):
    for j in range(1000):
        if i*j > high and check_palindrome(i*j):
            high = i*j

print(high)
