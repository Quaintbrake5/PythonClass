from statistics import kde
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns

# Load the housing dataset
df = pd.read_csv(r"Data Science/Housing/housing.csv")

# Display the first few rows of the dataset
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.shape)

# Histogram
sns.histplot(data=df, x="median_house_value", bins=50, kde=True)
plt.title('Distribution of Median House Value')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot Diagram
plt.figure(figsize=(10,6))
plt.scatter(df['median_income'], df['median_house_value'], alpha=0.5)
plt.title('Median Income vs Median House Value')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.show()

# Frequency Distribution
plt.figure(figsize=(10,6))
sns.kdeplot(data=df, x="median_house_value", shade=True)
plt.title('KDE of Median House Value')
plt.xlabel('Median House Value')
plt.ylabel('Density')
plt.show()

# Box Plot
plt.figure(figsize=(10,6))
sns.boxplot(x='ocean_proximity', y='median_house_value', data=df)
plt.title('Boxplot of Median House Value by Ocean Proximity')
plt.xlabel('Ocean Proximity')
plt.ylabel('Median House Value')
plt.show()