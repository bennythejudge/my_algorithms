import my_functions


if __name__ == "__main__":
  a = 10
  b = 2
  print "gcd {},{}: {}".format(a,b,my_functions.gcd(a,b))
  a = 101
  b = 201
  print "gcd {},{}: {}".format(a,b,my_functions.gcd(a,b))
  a = 1000
  b = 500
  print "gcd {},{}: {}".format(a,b,my_functions.gcd(a,b))
  a = 1024
  b = 2048
  print "gcd {},{}: {}".format(a,b,my_functions.gcd(a,b))
  # --------------------
  a = 10
  b = 2
  print "lcm {},{}: {}".format(a,b,my_functions.lcm(a,b))
  a = 101
  b = 201
  print "lcm {},{}: {}".format(a,b,my_functions.lcm(a,b))
  a = 1000
  b = 500
  print "lcm {},{}: {}".format(a,b,my_functions.lcm(a,b))
  a = 1024
  b = 2048
  print "lcm {},{}: {}".format(a,b,my_functions.lcm(a,b))
  a = 1025
  b = 2045
  print "lcm {},{}: {}".format(a,b,my_functions.lcm(a,b))
