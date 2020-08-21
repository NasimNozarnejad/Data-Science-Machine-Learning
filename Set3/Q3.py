import pandas as pd
import sys
n=sys.argv[1:]
df=pd.read_csv('su5m')
def main(n):
	Ratio=df['f2017']/df['m2017']
	A=pd.DataFrame({'country':df['country'],'ratio':Ratio})
	B=A.groupby('country')
	C=B['ratio'].sum()
	MEAN=C[n].mean()
	return MEAN
print(main(n))	
