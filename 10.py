#sieve of erasthothenes
limit = 2000000
s = 0
primes = [True] * limit #initialise primes
primes[0] = primes[1] = False
for i, isprime in enumerate(primes):
  if isprime:
      s += i
      for n in range(i**2, limit, i):
          primes[n] = False
print(s)
