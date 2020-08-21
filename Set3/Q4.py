import pandas as pd
import sys
n=int(sys.argv[1])
df=pd.read_csv('2014_world_gdp_with_codes')
DF=pd.read_csv('migrants')
DF['under18']= pd.to_numeric(DF['under18'],errors='coerce')
def main(n):
	A=pd.DataFrame({'country':df['COUNTRY'],'GDP':df['GDP (BILLIONS)']})
	B=pd.DataFrame({'country':DF['country'],'u18':DF['under18']})
	C=pd.merge(A,B,how='outer',on=['country'])
	pd.to_numeric(C['u18'])	
	C['GDP']=C['GDP'].fillna(-1)
	C['u18']=C['u18'].fillna(0)
	NEWC=C[C['GDP']>= n]
	Value=NEWC['u18'].mean()
	return Value
print(main(n))
