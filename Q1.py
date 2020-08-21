import pandas as pd
import numpy as np
import sys
df=pd.read_csv('tesla-stock-price')
n=int(sys.argv[1])

def main(n):	
	A=df[['high','low']].mean(axis=1)
	B=np.matrix(A)
	NUM=len([1 for i in range(np.size(B)-1) if (B[0,i] <= n and B[0,i+1] > n) ])
	return NUM
	
print(main(n))	
