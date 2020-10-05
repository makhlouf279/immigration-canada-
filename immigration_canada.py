import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


df_can =pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

#print ('Data read into a pandas dataframe!')

print(df_can.head(5))
#size de dataframe
print(df_can.shape)
print("tous les colones de data base :\n" , df_can.columns)
#type de chaque colone 
print(df_can.info)
print(df_can['OdName'])
print(df_can.index.values)
print(type(df_can.columns))
print(type(df_can.index))
#to get the index and columns as list
df_can.columns.tolist()
df_can.index.tolist()
print (type(df_can.columns.tolist()))
print (type(df_can.index.tolist()))
#netoyage de dataframe 
df_can.drop([ 'AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
print(df_can.head(2))
#renommer les colonnes
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
print(df_can.columns)
#le nombre total d`immigrant entre 1980 jusqu`au 2013
df_can['Total'] = df_can.sum(axis=1)
print(df_can.columns)
print(df_can.isnull().sum())
#summary of each column in our dataframe
print(df_can.describe)
#filtering on the list of countries ('OdName') and the data for years: 1980 - 1985.
print(df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]])
df_can.set_index('Country', inplace=True)
print(df_can.head(3))
# nombre des immigrant de japan
print(df_can.loc['Japan'])

"""
alternate methods
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())

# alternate method
print(df_can.iloc[87, 36]) 
# year 2013 is the last column, with a positional index of 36
"""
# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])

#convert the column names into strings: '1980' to '2013'

df_can.columns = list(map(str, df_can.columns))

[print (type(x)) for x in df_can.columns.values]

#<-- uncomment to check type of column headers

#Since we converted the years to string, let's declare a variable
# that will allow us to easily call upon the full range of years

years = list(map(str, range(1980, 2014)))
print(years)
condition = df_can['Continent'] == 'Asia'
print(condition)
print(df_can[condition])

#un autre filltrage
print(df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')])


print('data dimensions:', df_can.shape)
print(df_can.columns)
print(df_can.head(2))

#visualisation
#line plot

haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
print(haiti.head())
haiti.index = haiti.index.map(int) 
haiti.plot(kind='line')
plt.title('Immigration from 1980-2013')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.text(2000, 6000, '2010 Earthquake')
plt.show()

#Get the data set for China and India, and display dataframe

df_CI=df_can.loc[['China','India'],years]
# il faut inverser la base 
df_CI=df_CI.transpose()
print(df_CI)
df_CI.index = df_CI.index.map(int)
df_CI.plot(kind='line')
plt.title('immigration from China and india')
plt.ylabel('number of immigrant')
plt.xlabel('years')
plt.show()

#Compare the trend of top 4 countries that contributed the most to immigration to Canada
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

df_C5= df_can.loc[['India', 'China', 'Philippines', 'Pakistan'], years]
df_C5=df_C5.transpose()
print(df_C5)
df_C5.index = df_C5.index.map(int) 
df_C5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size
plt.title('Immigration Trend of Top 4 Countries')
plt.ylabel('Number of Immigrants') 
plt.xlabel('Years')
plt.show()

print(df_can.head())

#suite














































 































