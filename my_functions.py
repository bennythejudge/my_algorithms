def gcd(a,b):
  """
  Find the GCD of 2 numbers
  """
  while b:
    a, b = b, a%b

  return a
