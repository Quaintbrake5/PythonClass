# MatplotLib.... python lib for data visualisation


# STATISTICS...
# The science of learning about data and making inferences from it.
# It provides tools for collecting, analyzing, interpreting, and presenting data in order to make informed decisions and draw meaningful conclusions.
# It bridges the gap between raw data and actionable insights, enabling individuals and organizations to make informed decisions based on evidence rather than intuition or guesswork.
# 
# Descriptive statistics: Summarizing and describing the main features of a dataset.
# Inferential statistics: Making predictions or inferences about a population based on a sample of data.
#
# Box plots, histograms, scatter plots, bar charts, line graphs, pie charts
# Central tendency: Mean, median, mode
# Dispersion: Range, variance, standard deviation
# Correlation and regression analysis
# Probability distributions: Normal distribution, binomial distribution, Poisson distribution
# Testing hypotheses: Null hypothesis, alternative hypothesis, p-values, confidence intervals, regression
# Sampling methods: Random sampling, stratified sampling, cluster sampling
# 
# WHY STATISTICS IS CRITICAL IN DATA SCIENCE...
# In era of big data, it is essential for...
# 
# 1. Interpretation: Data can be misread (average vs median salary in a company tell very different stories....)
# 2. Prediction: Probability and statistical models help predict future trends and behaviors based on historical data. (E.g. )
# 3. Decision-Making: Statistical analysis provides a solid foundation for making informed decisions, helping to minimize risks and maximize opportunities. (E.g. A/B testing)
# 4. Data Quality: Statistical techniques help identify outliers, missing values, and inconsistencies in data, ensuring that analyses are based on accurate and reliable information.
# 5. Model Evaluation: Statistics are used to assess the performance of machine learning models,
# 
# PROBABILITY vs. STATISTICS
# 
# Probability: Predicts what data we're most likely to see (e.g toss a fair coin/die)...
# Statistics: Starts with data; tries to infer what model produced it...
# 
# Mean: Arithmetic average of all values...                             
# Median: Value that splits ordered data into two parts.... if 'n' is odd, the middle is the median; if their two values, take the average
# unlike Mean, Median is robust and immune to skewed data and outliers. It represents the typical case especially in skewed distribution....
# 
# #


# import matplotlib.pyplot as plt
# import numpy as np


# plt.plot(days, sales, marker='o')
# plt.title("Sales over 5 days")
# plt.xlabel("Days")
# plt.ylabel("Unit sold")
# plt.show()

# products = ["Bread", "Milk", "Beef"]
# unitSold = [300,230,430]

# plt.bar(products, unitSold, color=['blue', 'green', 'pink'])

# plt.title("Sales over 5 days")
# plt.xlabel("Unit sold per produt")
# plt.ylabel("Units")
# plt.show()

import numpy as np

purchases = np.array([10,20,30,200,300])

mean_value = purchases.mean()

# print(mean_value)


data = np.array([45,50,52,55,60,65,150,200])
average = data.mean()
middle = np.median(data)
print(f"Mean: {average} \nMedian: {middle}")