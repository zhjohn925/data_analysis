import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

df = pd.read_csv('covid_19_data.csv')

df.drop(['SNo', 'Last Update'], axis=1, inplace=True)
df.rename(columns={'ObservationDate':'Date', 'Province/State':'State', 'Country/Region':'Country'}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'])

imputer = SimpleImputer(strategy='constant')
df2 = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# df3 = df2.groupby(['Country', 'Date'])[['Country', 'Date', 'Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
df3 = df2.groupby(['Country', 'Date'])[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

countries = df3['Country'].unique()
print(countries)

# different countries
# for idx in range(0,len(countries)): 
for idx in np.where(countries == 'Mainland China')[0] : 
    C = df3[df3['Country']==countries[idx]].reset_index()        
    plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
    plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
    plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
    plt.title(countries[idx])
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of cases')
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

