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


#Pie Chart

df_can1 =pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
print(df_can1.head())

# clean up the dataset to remove unnecessary columns (eg. REG) 
df_can1.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)

# let's rename the columns so that they make sense
df_can1.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)

# for sake of consistency, let's also make all column labels of type string
df_can1.columns = list(map(str, df_can1.columns))

# set the country name as index - useful for quickly looking up countries using .loc method
df_can1.set_index('Country', inplace=True)

# add total column
df_can1['Total'] = df_can1.sum(axis=1)

# years that we will be using in this lesson - useful for plotting later on
years = list(map(str, range(1980, 2014)))
print('data dimensions:', df_can1.shape)

mpl.style.use('ggplot') # optional: for ggplot-like style

# check for latest version of Matplotlib
print('Matplotlib version: ', mpl.__version__) # >= 2.0.0

# group countries by continents and apply sum() function 
df_continents = df_can1.groupby('Continent', axis=0).sum()

# note: the output of the groupby method is a `groupby' object. 
# we can not use it further until we apply a function (eg .sum())
print(type(df_can1.groupby('Continent', axis=0)))

print(df_continents.head())

# autopct create %, start angle represent starting point
"""
df_continents['Total'].plot(kind='pie',
                            figsize=(5, 6),
                            autopct='%1.1f%%', # add in percentages
                            startangle=90,     # start angle 90° (Africa)
                            shadow=True,       # add shadow      
                            )

plt.title('Immigration to Canada by Continent [1980 - 2013]')
plt.axis('equal') # Sets the pie chart to look like a circle.

plt.show()
"""
colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1] # ratio for each continent with which to offset each wedge.

df_continents['Total'].plot(kind='pie',
                            figsize=(15, 6),
                            autopct='%1.1f%%', 
                            startangle=90,    
                            shadow=True,       
                            labels=None,         # turn off labels on pie chart
                            pctdistance=1.2,    # the ratio between the center of each pie slice and the start of the text generated by autopct 
                            colors=colors_list,  # add custom colors
                            explode=explode_list # 'explode' lowest 3 continents
                            )

# scale the title up by 12% to match pctdistance
plt.title('Immigration to Canada by Continent [1980 - 2013]', y=1.12) 

plt.axis('equal') 

# add legend
plt.legend(labels=df_continents.index, loc='upper left') 

plt.show()


# boxing plot

# to get a dataframe, place extra square brackets around 'Japan'.
df_japan = df_can1.loc[['Japan'], years].transpose()
print(df_japan.head())


df_japan.plot(kind='box', figsize=(8, 6))
#Plot by passing in kind='box'.
plt.title('Box plot of Japanese Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')

plt.show()

print(df_japan.describe())

#Compare the distribution of the number of new immigrants from India and China for the period 1980 - 2013.
#Get the dataset for China and India and call the dataframe df_CI1

df_CI1= df_can1.loc[['China', 'India'], years].transpose()
print(df_CI1.head())
#Let's view the percentages associated with both countries using the describe() method

print(df_CI1.describe())

# DATA PLOT
df_CI1.plot(kind='box', figsize=(10, 7))
plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
plt.xlabel('Number of Immigrants')
plt.show()

# horizontal box plots
df_CI1.plot(kind='box', figsize=(10, 7), color='blue', vert=False)
plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
plt.xlabel('Number of Immigrants')
plt.show()


#Subplots

fig = plt.figure() # create figure

ax0 = fig.add_subplot(1, 2, 1) # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(1, 2, 2) # add subplot 2 (1 row, 2 columns, second plot). See tip below**

# Subplot 1: Box plot
df_CI1.plot(kind='box', color='blue', vert=False, figsize=(20, 6), ax=ax0) # add to subplot 1
ax0.set_title('Box Plots of Immigrants from China and India (1980 - 2013)')
ax0.set_xlabel('Number of Immigrants')
ax0.set_ylabel('Countries')

# Subplot 2: Line plot
df_CI1.plot(kind='line', figsize=(20, 6), ax=ax1) # add to subplot 2
ax1.set_title ('Line Plots of Immigrants from China and India (1980 - 2013)')
ax1.set_ylabel('Number of Immigrants')
ax1.set_xlabel('Years')

plt.show()

#Create a box plot to visualize the distribution of the top 15 countries (based on total immigration) grouped by the decades 1980s, 1990s, and 2000s.
#Step 1: Get the dataset. Get the top 15 countries based on Total immigrant population. Name the dataframe df_top15.

df_top15 = df_can1.sort_values(['Total'], ascending=False, axis=0).head(15)
print(df_top15)

"""
Step 2: Create a new dataframe which contains the aggregate for each decade. One way to do that:

Create a list of all years in decades 80's, 90's, and 00's.
Slice the original dataframe df_can to create a series for each decade and sum across all years for each country.
Merge the three series into a new data frame. Call your dataframe new_df.
"""
 # create a list of all years in decades 80's, 90's, and 00's
years_80s = list(map(str, range(1980, 1990))) 
years_90s = list(map(str, range(1990, 2000))) 
years_00s = list(map(str, range(2000, 2010))) 

 # slice the original dataframe df_can to create a series for each decade
df_80s = df_top15.loc[:, years_80s].sum(axis=1) 
df_90s = df_top15.loc[:, years_90s].sum(axis=1) 
df_00s = df_top15.loc[:, years_00s].sum(axis=1)



 # merge the three series into a new data frame
new_df = pd.DataFrame({'1980s': df_80s, '1990s': df_90s, '2000s':df_00s}) 


# display dataframe
print(new_df.head())

#methode describe
print(new_df.describe())


#Step 3: Plot the box plots.

new_df.plot(kind='box', figsize=(10, 6))
plt.title('Immigration from top 15 countries for decades 80s, 90s and 2000s')
plt.show()


# let's check how many entries fall above the outlier threshold 
new_df[new_df['2000s']> 209611.5]


#Scatter Plots
"""
Using a scatter plot, let's visualize the trend of total immigrantion to Canada (all countries combined) for the years 1980 - 2013.

Step 1: Get the dataset. Since we are expecting to use the relationship betewen years and total population, we will convert years to int type.
"""
# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can1[years].sum(axis=0))

# change the years to type int (useful for regression later on)
df_tot.index = map(int, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace = True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
print(df_tot.head())

"""
Step 2: Plot the data. In Matplotlib, we can create a scatter plot set by passing in kind='scatter' as plot argument.
 We will also need to pass in x and y keywords to specify the columns that go on the x- and the y-axis.
"""

df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

print(plt.show())

"""
Step 1: Get the equation of line of best fit. We will use Numpy's polyfit() method by passing in the following:

x: x-coordinates of the data.
y: y-coordinates of the data.
deg: Degree of fitting polynomial. 1 = linear, 2 = quadratic, and so on.
"""


x = df_tot['year']      # year on x-axis
y = df_tot['total']     # total on y-axis
fit = np.polyfit(x, y, deg=1)

fit
#Step 2: Plot the regression line on the scatter plot.

df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

# plot line of best fit
plt.plot(x, fit[0] * x + fit[1], color='red') # recall that x is the Years
plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))

plt.show()

# print out the line of best fit
'No. Immigrants = {0:.0f} * Year + {1:.0f}'.format(fit[0], fit[1]) 

"""
Create a scatter plot of the total immigration from Denmark, Norway, and Sweden to Canada from 1980 to 2013?

Step 1: Get the data:

Create a dataframe the consists of the numbers associated with Denmark, Norway, and Sweden only. Name it df_countries.
Sum the immigration numbers across all three countries for each year and turn the result into a dataframe. Name this new dataframe df_total.
Reset the index in place.
Rename the columns to year and total.
Display the resulting dataframe.
"""
 # create df_countries dataframe
df_countries = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()

 # create df_total by summing across three countries for each year
df_total = pd.DataFrame(df_countries.sum(axis=1))

 # reset index in place
df_total.reset_index(inplace=True)
 # rename columns
df_total.columns = ['year', 'total']

 # change column year from string to int to create scatter plot
df_total['year'] = df_total['year'].astype(int)

 # show resulting dataframe
print(df_total.head())


#Step 2: Generate the scatter plot by plotting the total versus year in df_total.


 # generate scatter plot
df_total.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')
 # add title and label to axes
plt.title('Immigration from Denmark, Norway, and Sweden to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
 # show plot
plt.show()


#Bubble Plots

"""
Let's start by analyzing the effect of Argentina's
 great depression.

Argentina suffered a great depression from 1998 - 2002, 
which caused widespread unemployment,
riots, the fall of the government, and a default on the
 country's foreign debt. In terms of income, over 50% of
 Argentines were poor, and seven out of ten Argentine 
 children were poor at the depth of the crisis in 2002.

Let's analyze the effect of this crisis, and compare
 Argentina's immigration to that of it's neighbour 
 Brazil. Let's do that using a bubble plot of
 immigration from Brazil and Argentina for the 
 years 1980 - 2013. We will set the weights for
 the bubble as the normalized value of the population 
 for each year.

Step 1: Get the data for Brazil and Argentina.
 Like in the previous example, we will convert 
 the Years to type int and bring it in the dataframe.
"""
df_can_t = df_can1[years].transpose() # transposed dataframe

# cast the Years (the index) to type int
df_can_t.index = map(int, df_can_t.index)

# let's label the index. This will automatically be the column name when we reset the index
df_can_t.index.name = 'Year'

# reset index to bring the Year in as a column
df_can_t.reset_index(inplace=True)

# view the changes
print(df_can_t.head())

#Step 2: Create the normalized weights.
# normalize Brazil data
norm_brazil = (df_can_t['Brazil'] - df_can_t['Brazil'].min()) / (df_can_t['Brazil'].max() - df_can_t['Brazil'].min())

# normalize Argentina data
norm_argentina = (df_can_t['Argentina'] - df_can_t['Argentina'].min()) / (df_can_t['Argentina'].max() - df_can_t['Argentina'].min())


#Step 3: Plot the data.

# Brazil
ax0 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Brazil',
                    figsize=(14, 8),
                    alpha=0.5,                  # transparency
                    color='green',
                    s=norm_brazil * 2000 + 10,  # pass in weights 
                    xlim=(1975, 2015)
                   )

# Argentina
ax1 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Argentina',
                    alpha=0.5,
                    color="blue",
                    s=norm_argentina * 2000 + 10,
                    ax = ax0
                   )

ax0.set_ylabel('Number of Immigrants')
ax0.set_title('Immigration from Brazil and Argentina from 1980 - 2013')
ax0.legend(['Brazil', 'Argentina'], loc='upper left', fontsize='x-large')


"""
Previously in this lab, we created box plots to
 compare immigration from China and India to Canada.
 Create bubble plots of immigration from China and India
 to visualize any differences with time from 1980 to 2013. 
 You can use df_can_t that we defined and used in the previous example.

Step 1: Normalize the data pertaining to China and India.
"""

# normalize China data
norm_china = (df_can_t['China'] - df_can_t['China'].min()) / (df_can_t['China'].max() - df_can_t['China'].min())

# normalize India data
norm_india = (df_can_t['India'] - df_can_t['India'].min()) / (df_can_t['India'].max() - df_can_t['India'].min())

#Step 2: Generate the bubble plots.
 # China
ax0 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='China',
                    figsize=(14, 8),
                    alpha=0.5,                  # transparency
                    color='green',
                    s=norm_china * 2000 + 10,  # pass in weights 
                    xlim=(1975, 2015)
                   )



 # India
ax1 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='India',
                    alpha=0.5,
                    color="blue",
                    s=norm_india * 2000 + 10,
                    ax = ax0
                   )


ax0.set_ylabel('Number of Immigrants')
ax0.set_title('Immigration from China and India from 1980 - 2013')
ax0.legend(['China', 'India'], loc='upper left', fontsize='x-large')


#---------------
#------------

 































