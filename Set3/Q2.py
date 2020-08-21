import pandas as pd
import sys
n=sys.argv[1]
def main(n):
	df=pd.read_csv('significant-earthquakes')
	Q=df.drop(['Year','Code'],axis=1)
	E=Q.groupby("Entity")
	F=E['Number of significant earthquakes (significant earthquakes)'].sum()
	NUM=F[n]
	return NUM
print(main(n))	
