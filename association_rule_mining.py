# %% import dataframe from pickle file
import pandas as pd

df = pd.read_pickle("UK.pkl")

df.head()


# %% convert dataframe to invoice-based transactional format
from mlxtend.preprocessing import TransactionEncoder

df_invoice = df.groupby(["InvoiceNo"]).apply(
    lambda gdf: gdf["Description"].to_list()
)

te = TransactionEncoder()
transactions = te.fit_transform(df_invoice)
transactions = pd.DataFrame(transactions, columns=te.columns_)
transactions


# %% apply apriori algorithm to find frequent items and association rules
from mlxtend.frequent_patterns import apriori, association_rules

freq_items = apriori(
    transactions,
    min_support=0.01,
    use_colnames=True,
    verbose=1,
)
rules = association_rules(
    freq_items,
    metric="confidence",
    min_threshold=0.6,
)


# %% count of frequent itemsets that have more then 1/2/3 items,
# and the frequent itemsets that has the most items
freq_items["length"] = freq_items["itemsets"].apply(len)
print((freq_items["length"] > 1).sum())
print((freq_items["length"] > 2).sum())
print((freq_items["length"] > 3).sum())
print(freq_items["length"].max())

print(
    freq_items[freq_items["length"] == freq_items["length"].max()][
        "itemsets"
    ].tolist()
)


# %% top 10 lift association rules

rules.sort_values("lift", ascending=False).head(10)[
    ["antecedents", "consequents"]
]


# %% scatterplot support vs confidence
import seaborn as sns

ax = sns.scatterplot(
    data=rules,
    x="support",
    y="confidence",
    alpha=0.5,
)
ax.set(
    xlabel="Support",
    ylabel="Confidence",
    title="Support vs Confidence",
)


# %% scatterplot support vs lift
ax = sns.scatterplot(data=rules, x="support", y="lift", alpha=0.5)
ax.set(
    xlabel="Support",
    ylabel="Lift",
    title="Support vs Lift",
)
