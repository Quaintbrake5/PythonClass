import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns

# Load the wine datasets (Both red and white)
df_red = pd.read_csv(r"Data Science/Wine Quality/winequality-red.csv", sep=';')
df_white = pd.read_csv(r"Data Science/Wine Quality/winequality-white.csv", sep=';')

# Add a 'type' column to distinguish between red and white wines
df_red['type'] = 'red'
df_white['type'] = 'white'

# Combine the datasets
df = pd.concat([df_red, df_white], ignore_index=True)

# Display the first few rows of the dataset
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.shape)

# Histogram (Of both red and white wine quality)
sns.histplot(data=df, x="quality", hue="type", multiple="stack", bins=10)
plt.title('Distribution of Wine Quality')
plt.xlabel('Quality Score')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot Diagram (Alcohol vs Quality)
plt.figure(figsize=(10,6))
plt.scatter(df['alcohol'], df['quality'], alpha=0.5, c=(df['type'] == 'red').astype(int), cmap='coolwarm')
plt.title('Alcohol Content vs Wine Quality')
plt.xlabel('Alcohol Content')
plt.ylabel('Quality Score')
plt.colorbar(label='Wine Type (W: White, R: Red)')
plt.show()

# Pair Plot
plt.figure(figsize=(12,10))
sns.pairplot(df, hue='type', diag_kind='kde')
plt.suptitle('Pair Plot of Wine Features', y=1.02)
plt.show()

# Frequency Distribution (KDE of Alcohol Content)
plt.figure(figsize=(10,6))
sns.kdeplot(data=df, x="alcohol", hue="type", fill=True)
plt.title('KDE of Alcohol Content by Wine Type')
plt.xlabel('Alcohol Content')
plt.ylabel('Density')
plt.show()

# Box Plot (Quality by Wine Type)
plt.figure(figsize=(10,6))
sns.boxplot(x='type', y='quality', data=df)
plt.title('Boxplot of Wine Quality by Type')
plt.xlabel('Wine Type')
plt.ylabel('Quality Score')
plt.show()

# Correlation Plot
plt.figure(figsize=(12,8))
sns.scatterplot(x='pH', y='quality', hue='type', data=df)
plt.title('Correlation Plot of pH vs Quality')
plt.xlabel('pH Level')
plt.ylabel('Quality Score')
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12,8))
corr = df.drop('type', axis=1).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Wine Features')
plt.show()

# Baseline Regression Model
# For this, Split into train/test; train Linear Regression or Random Forest; evaluate using RMSE, MAE, R².
X = df.drop(['quality', 'type'], axis=1)
y = df['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R² Score:", r2_score(y_test, y_pred))

# Classification Model (Quality as Good (>=7) vs Bad (<7))
# We need to train a classification model to predict if a wine is good or bad based on its features.
df['quality_label'] = (df['quality'] >= 7).astype(int)
X = df.drop(['quality', 'quality_label', 'type'], axis=1)
y = df['quality_label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, y_pred))

