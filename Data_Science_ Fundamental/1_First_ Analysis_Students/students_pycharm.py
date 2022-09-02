import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import trim_mean

students = pd.read_csv('students.csv')
print(students.head())


# Using IQR
def outliers(df,col):

    Q1 = df[col].quantile(0.25) # 9
    Q3 = df[col].quantile(0.75) # 14
    IQR = Q3 - Q1 # 5

    lower_threshold =  Q1 - (1.5 * IQR)  #1.5
    higher_threshold = Q3 + (1.5 * IQR) #21.5


    outliers_list = df.index[ df[col] < lower_threshold | df[col] > higher_threshold ]
    return outliers_list



outliers_list = []
for i in 'math_grade':
    outliers_list.extend(outliers(students,i))




# sns.boxplot(x='math_grade', data = students)
# plt.show()
# plt.close()