# %% import dataframe from pickle file
import pandas as pd

df = pd.read_pickle("UK.pkl")

df.head()

type(df)
# %% convert dataframe to invoice-based transactional format
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
df = pd.read_pickle("UK.pkl")

te = TransactionEncoder()
te_ary = te.fit(df).transform(df)
df_f = pd.DataFrame(te_ary, columns=te.columns_)



# %% apply apriori algorithm to find frequent items and association rules
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
df = pd.read_pickle("UK.pkl")


te = TransactionEncoder()
te_ary = te.fit(df).transform(df)
df_f = pd.DataFrame(te_ary, columns=te.columns_)
appp = apriori(df_f, min_support=0.2, use_colnames=True, verbose=1)

appp.head()


# %% count of frequent itemsets that have more then 1/2/3 items,
# and the frequent itemsets that has the most items
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
df = pd.read_pickle("UK.pkl")

te = TransactionEncoder()
te_ary = te.fit(df).transform(df)
df_f = pd.DataFrame(te_ary, columns=te.columns_)
apriori(df_f, min_support=0.5, use_colnames=True)

frequent_itemsets = apriori(df_f, min_support=0.6, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets


# %% top 10 lift association rules
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

df = pd.read_pickle("UK.pkl", sep=',')
df.head(10)
frequent_itemsets = apriori(df_f, min_support=0.6, use_colnames=True)
apriori(df, min_support=0.5, use_colnames=False, max_len=None, verbose=0, low_memory=False)
rules = association_rules(freq_items, metric="confidence", min_threshold=0.6)
rules.head()

# %% scatterplot support vs confidence
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x=rules["support"], y=rules["confidence"], alpha=0.5)
plt.xlabel("Support")
plt.ylabel("Confidence")
plt.title("Support vs Confidence")


# %% scatterplot support vs lift
