import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# preset values
significance_threshold = 0.05
sample_size = 100
lift = .3
control_rate = .5
name_rate = (1 + lift) * control_rate

# initialize an empty list of results
results = []

# start the loop
for i in range(200):
  # simulate data:
  sample_control = np.random.choice(['yes', 'no'],  size=int(sample_size/2), p=[control_rate, 1-control_rate])
  sample_name = np.random.choice(['yes', 'no'], size=int(sample_size/2), p=[name_rate, 1-name_rate])
  group = ['control']*int(sample_size/2) + ['name']*int(sample_size/2)
  outcome = list(sample_control) + list(sample_name)
  sim_data = {"Email": group, "Opened": outcome}
  sim_data = pd.DataFrame(sim_data)

  # run the test
  ab_contingency = pd.crosstab(np.array(sim_data.Email), np.array(sim_data.Opened))
  chi2, pval, dof, expected = chi2_contingency(ab_contingency)
  result = ('significant' if pval < significance_threshold else 'not significant')

  # append the result to our results list here:
  # results.append(result)


print(sim_data)


# calculate proportion of significant results here:
results =  np.array(results)
# # divide by 200 bcoz we have repeated the experiment 200 times
# print("Proportion of significant results:")
# print(np.sum(results == 'significant')/200)
# print("Proportion of NOT significant results:")
# print(np.sum(results == 'not significant')/200)

import matplotlib as plt
hours_reported =[3, 2.5, 2.75, 2.5, 2.75, 3.0, 3.5, 3.25, 3.25,  3.5, 3.5, 3.75, 3.75,4, 4.0, 3.75,  4.0, 4.25, 4.25, 4.5, 4.5, 5.0, 5.25, 5, 5.25, 5.5, 5.5, 5.75, 5.25, 4.75]
exam_scores = [52.53, 59.05, 61.15, 61.72, 62.58, 62.98, 64.99, 67.63, 68.52, 70.29, 71.33, 72.15, 72.67, 73.85, 74.44, 75.62, 76.81, 77.82, 78.16, 78.94, 79.08, 80.31, 80.77, 81.37, 85.13, 85.38, 89.34, 90.75, 97.24, 98.31]

# Create your figure here
plt.figure(figsize=(10,8))

# Create your hours_lower_bound and hours_upper_bound lists here
# list comprehension
hours_lower_bound = [element - (element * 0.2) for element in hours_reported]
hours_upper_bound = [element + (element * 0.2) for element in hours_reported]

# Make your graph here
plt.plot(exam_scores, hours_reported, linewidth=2)

plt.fill_between(exam_scores, hours_lower_bound, hours_upper_bound, alpha = 0.2)

plt.xlabel("Score")
plt.title("Time spent studying vs final exam scores")
plt.ylabel('Hours studying (self-reported)')
