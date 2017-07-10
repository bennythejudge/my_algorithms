# recursive
def mcd(a,b):
  """ Trova il MCD tra due numeri """
  if a*b == 0: return 1
  if a==b:
    return a
  elif a>b:
    return mcd(a-b, b)
  else:
    return mcd(b-a, a)


if __name__ == "__main__":
  for i in xrange(0,1000000):
    n1 = random.randint(n1, n2)
    n2 = random.randint(n1, n2)
    print "1,4: {}".format(mcd(1,4))
    print "10,4: {}".format(mcd(10,4))
    print "10,6: {}".format(mcd(10,6))
    print "11,6: {}".format(mcd(11,6))
    print "1001,110: {}".format(mcd(1001,110))
    print "1021,1024: {}".format(mcd(1021,1024))
    print "1022,1024: {}".format(mcd(1022,1024))
    print "1048,1024: {}".format(mcd(1048,1024))
