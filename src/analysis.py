import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#load the dataset
df = pd.read_csv("detailed_ev_charging_stations.csv")

#find the shape and data types
print(df.shape)
print(df.info())

#viewing the first 5 rows
print(df.head())

# Summary statistics
print(df.describe())

# Check missing values
print(df.isna().sum())

# Pie Plot by Charger Type
labels = ['AC Level 1', 'AC Level 2', 'DC Fast Charger']
sizes = pd.Series(labels).value_counts()
fig, ax = plt.subplots()
ax.pie(sizes, labels = labels, autopct = '%1.1f%%')
plt.show()


# Bar Plot by State