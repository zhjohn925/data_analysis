import pandas as pd

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


