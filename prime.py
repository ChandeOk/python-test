import math;

def get_primes(min, max):
  result = []
  for i in range(min, max):
    if is_prime(i):
      result.append(i) 
  return result

def is_prime(num):
  if num == 1:
    return False
  if num == 2 or num == 3:
    return True
  for i in range(2, math.isqrt(num) + 1):
    if num % i == 0:
      return False
  return True