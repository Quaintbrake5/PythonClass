import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

# Data Loading
data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Exam_Score": [35, 50, 55, 65, 70, 75, 80, 85, 95]
}

df = pd.DataFrame(data)


X = df[["Hours_Studied"]]
y = df["Exam_Score"]

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])
print("Mean Squared Error:", mean_squared_error(y, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y, y_pred))
print("R-squared:", r2_score(y, y_pred))

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Student Score Regression Model: Hours Studied vs Exam Score')
plt.legend()
plt.show()