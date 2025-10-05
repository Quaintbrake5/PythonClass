import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv(r"Data Science/titanic.csv")

#Take a peek at the data
print("Shape of the dataset:", df.shape)
print("\nFirst 5 rows", df.head())
print("\nDataset Info:\n")
print(df.info())
print("\n Summary Statistics (numeric columns)\n", df.describe())


#Check for missing values
# print("\nMissing values:\n", df.isnull().sum())

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
# print("\nMissing values:\n", df.isnull().sum())

df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
# print("\nMissing values:\n", df.isnull().sum())

# Drop 'Cabin' column due to high number of missing values
df.drop(columns=['Cabin'], inplace=True)
# print("\nMissing values:\n", df.isnull().sum())

# print("\nValue count for survived", df["Survived"].value_counts())

# print("\nValue count for sex", df["Sex"].value_counts())


# Visualizations
sns.countplot(x='Survived', data=df)
plt.title('Survival Count(0 = Died, 1 = Survived)')
plt.show()

sns.countplot(x= 'Sex', hue='Survived', data=df)
plt.title('Survival by Gender')
plt.show()

sns.histplot(x=df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

sns.boxplot(x='Pclass', y='Age', data=df)
plt.title('Age Distribution by Passenger Class')
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
