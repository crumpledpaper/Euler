#sieve of erasthothenes
limit = 110000
count = 0
primes = [True] * limit #initialise primes
primes[0] = primes[1] = False
for i, isprime in enumerate(primes):
  if isprime:
    count += 1
    if count == 10001:
      print(i)
    for n in range(i**2, limit, i):
      primes[n] = False


