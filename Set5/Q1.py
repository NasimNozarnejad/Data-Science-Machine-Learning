import numpy as np

import pandas as pd

from scipy.stats import ttest_ind

df = pd.read_csv('countries_2.csv.txt')

a=[]; b=[]

A = ['internetusage','Imports','Exports','migrants','GDP','PPP','education']

for k in range(len(A)):

    a=[]; b=[]

    for i in range(len(df)):

        if df['Year'][i]==2005:

            a.append((df [A[k]])[i])

        if df['Year'][i]==2017:

            b.append((df [A[k]])[i])

    if (ttest_ind(a,b)[1])<0.05:

        print(A[k])
