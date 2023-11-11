# %% Import excel to dataframe
import pandas as pd
# import excel to dataframe
df = pd.read_excel("Online Retail.xlsx")


# %%  Show the first 10 row
# show the first 10 rows

import pandas as pd
df = pd.read_excel("Online Retail.xlsx")
df.head(10)


# %% Generate descriptive statistics regardless the datatypes
import pandas as pd
df = pd.read_excel("Online Retail.xlsx")
df.describe()



# %% Remove all the rows with null value and generate stats again
import pandas as pd
df = pd.read_excel("Online Retail.xlsx")
new_df = df.dropna()
new_df


# %% Remove rows with invalid Quantity (Quantity being less than 0)
import pandas as pd
df = pd.read_excel("Online Retail.xlsx")
df['CustomerID'] = pd.to_numeric(df['CustomerID'])
df = df[(df['Quantity']>0)]
df


# %% Remove rows with invalid UnitPrice (UnitPrice being less than 0)
import pandas as pd
df = pd.read_excel("Online Retail.xlsx")
df['CustomerID'] = pd.to_numeric(df['CustomerID'])
df = df[(df['UnitPrice']>3)]
df


# %% Only Retain rows with 5-digit StockCode
import pandas as pd
df = pd.read_excel("Online Retail.xlsx")
df["StockCode"] = df["StockCode"].astype("string")
mask = (df['StockCode'].str.len() == 5)
data =df.loc[mask]
print(data)
        


# %% strip all description
import pandas as pd;
df = pd.read_excel('Online Retail.xlsx')
df['InvoiceNo'] = df['InvoiceNo'].astype("string").str.strip()
df['StockCode'] = df['StockCode'].astype("string").str.strip()
df['Description'].str.strip()
df['Quantity'] = df['Quantity'].astype("string").str.strip()
df['InvoiceDate'] = df['InvoiceDate'].astype("string").str.strip()
df['UnitPrice'] = df['UnitPrice'].astype("string").str.strip()
df['CustomerID'] = df['CustomerID'].astype("string").str.strip()
df['Country'].str.strip()
print(df)



# %% Generate stats again and check the number of rows
import pandas as pd;
df = pd.read_excel('Online Retail.xlsx')
num_rows = len(df.index)
print(num_rows)




# %% Plot top 5 selling countries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_excel('Online Retail.xlsx')


 

top5_selling_countries = df["Country"].value_counts()[:5]
sns.barplot(x=top5_selling_countries.index, y=top5_selling_countries.values)
plt.xlabel("Country")
plt.ylabel("Amount")
plt.title("Top 5 Selling Countries")


# %% Plot top 20 selling products, drawing the bars vertically to save room for product description
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_excel('Online Retail.xlsx')



top20_selling_products = df["Description"].value_counts()[:20]
sns.barplot(y=top20_selling_products.values, x=top20_selling_products.index)
plt.xlabel("Country")
plt.ylabel("Amount")
plt.title("Top 20 Selling Countries")
plt.show()

# %% Focus on sales in UK
import pandas as pd;
df = pd.read_excel('Online Retail.xlsx')

df = df[df['Country'].isin([ "United Kingdom"])].copy()
df.head()


#%% Show gross revenue by year-month
from datetime import datetime
import pandas as pd;
import seaborn as sns 
import matplotlib.pyplot as plt
df = pd.read_excel('Online Retail.xlsx')

df['GrossRevenue'] = df['Quantity'] * df['UnitPrice']
df["YearMonth"] = df["InvoiceDate"].apply(
    lambda dt: datetime(year=dt.year, month=dt.month, day=1)
)
sns.lineplot(x = df['YearMonth'], y = df['GrossRevenue'], data=df,)
plt.show() # to show graph

# %% save df in pickle format with name "UK.pkl" for next lab activity
# we are only interested in InvoiceNo, StockCode, Description columns
import pandas as pd;
import pickle
df = pd.read_excel('Online Retail.xlsx')
df = df[['InvoiceNo', 'StockCode', 'Description']]
df.to_pickle('UK.pkl')
df.head()
file_path = 'UK.pkl'
with open(file_path, 'wb') as file:
    pickle.dump(df, file)
print("The variable 'data' has been saved successfully.")
file.close()
# %%
