
- Pandas functions
------------+------------------+-----------------+----------------------------------------------
Data Format |  Read            |  Save           |  Comments
------------+------------------+-----------------+----------------------------------------------
csv         |  pd.read_csv()   |  df.to_csv()    |  csv stands for comma separated values.
json        |  pd.read_json()  |  df.to_json()   |
Excel       |  pd.read_excel() |  df.to_excel()  |
sql         |  pd.read_sql()   |  df.to_sql()    |
------------+------------------+-----------------+---------------------------------------------

- Basic Insights of Dataset (Data types)
  Use dataframe.dtypes to check data types
  df.dtypes
-------------------------------+------------------------------------------+----------------------------------------
Pandas Type :                  | Native Python Type :                     | Description :                      
-------------------------------+------------------------------------------+----------------------------------------
   object                      |    string                                |   numbers and strings 
-------------------------------+------------------------------------------+----------------------------------------
   int64                       |    int                                   |   Numeric characters
-------------------------------+------------------------------------------+----------------------------------------
   float64                     |    float                                 |   Numeric characters with decimals 
-------------------------------+------------------------------------------+----------------------------------------
   datetime64, timedelta[ns]   |    N/A (but see the datatime module in   |   time data
                               |    Python's standard library)            |
-------------------------------+------------------------------------------+----------------------------------------


Various DataSet: 
    https://archive.ics.uci.edu/ml/index.php
    
Auto as an example:
    https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data
 
''' 
3,?,alfa-romero,gas,std,two,convertible,rwd,front,88.60,168.80,64.10,48.80,2548,dohc,four,130,mpfi,3.47,2.68,9.00,111,5000,21,27,13495
3,?,alfa-romero,gas,std,two,convertible,rwd,front,88.60,168.80,64.10,48.80,2548,dohc,four,130,mpfi,3.47,2.68,9.00,111,5000,21,27,16500
2,164,audi,gas,std,four,sedan,4wd,front,99.40,176.60,66.40,54.30,2824,ohc,five,136,mpfi,3.19,3.40,8.00,115,5500,18,22,17450
2,?,audi,gas,std,two,sedan,fwd,front,99.80,177.30,66.30,53.10,2507,ohc,five,136,mpfi,3.19,3.40,8.50,110,5500,19,25,15250
1,158,audi,gas,std,four,sedan,fwd,front,105.80,192.70,71.40,55.70,2844,ohc,five,136,mpfi,3.19,3.40,8.50,110,5500,19,25,17710
:::::::::::::::::::::::::::::::::::::::::::::::::::::
'''

import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

# import dataset without headers
df = pd.read_csv(url, header = None)

#Replace default header by df.columns = headers
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "enginie-location", "wheel-base", "length", "width", 'height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", 
           "peak-rpm", "city-mpg", "highway-mpg", "price"]
           
df.columns = headers

# df prints the entire dataframe (not recommended for large datasets)
# df.head(n) to show the first n rows of data frame
# df.tail(n) to show the bottom n rows of data frame

df.head(5)

# Saving modified dataset 

path = "C:\Windows\...\automobile.csv"
df.to_csv(path)

# Returns a statistical summary
df.describe()

# To enable a summary of all the columns, add include="all"
df.describe(include="all")

# Another method to check the dataset 
df.info()

# In the summary, 
# "Unique" is the number of distinct objects in the column, 
# "top" is the most frequently occurring object, 
# "freq" is the number of times the top object appears in the column.
# Some values in the table are shown here as "NaN", which stands for "not a number".
# This is because that particular statistical metric cannot be calculated for that specific
# column data type.








