import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('test_data.csv')

# Create the model here:
model =sm.OLS.from_formula('score ~ hours_studied', data = students)
# Fit the model here:
results = model.fit()
# Print the coefficients here:
# print(results.params)
# output
# Intercept        43.016014 (intercept is the expected value of the outcome variable when the predictor is equal to zero)
# hours_studied     9.848111 (slope is the expected difference in the outcome variable for a one unit difference in the predictor variable)


# Write equation for a line
y = 9.85 * students.hours_studied + 43

# Create the plot here:
plt.scatter(students.hours_studied, students.score)
plt.title('LInear Regret')
plt.xlabel('hours study')
plt.ylabel('math score')
plt.plot(students.hours_studied, y)
# plt.show()
plt.close()




###################################
# QUANTITATIVE PREDICTOR

# Using a Regression Model for Prediction

# Calculate and print `pred_3hr` here:
pred_3hr = results.params[1]*3 + results.params[0]
# print(pred_3hr)


###################################
# Interpretation of the intercept:
# A student who studied for 0 hours is expected to score a 43 on the test.

# Interpretation of the slope:
# For every additional 1 hour of studying, students are expected to score 9.8 points higher on the test.


###################################
# Checking
# Assumptions of Linear Regression

# Calculate `fitted_values` here:
fitted_values = results.predict(students)
# print(fitted_values)

# Calculate `residuals` here:
residuals = students.score - fitted_values

# Print the first 5 residuals here:
# print(residuals[0:5])


# Normality assumption
plt.hist(residuals)
# plt.show()
plt.close()

# Homoscedasticity assumption
plt.scatter(fitted_values, residuals)
# plt.show()
plt.close()




######################################################################################
# Categorical Predictors
# predicting score base on breakfast

# Calculate group means
no_bf = students[students['breakfast'] == 0]
with_bf = students[students['breakfast'] == 1]

# or we can use this code
# print(students.groupby('breakfast').mean().score)

# Create the scatter plot here:
plt.scatter(students.breakfast,students.score)
plt.plot([0,1],[no_bf.mean(), with_bf.mean()])
plt.xlabel('breakfast = 1 no breakfast = 0')
plt.ylabel('score')
# plt.show()


####################################################
# CATEGORIACAL PREDICTOR
# Predicting score with breakfast

# Note that this will work if the play_bball variable is coded with 0s and 1s, but it will also work if it is coded
# with Trues and Falses, or even if it is coded with strings like 'yes' and 'no'

# Calculate and print group means
mean_score_no_breakfast = np.mean(students.score[students.breakfast == 0])
mean_score_breakfast = np.mean(students.score[students.breakfast == 1])
print('Mean score (no breakfast): ', mean_score_no_breakfast)
print('Mean score (breakfast): ', mean_score_breakfast)


model = sm.OLS.from_formula('score ~ breakfast', data = students)
results = model.fit()
print(results.params)

# output
# Mean score (no breakfast):  61.664150943396216
# Mean score (breakfast):  73.72127659574468

# Intercept    61.664151
# breakfast    12.057126
# if you dont take breakfast your score could be 61.66 but if you take breakfast
# your score could be 73.72

