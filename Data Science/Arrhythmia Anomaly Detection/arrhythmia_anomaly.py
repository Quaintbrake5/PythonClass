# We are to detect anomalies in the dataset
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
import os
import warnings
warnings.filterwarnings('ignore')

# Load the arrhythmia dataset
df = pd.read_csv(r"Data Science/Arrhythmia Anomaly Detection/arrhythmia.data", header=None, sep=',')

# Display first few rows of dataset
print(df.head())
print(df.info())
# print(df.describe())
print(df.isnull().sum())
print(df.shape)

# Anomaly Detection
# In this dataset, class '1' indicates normal instances, while classes '2' to '16' indicate various types of arrhythmia (anomalies).
# We will treat class '1' as normal and all other classes as anomalies.
df['target'] = df[279].apply(lambda x: 0 if x == 1 else 1)  # 0 for normal, 1 for anomaly
df.drop(columns=[279], inplace=True)
print(df['target'].value_counts())
print(df['target'].value_counts(normalize=True))

# Visualizations
# Histogram of target variable
sns.countplot(x='target', data=df)
plt.title('Distribution of Normal vs Anomalous Instances')
plt.xlabel('Class (0: Normal, 1: Anomaly)')
plt.ylabel('Frequency')
plt.show()

# Pair Plot (Due to high dimensionality, we will sample a subset of features for visualization)
n_samples = min(1000, len(df))
sampled_features = df.sample(n=n_samples, random_state=42)  # Sample up to 1000 instances for visualization
plt.figure(figsize=(12,10))
sns.pairplot(sampled_features, hue='target', diag_kind='kde', vars=[sampled_features.columns[i] for i in range(10)])  # Using first 10 features for pairplot
plt.suptitle('Pair Plot of Sampled Features', y=1.02)
plt.show()

# Scatter Plot Diagram (Using first two features for simplicity)
plt.figure(figsize=(10,6))
plt.scatter(df[0], df[1], alpha=0.5, c=df['target'], cmap='coolwarm')
plt.title('Scatter Plot of First Two Features')
plt.xlabel('Feature 0')
plt.ylabel('Feature 1')
plt.colorbar(label='Class (0: Normal, 1: Anomaly)')
plt.show()

# Frequency Distribution (KDE of first feature)
plt.figure(figsize=(10,6))
sns.kdeplot(data=df, x=0, hue="target", fill=True)
plt.title('KDE of Feature 0 by Class')
plt.xlabel('Feature 0')
plt.ylabel('Density')
plt.show()

# Box Plot (First feature by class)
plt.figure(figsize=(10,6))
sns.boxplot(x='target', y=0, data=df)
plt.title('Boxplot of Feature 0 by Class')
plt.xlabel('Class (0: Normal, 1: Anomaly)')
plt.ylabel('Feature 0')
plt.show()

# Correlation Plot
plt.figure(figsize=(12,8))
sns.scatterplot(x=0, y=1, hue='target', data=df)
plt.title('Correlation Plot of Feature 0 vs Feature 1')
plt.xlabel('Feature 0')
plt.ylabel('Feature 1')
plt.show()

# Correlation Heatmap
# plt.figure(figsize=(14,12))
# df_numeric = df.apply(pd.to_numeric, errors='coerce')
# corr = df_numeric.corr()
# sns.heatmap(corr, annot=True, cmap='viridis', fmt=".2f")
# plt.title('Correlation Heatmap of Arrhythmia Features')
# plt.show()


# Prepare data for modeling
# Handle missing values by replacing '?' with NaN and converting to float
df.replace('?', np.nan, inplace=True)
df = df.apply(pd.to_numeric, errors='coerce')

# Impute missing values with column median
# Impute missing values with column median
df.fillna(df.median(numeric_only=True), inplace=True)

# Split features and target
X = df.drop('target', axis=1)
y = df['target']

# Train-test split with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Baseline Classification Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Evaluation
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R² Score:", r2_score(y_test, y_pred))

# Feature Importance
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(12,6))
plt.title("Feature Importances")
plt.bar(range(X.shape[1]), importances[indices], align='center')
plt.xticks(range(X.shape[1]), [str(i) for i in indices])
plt.xlim([-1, X.shape[1]])
plt.show()
# Note: Due to the high dimensionality of the dataset, visualizations and interpretations may be limited.