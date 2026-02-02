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
plt.title('Charger Type Distribution')
plt.show()

# Bar Plot for Usage Stats vs Charger Type
plt.figure(figsize=(10,6))
ax = sns.barplot(x='Charger Type', y='Usage Stats (avg users/day)', data=df, hue='Charger Type', legend=False)

for container in ax.containers: 
    ax.bar_label(container, fmt='%.1f', padding=3, fontsize=10, fontweight='bold')

plt.margins(y=0.1) 
plt.title('Average Usage Stats by Charger Type (2026 Data)')
plt.xlabel('Charger Type')
plt.ylabel('Average Usage Stats (avg users/day)')
plt.show()

# Installation Year and Charging Capacity Analysis
plt.figure(figsize=(12,6))
sns.scatterplot(x='Installation Year', y='Charging Capacity (kW)', data=df, hue='Charger Type', style='Charger Type', s=100)
plt.title('Installation Year vs Charging Capacity')
plt.xlabel('Installation Year')
plt.ylabel('Charging Capacity (kW)')
plt.legend(title='Charger Type')
plt.show()


