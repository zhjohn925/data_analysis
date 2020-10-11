import pandas as pd

#####################################################################
# On Mac, to workaround the error: ssl.SSLCertVerificationError
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# Not sure if we need this:
# pip3 install --upgrade certifi
#####################################################################

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)

print("The first 5 rows of the dataframe") 
df.head(5)

print("The last 10 rows of the dataframe") 
df.tail(10)

# Add headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.columns = headers
df.head(10)

# Drop missing values along the column "price"
df.dropna(subset=["price"], axis=0)

# Find the name of the columns of the dataframe
df.columns

# Save Dataset
df.to_csv(automobile.csv", index=False)

# Data types
df.dtypes

# provide various summary statistics, excluding NaN (Not a Number) values.
# This shows the statistical summary of all numeric-typed (int, float) columns.
df.describe()

# Check all the columns including those that are of type object.
# Some values in the table above show as "NaN", this is because those numbers 
# are not available regarding a particular column type
df.describe(include="all")

# Selected columns
# dataframe[[' column 1 ',column 2', 'column 3'] ].describe()
df[['length', 'compression-ratio']].describe()

# provide a concise summary of your DataFrame.
df.info

import numpy as np

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)

# use Python's built-in functions to identify these missing values. 
missing_data = df.isnull()
missing_data.head(5)

# Based on the summary above, each column has 205 rows of data, seven columns containing missing data:
# "normalized-losses": 41 missing data
# "num-of-doors": 2 missing data
# "bore": 4 missing data
# "stroke" : 4 missing data
# "horsepower": 2 missing data
# "peak-rpm": 2 missing data
# "price": 4 missing data          
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("") 

# Calculate the average of the column          
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)   

# Replace "NaN" by mean value in "normalized-losses" column
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)
          
# Calculate the mean value for 'bore' column
avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)
          
# Replace NaN by mean value
df["bore"].replace(np.nan, avg_bore, inplace=True)

# calculate the mean vaule for "stroke" column
avg_stroke = df["stroke"].astype("float").mean(axis = 0)
print("Average of stroke:", avg_stroke)

# replace NaN by mean value in "stroke" column
df["stroke"].replace(np.nan, avg_stroke, inplace = True)
          
# Calculate the mean value for the 'horsepower' column:
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)
          
# Replace "NaN" by mean value:
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)
          
# Calculate the mean value for 'peak-rpm' column:
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
          
# Replace NaN by mean value:
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)     
          
# To see which values are present in a particular column, we can use the ".value_counts()" method:
df['num-of-doors'].value_counts()        
          
#  use the ".idxmax()" method to calculate for us the most common type automatically:
df['num-of-doors'].value_counts().idxmax()
          
# The replacement procedure is very similar to what we have seen previously
#replace the missing 'num-of-doors' values by the most frequent 
df["num-of-doors"].replace(np.nan, "four", inplace=True)
          
# let's drop all rows that do not have price data:
# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

df.head()          
          
