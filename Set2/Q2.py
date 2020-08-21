import sys
import re
n0=sys.argv[1]
n1=sys.argv[2]
n2=sys.argv[3]
A=open(n0, 'r')
data=A.read().upper()
data1=re.findall(r"[\w]+",data)
list=[]
def main(n0,n1,n2):
      for word in data1:
            if word.startswith(n1.upper()):
                  if word.endswith(n2.upper()):
                        list.append(word)
      return list                  
                 
print(main(n0,n1,n2))
