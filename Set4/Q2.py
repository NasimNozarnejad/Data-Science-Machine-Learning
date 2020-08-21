import numpy as np
import pandas as pd
import sys
filename=sys.argv[1]
df = pd.read_csv(filename)
Key=df.keys()
KEYS=Key.drop(Key[0])
INT_KEY=[]
for k in KEYS:
    if not isinstance(df[k][1], str):
        INT_KEY.append(k) 

y=np.zeros((14,14))
for i in range(14):
    for j in range(14):
        if np.std(df[INT_KEY[i]])==0 or np.std(df[INT_KEY[j]])==0:
            B=np.zeros((2,2))
        else:
            B = np.corrcoef(df[INT_KEY[i]],df[INT_KEY[j]])
        if i==j:
            y[i][j]=0
        else:
            y[i][j] = B[0,1]
        
y[np.isnan(y)]=0
print('correlation matrix is:\n' + str(y))
