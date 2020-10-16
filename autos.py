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

########################################          
# Data Wrangling.
########################################
          
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
          
#####################################          
# Deal with missing data
#####################################
# drop data (ie. Whole columns should be dropped only if most entries in the column are empty)
# a. drop the whole row
# b. drop the whole column
# replace data
# a. replace it by mean
# b. replace it by frequency
# c. replace it based on other functions
          
# We will apply each method to many different columns:
# Replace by mean:
#   "normalized-losses": 41 missing data, replace them with mean
#   "stroke": 4 missing data, replace them with mean
#   "bore": 4 missing data, replace them with mean
#   "horsepower": 2 missing data, replace them with mean
#   "peak-rpm": 2 missing data, replace them with mean
# Replace by frequency:
#   "num-of-doors": 2 missing data, replace them with "four".
#   Reason: 84% sedans is four doors. Since four doors is most frequent, it is most likely to occur
# Drop the whole row:
#   "price": 4 missing data, simply delete the whole row
#   Reason: price is what we want to predict. Any data entry without price data cannot be used for prediction; 
#           therefore any row now without price data is not useful to us
          
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
# four    114
# two      89
# Name: num-of-doors, dtype: int64          
          
#  use the ".idxmax()" method to calculate for us the most common type automatically:
df['num-of-doors'].value_counts().idxmax()
# 'four'
          
# The replacement procedure is very similar to what we have seen previously
#replace the missing 'num-of-doors' values by the most frequent 
df["num-of-doors"].replace(np.nan, "four", inplace=True)
          
# let's drop all rows that do not have price data:
# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

df.head()          
# Good! Now, we obtain the dataset with no missing values.
 
###################################################################################################          
# Correct data format
# Check and make sure that all data is in the correct format (int, float, text or other)          
################################################################################################### 
# Use  .dtype() to check the data type
#      .astype() to change the data type

df.dtypes
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
df.dtypes

##############################################################################          
# Data Standardization
############################################################################## 
          
# Data is usually collected from different agencies with different formats. 
# (Data Standardization is also a term for a particular type of data normalization, where 
#  we subtract the mean and divide by the standard deviation)

# What is Standardization?
# Standardization is the process of transforming data into a common format which allows 
# the researcher to make the meaningful comparison.
          
# Example: Transform mpg to L/100km:
# The formula for unit conversion is  "L/100km = 235 / mpg"
df.head()          
# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]
# check your transformed data 
df.head()
          
# transform mpg to L/100km in the column of "highway-mpg", and change the name of column to "highway-L/100km".
# transform mpg to L/100km by mathematical operation (235 divided by mpg)
df["highway-mpg"] = 235/df["highway-mpg"]
# rename column name from "highway-mpg" to "highway-L/100km"
df.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)
# check your transformed data 
df.head()

##############################################################################          
# Data Normalization
##############################################################################          

# Why normalization?
# Normalization is the process of transforming values of several variables 
# into a similar range. Typical normalizations include scaling the variable so 
# the variable average is 0, scaling the variable so the variance is 1, or scaling 
# variable so the variable values range from 0 to 1
# Example :
#   To demonstrate normalization, let's say we want to scale the columns "length", "width" and "height"
#   Target: would like to Normalize those variables so their value ranges from 0 to 1.
#   Approach: replace original value by (original value)/(maximum value) 
          
# replace (original value) by (original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max() 
# show the scaled columns
df[["length","width","height"]].head()

###############################################################
# Binning
###############################################################
# Why binning?
# Binning is a process of transforming continuous numerical variables into discrete categorical 'bins', 
# for grouped analysis.

# Example:
#    In our dataset, "horsepower" is a real valued variable ranging from 48 to 288, it has 57 unique values. 
#    What if we only care about the price difference between cars with high horsepower, medium horsepower, 
#    and little horsepower (3 types)? Can we rearrange them into three ‘bins' to simplify analysis?
# Use the Pandas method 'cut' to segment the 'horsepower' column into 3 bins

# Convert data to correct format
df["horsepower"]=df["horsepower"].astype(int, copy=True)

# Lets plot the histogram of horspower, to see what the distribution of horsepower looks like.
%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot
plt.pyplot.hist(df["horsepower"])

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

# linspace(start_value, end_value, numbers_generated)
# 3 bins of equal size bandwidth           
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins
          
# set group names:
group_names = ['Low', 'Medium', 'High']
          
# apply the function "cut" the determine what each value of "df['horsepower']" belongs to.
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df[['horsepower','horsepower-binned']].head(20)

# see the number of vehicles in each bin.
df["horsepower-binned"].value_counts()
# Low       153
# Medium     43
# High        5
# Name: horsepower-binned, dtype: int64   

# Lets plot the distribution of each bin
%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot
pyplot.bar(group_names, df["horsepower-binned"].value_counts())

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
          
# Check the dataframe above carefully, you will find the last column provides 
# the bins for "horsepower" with 3 categories ("Low","Medium" and "High").
# We successfully narrow the intervals from 57 to 3!
 
###############################################################
# Bins visualization
###############################################################          
# Normally, a histogram is used to visualize the distribution of bins we created above.
# shows the binning result for attribute "horsepower"
%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot

a = (0,1,2)

# draw historgram of attribute "horsepower" with bins = 3
plt.pyplot.hist(df["horsepower"], bins = 3)

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
 
          
###########################################################################          
# Indicator variable (or dummy variable)
###########################################################################

# An indicator variable (or dummy variable) is a numerical variable used to label categories. 
# They are called 'dummies' because the numbers themselves don't have inherent meaning.

# Why we use indicator variables?
# So we can use categorical variables for regression analysis in the later modules.

# Example:
# We see the column "fuel-type" has two unique values, "gas" or "diesel". Regression 
# doesn't understand words, only numbers. To use this attribute in regression analysis, we 
# convert "fuel-type" into indicator variables.

# Use the panda's method 'get_dummies' to assign numerical values to different 
# categories of fuel type.
          
df.columns
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.head()
          
# change column names for clarity
dummy_variable_1.rename(columns={'fuel-type-diesel':'gas', 'fuel-type-diesel':'diesel'}, inplace=True)
dummy_variable_1.head()

# We now have the value 0 to represent "gas" and 1 to represent "diesel" in the 
# column "fuel-type". We will now insert this column back into our original dataset.
          
# merge data frame "df" and "dummy_variable_1" 
df = pd.concat([df, dummy_variable_1], axis=1)
# drop original column "fuel-type" from "df"
df.drop("fuel-type", axis = 1, inplace=True)
df.head()

# The last two columns are now the indicator variable representation of the fuel-type 
# variable. It's all 0s and 1s now.
 
# create indicator variable to the column of "aspiration": "std" to 0, while "turbo" to 1.          
# get indicator variables of aspiration and assign it to data frame "dummy_variable_2"
dummy_variable_2 = pd.get_dummies(df['aspiration'])
# change column names for clarity
dummy_variable_2.rename(columns={'std':'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)
# show first 5 instances of data frame "dummy_variable_1"
dummy_variable_2.head()
          
# Merge the new dataframe to the original dataframe then drop the column 'aspiration' 
# merge the new dataframe to the original datafram
df = pd.concat([df, dummy_variable_2], axis=1)
# drop original column "aspiration" from "df"
df.drop('aspiration', axis = 1, inplace=True)
          
# Save the new csv
df.to_csv('clean_df.csv')
