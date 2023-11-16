# %% Import excel to dataframe
import pandas as pd
# import excel to dataframe
df = pd.read_excel("Online Retail.xlsx")


# %%  Show the first 10 row
# show the first 10 rows
df.head(10)


# %% Generate descriptive statistics regardless the datatypes
df.describe(include="all")


# %% Remove all the rows with null value and generate stats again
df = df.dropna()
df

# %% Remove rows with invalid Quantity (Quantity being less than 0)
df = df[(df['Quantity']>0)]
df


# %% Remove rows with invalid UnitPrice (UnitPrice being less than 0)
df = df[(df['UnitPrice']>0)]
df


# %% Only Retain rows with 5-digit StockCode
df["StockCode"] = df["StockCode"].astype("string")
mask = (df['StockCode'].str.len() == 5)
df =df.loc[mask]
df


# %% strip all description
df['Description'] = df['Description'].str.strip()
df



# %% Generate stats again and check the number of rows
df.describe(include="all")




# %% Plot top 5 selling countries
import matplotlib.pyplot as plt
import seaborn as sns

top5_selling_countries = df["Country"].value_counts()[:5]
sns.barplot(x=top5_selling_countries.index, y=top5_selling_countries.values)
plt.xlabel("Country")
plt.ylabel("Amount")
plt.title("Top 5 Selling Countries")


# %% Plot top 20 selling products, drawing the bars vertically to save room for product description
top20_selling_products = df["Description"].value_counts()[:20]
sns.barplot(x=top20_selling_products.values, y=top20_selling_products.index)
plt.ylabel("Country")
plt.xlabel("Amount")
plt.title("Top 20 Selling Countries")


# %% Focus on sales in UK
df = df[df['Country'].isin([ "United Kingdom"])]
df


#%% Show gross revenue by year-month
from datetime import datetime

df['GrossRevenue'] = df['Quantity'] * df['UnitPrice']
df["YearMonth"] = df["InvoiceDate"].apply(
    lambda dt: datetime(year=dt.year, month=dt.month, day=1)
)
sns.lineplot(
    data=df.groupby("YearMonth").sum(numeric_only=True).reset_index(),
    x = 'YearMonth', 
    y = 'GrossRevenue',
)


# %% save df in pickle format with name "UK.pkl" for next lab activity
# we are only interested in InvoiceNo, StockCode, Description columns
df = df[['InvoiceNo', 'StockCode', 'Description']]
df.to_pickle('UK.pkl')

# %%
