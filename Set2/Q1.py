import sys
n=int(sys.argv[1])
def main(n):
      if n > 1:
            for i in range(2, n-1):
                  if (n % i) == 0:
                        A= str(n)+ ' ' +"is not a prime number"
                        break
            else:
                  A = str(n)+ ' ' +"is a prime number"
      else:
            A= str(n)+ ' ' +"is not a prime number"
      return A                           
print(main(n))
