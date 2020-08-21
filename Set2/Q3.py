import sys
import re
n0=sys.argv[1]
n1=sys.argv[2]
n2=sys.argv[3]
A=open(n0, 'r')
data=A.read().upper()
data1=re.findall(r"[\w]+",data)
print(data1)
WORD1=[]
WORD2=[]
LWORD1=len(n1)
LWORD2=len(n2)
def main(n0,n1,n2):
      num=0
      for word in data1:
            num+=1
            L=len(word)
            if word.startswith(n1.upper()):
                  if L==LWORD1:
                        WORD1.append(num)
                       
            if word.startswith(n2.upper()):
                  if L==LWORD2:
                        WORD2.append(num)
      for i in WORD1:
            data1[i-1]=n2.upper()
      for j in WORD2:
            data1[j-1]=n1.upper()
      return WORD1, WORD2                
print(main(n0,n1,n2))
print(data1)                       
f=open(n0,"w")
for k in data1:
      f.write(" " + k)
f.close()                          

