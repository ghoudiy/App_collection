is_prime = [True] * (10 ** 7 + 5)
primes = []
def seive(n):
  is_prime[0] = False
  is_prime[1] = False
  for i in range(2, n):
    j = i * i
    if is_prime[i]:
      primes.append(i)
      while j < n:
        is_prime[j] = False
        j += i