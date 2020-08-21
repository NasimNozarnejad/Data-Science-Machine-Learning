import numpy as np

import pandas as pd

from scipy.stats import ttest_ind

df = pd.read_csv('countries_2.csv.txt')

A = ['internetusage','Imports','Exports','migrants','GDP','PPP','education']

output = []

output=df['country'].unique()

for k in range(len(A)):

    for i in range(len(output)):

        B=df[df['country']==output[i]]

        C=df[df['country']!=output[i]]      

        if (ttest_ind(B[A[k]],C[A[k]])[1]) < 0.05:

            print(output[i],A[k])
