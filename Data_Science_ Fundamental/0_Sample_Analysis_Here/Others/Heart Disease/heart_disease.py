import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp
from scipy.stats import binom_test




# details:
# chol: serum cholestorol in mg/dl
# fbs: An indicator for whether fasting blood sugar is greater than 120 mg/dl (1 = true; 0 = false)

pd.set_option('display.max_columns', None)
heart = pd.read_csv('heart_disease.csv')
# print(heart.head())
# print(heart.shape)

# with heart disease
yes_hd = heart[heart.heart_disease == 'presence']
# without heart disease
no_hd = heart[heart.heart_disease == 'absence']

# colesterol level w/ hd
chol_hd = yes_hd.chol
# print(chol_hd)


# In general, total cholesterol over 240 mg/dl is considered “high” (and therefore unhealthy).
# mean cholesterol level for patients who were diagnosed with heart disease
print(np.mean(chol_hd))

#Null: People with heart disease have an average cholesterol level equal to 240 mg/dl
# Alternative: People with heart disease have an average cholesterol level that is greater than 240 mg/dl


tstat, pval = ttest_1samp(chol_hd,240)
print(pval)


plt.hist(chol_hd)
# plt.show()

p_val_one =