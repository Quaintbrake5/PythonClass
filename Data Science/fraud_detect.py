# Import Pandas
import pandas as pd
import sys
sys.path.insert(0, r'C:\Users\DELL\AppData\Local\Programs\Python\Python313\Lib\site-packages')

# Load the dataset
df = pd.read_csv("Data Science/bank_transactions_data.csv")

# Data Loading and Initial Inspection
print(df.info())
print(df.describe())
print(df.head())
print(df.tail())
print(df.shape)

# Data Cleaning
print(df.isnull().sum())
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.shape)

# Exploratory Data Analysis (EDA)
print(df['TransactionType'].value_counts())
print(df['TransactionAmount'].describe())
print(df['AccountID'].nunique())
print(df['MerchantID'].nunique())
print(df.groupby('TransactionType')['TransactionAmount'].mean())

# Feature Engineering and Wrangling
df['hour'] = pd.to_datetime(df['TransactionDate']).dt.hour
df['day'] = pd.to_datetime(df['TransactionDate']).dt.day
df['month'] = pd.to_datetime(df['TransactionDate']).dt.month
df['year'] = pd.to_datetime(df['TransactionDate']).dt.year
df.drop(['TransactionDate', 'PreviousTransactionDate', 'TransactionID', 'AccountID', 'DeviceID', 'IP Address', 'MerchantID'], axis=1, inplace=True)

# Encode categorical variables
df = pd.get_dummies(df, columns=['TransactionType', 'Location', 'Channel', 'CustomerOccupation'], drop_first=True)

# Create a proxy target variable for fraud detection based on LoginAttempts > 1
df['is_fraud'] = (df['LoginAttempts'] > 1).astype(int)

print(df.head())
print(df.shape)

# Baseline Classification Model
# For this, Split into train/test; train Logistic Regression or Random Forest; evaluate using Accuracy, Precision, Recall, F1, ROC AUC, Confusion Matrix.
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
X = df.drop('is_fraud', axis=1)
y = df['is_fraud']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, y_pred))

# Interpretation and Insights
importances = model.feature_importances_
feature_names = X.columns
feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
print(feature_importance_df)

# Interpretation and Insights with Matplotlib
# Which features are most predictive? Where does the model make errors (false positives/false negatives)? What are the business implications?

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.barh(feature_importance_df['Feature'][:10], feature_importance_df['Importance'][:10], color='skyblue')
plt.xlabel('Importance')
plt.title('Top 10 Feature Importance in Fraud Detection Model')
plt.show()

# Visualize distributions: histograms, boxplots, violin plots.
import seaborn as sns

plt.figure(figsize=(10,6))
sns.boxplot(x='TransactionAmount', data=df)
plt.title("Boxplot of Transaction Amounts")
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(data=df, x='TransactionAmount', bins=50, kde=True)
plt.title("Histogram of Transaction Amounts")
plt.show()

plt.figure(figsize=(10,6))
sns.violinplot(x='TransactionAmount', data=df)
plt.title("Violin Plot of Transaction Amounts")
plt.show()

