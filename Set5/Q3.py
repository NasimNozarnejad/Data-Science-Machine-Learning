import numpy as np

import pandas as pd

from scipy.stats import ttest_ind

df = pd.read_csv('Credit.csv.txt')

output = [' Male','Yes','Yes']

B = ['Gender','Student','Married']

A = ['Income','Limit','Rating','Cards','Age','Education','Balance']

 

for l in range(len(B)):

    value=df[df[B[l]]==output[l]]

    anti_value=df[df[B[l]]!=output[l]]

    for k in range(len(A)):

        if (ttest_ind(value[A[k]],anti_value[A[k]])[1])<0.05:

            print(B[l],A[k])
