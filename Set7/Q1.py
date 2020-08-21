#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import scipy.stats
from sklearn import linear_model, preprocessing

dfCountries = pd.read_csv('./S07/notebooks/datasets/Data.csv')
dfCountries[dfCountries.isna().any(axis=1)]

dfCountries = pd.read_csv('./S07/notebooks/datasets/UN_Uncleaned.csv')
originData = dfCountries
data = dfCountries[~dfCountries.isna().any(axis=1)]


df = data.drop(['Unnamed: 0', 'country', 'Year'], axis=1, inplace = False)
def normalize_data(df):
   
    cols = df.loc[:, df.dtypes == object].columns
    for col in list(cols):
        df[col] = df[col].str.replace(',','')
       
    for col in df.columns:
        if col!='Unnamed: 0':
            # Create x, where x the 'scores' column's values as floats
            x = df[[col]].values.astype(float)

            # Create a minimum and maximum processor object
            min_max_scaler = preprocessing.MinMaxScaler()

            # Create an object to transform the data to fit minmax processor
            x_scaled = min_max_scaler.fit_transform(x)

            # Run the normalizer on the dataframe
            df[col] = x_scaled

    return df
   
data = normalize_data(df)

def fit_regression_model(df, yCol):

    reg = linear_model.LinearRegression()
    reg.fit(df.drop([yCol], axis=1, inplace=False) ,df[yCol])
   
    print(reg.score(df.drop([yCol], axis=1, inplace=False), df[yCol]))
    return reg

def predict_col_value(reg_model, other_col_values_array):

    return reg_model.predict(other_col_values_array)

def calculate_mean_mode_val(df, col_name):

    return (df.col_name.mean(), mode(df.col_name))

def replace_field(df, reowIndex, colName, value):

    df.loc[rowIndex].at[colName] = value


def find_rows_with_nan(df, threshHold):

    return df.dropna(thresh=threshHold)


# internetusage CPIG CPIF Imports Exports homicide migrants GDP PPP tourexp tvarrival education Manufacturing
reg_model_for_internetusage = fit_regression_model(df = data, yCol = data.internetusage.name)
reg_model_for_CPIG = fit_regression_model(df = data, yCol = data.CPIG.name)
reg_model_for_CPIF = fit_regression_model(df = data, yCol = data.CPIF.name)
reg_model_for_Imports = fit_regression_model(df = data, yCol = data.Imports.name)
reg_model_for_Exports = fit_regression_model(df = data, yCol = data.internetusage.name)
reg_model_for_homicide = fit_regression_model(df = data, yCol = data.homicide.name)
reg_model_for_migrants = fit_regression_model(df = data, yCol = data.migrants.name)
reg_model_for_GDP = fit_regression_model(df = data, yCol = data.GDP.name)
reg_model_for_PPP = fit_regression_model(df = data, yCol = data.PPP.name)
reg_model_for_tourexp = fit_regression_model(df = data, yCol = data.tourexp.name)
reg_model_for_tvarrival = fit_regression_model(df = data, yCol = data.tvarrival.name)
reg_model_for_education = fit_regression_model(df = data, yCol = data.education.name)
reg_model_for_Manufacturing = fit_regression_model(df = data, yCol = data.Manufacturing.name)



regModelList = ["", reg_model_for_internetusage, reg_model_for_CPIG, reg_model_for_CPIF, reg_model_for_Imports, reg_model_for_Exports, reg_model_for_homicide, reg_model_for_migrants, reg_model_for_GDP, reg_model_for_PPP, reg_model_for_tourexp, reg_model_for_tvarrival, reg_model_for_education, reg_model_for_Manufacturing]


originData = originData.drop(['country', 'Year'], axis=1, inplace = False)


dfNew = find_rows_with_nan(originData, 13)


dfNew = normalize_data(dfNew)


# internetusage CPIG CPIF Imports Exports homicide migrants GDP PPP tourexp tvarrival education Manufacturing
unnamedDataFrame = dfNew[~dfNew['Unnamed: 0'].isnull()]
internetUsageNaNDataFrame = dfNew[dfNew['internetusage'].isnull()]
CPIGNaNDataFrame = dfNew[dfNew['CPIG'].isnull()]
CPIFNaNDataFrame = dfNew[dfNew['CPIF'].isnull()]
ImportsNaNDataFrame = dfNew[dfNew['Imports'].isnull()]
ExportsNaNDataFrame = dfNew[dfNew['Exports'].isnull()]
homicideNaNDataFrame = dfNew[dfNew['homicide'].isnull()]
migrantsNaNDataFrame = dfNew[dfNew['migrants'].isnull()]
GDPNaNDataFrame = dfNew[dfNew['GDP'].isnull()]
PPPNaNDataFrame = dfNew[dfNew['PPP'].isnull()]
tourexpNaNDataFrame = dfNew[dfNew['tourexp'].isnull()]
tvarrivalNaNDataFrame = dfNew[dfNew['tvarrival'].isnull()]
educationNaNDataFrame = dfNew[dfNew['education'].isnull()]
ManufacturingNaNDataFrame = dfNew[dfNew['Manufacturing'].isnull()]

dfList = [unnamedDataFrame, internetUsageNaNDataFrame, CPIGNaNDataFrame, CPIFNaNDataFrame, ImportsNaNDataFrame, ExportsNaNDataFrame, homicideNaNDataFrame, migrantsNaNDataFrame, GDPNaNDataFrame, PPPNaNDataFrame, tourexpNaNDataFrame, tvarrivalNaNDataFrame, educationNaNDataFrame, ManufacturingNaNDataFrame]

measureList = ['Unnamed: 0', 'internetusage', 'CPIG', 'CPIF', 'Imports', 'Exports', 'homicide', 'migrants', 'GDP', 'PPP', 'tourexp', 'tvarrival', 'education', 'Manufacturing']

print(measureList[12],measureList[13])

nanColIndex = []
shouldCalculateList = []
for index, df in enumerate(dfList):
    if len(df) > 0 and index != 0:

        nanColIndex.append(index)
        rowsValues = []
        observedMeasuredForRow = measureList[:index]+measureList[index+1:]

        for _,row in dfList[index].iterrows():
            tempList = []
            for item in observedMeasuredForRow:
                tempList.append(row[item])

            rowsValues.append(tempList)
        shouldCalculateList.append(rowsValues)
    else:
        pass


eduValues = []

for item in shouldCalculateList[0]:
    eduValue = predict_col_value(reg_model_for_education, [item[1:]])
    row = dfNew[dfNew['Unnamed: 0']==item[0]]
    dfNew['education'] = eduValue[0]
    eduValues.append((item[0], eduValue[0]))



manValues = []

for item in shouldCalculateList[0]:
    manValue = predict_col_value(reg_model_for_Manufacturing, [item[1:]])
    row = dfNew['Unnamed: 0']==item[0]
    dfNew['Manufacturing'] = manValue[0]
    manValues.append((item[0], manValue[0]))

dfNew.to_csv('UN_Fill_Row_With_Just_One_Empty_Col.csv')
