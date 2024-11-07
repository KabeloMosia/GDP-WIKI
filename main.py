import numpy as np
import pandas as pd

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
tables=pd.read_html(URL)
df=tables[3]
# Replace the column headers with column numbers
df.columns = range(df.shape[1])
# Retain columns name of country and value of GDP quoted by IMF)
df=df[[0,2]]
# Retain the Rows indicating the top 10 economies of the world.
df=df.iloc[1:11,:]
# Assign column names as "Country" and "GDP (Million USD)"
df.columns=['Country','GDP (Million USD)']
# Change the data type of the 'GDP (Million USD)' column to integer. 
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)
# Convert the GDP value in Million USD to Billion USD
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000
#Round the value to 2 decimal places.
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)
# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'})

# Load the DataFrame to the CSV file named "Largest_economies.csv"
df.to_csv('./Largest_economies.csv')
