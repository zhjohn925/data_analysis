import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

df = pd.read_csv('covid_19_data.csv')

df.drop(['SNo', 'Last Update'], axis=1, inplace=True)
df.rename(columns={'ObservationDate':'Date', 'Province/State':'State', 'Country/Region':'Country'}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'])

# It is used for imputing (replacing) missing or NaN (Not-a-Number) values in a dataset with 
# specified constant values (fill_value = 1.0 by default). 
# SimpleImputer(strategy='constant') is used to create a simple imputer with a constant imputation strategy.
imputer = SimpleImputer(strategy='constant')
# imputer.fit_transform() is used to both fit the imputer to a dataset and transform the dataset 
# by replacing missing values with imputed values.
# - The imputer learns statistical information from the dataset that it will later use to impute missing values. 
#   For example, if you're using the mean imputation strategy, the imputer calculates the mean of 
#   each feature (column) using the non-missing values in that feature.
# - Replace the missing values in the dataset with the imputed values based on the strategy you've specified. 
df2 = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# df3 = df2.groupby(['Country', 'Date'])[['Country', 'Date', 'Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
df3 = df2.groupby(['Country', 'Date'])[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

countries = df3['Country'].unique()
print(countries)

C = df3[df3['Country']=='Mainland China']
type(C)   # <class 'pandas.core.frame.DataFrame'>

#              Country       Date Confirmed Deaths Recovered
# 1488  Mainland China 2020-01-22       547     17        28
# 1489  Mainland China 2020-01-23       639     18        30
# 1490  Mainland China 2020-01-24       916     26        36
# ::::::

C.reset_index()
#     index         Country       Date Confirmed Deaths Recovered
# 0    1488  Mainland China 2020-01-22       547     17        28
# 1    1489  Mainland China 2020-01-23       639     18        30
# 2    1490  Mainland China 2020-01-24       916     26        36

# different countries
# for idx in range(0,len(countries)): 
for idx in np.where(countries == 'Mainland China')[0] : 
    C = df3[df3['Country']==countries[idx]].reset_index()
    # plt.scatter() is used to create scatter plots, which are a type of 
    # plot commonly used to display individual data points on a two-dimensional graph.
    # A scatter plot is useful for visualizing the relationship between two variables.        
    plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
    plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
    plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
    plt.title(countries[idx])
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of cases')
    # Add a legend to a Matplotlib plot. A legend is a key that explains 
    # the meaning of the various elements (e.g., lines, markers, or colors) 
    # on the plot, making it easier for viewers to interpret the data.
    plt.legend()
    plt.show()    

# the world
df4 = df3.groupby(['Date'])[['Confirmed','Deaths','Recovered']].sum().reset_index()
C = df4
plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
plt.title('World')
plt.xlabel('Days since the first suspect')
plt.ylabel('Number of cases')
plt.legend()
plt.show()

