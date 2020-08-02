def gcd(a,b):
  """
  Find the GCD of 2 numbers
  """
  #print "starts here"
  while b:
    #print "inside loop 1 b: {} a: {}".format(b,a)
    a, b = b, a%b
    #print "inside loop 2 b: {} a: {}".format(b,a)

  return a


def lcm(a,b):
  """
  Find the LCM of 2 numbers
  """

  print "LCM starts here"
  return a // gcd(a,b) * b
