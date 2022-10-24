# Binomial Test

#LIVE.com — a website that sells all the necessary props and costumes to recreate iconic movie scenes at home!
# The marketing department at Live-it-LIVE reports that, during this time of year, about 10% of visitors to Live-it-LIVE.com
# make a purchase.
#
# The monthly report shows every visitor to the site and whether or not they made a purchase.
# The checkout page had a small bug this month, so the business department wants to know whether the purchase rate dipped
# below expectation. They’ve asked us to investigate this question.
#
# In order to run a hypothesis test to address this, we’ll first need to know two things from the data:
#
# The number of people who visited the website
# The number of people who made a purchase on the website
# Assuming each row of our dataset represents a unique site visitor, we can calculate the number of people who visited the website
# by finding the number of rows in the data frame. We can then find the number who made a purchase by using a conditional statement
# to add up the total number of rows where a purchase was made.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


monthly_report = pd.read_csv('monthly_report.csv')
# print(monthly_report.head()
# print(monthly_report.purchase.unique())

# Number of visitors in our site (monthly_report)
sample_size = len(monthly_report)
# print(sample_size)


# Number of purchases
num_purchased = np.sum(monthly_report.purchase == 'y')
# print(num_purchased)


###################################################################
# Simulating Randomness
# p = 0.1 because of 10% purchase rate as per marketing
simulated_monthly_visitors = np.random.choice(['y', 'n'], size= sample_size, p=[0.1, 0.9])
# print(simulated_monthly_visitors)



# simulated number of purchase per month
simulated_num_purchased = np.sum(simulated_monthly_visitors == 'y')
# print(simulated_num_purchased)



# Repeat multiple times
null_outcomes = []

#start for loop here:
for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=sample_size, p=[0.1, 0.9])
  simulated_num_purchased = np.sum(simulated_monthly_visitors == 'y')
  null_outcomes.append(simulated_num_purchased)
# print(null_outcomes)



#calculate the minimum and maximum values in null_outcomes here:
null_min = np.min(null_outcomes)
null_max = np.max(null_outcomes)
# print(null_min)
# print(null_max)



# Inspecting the Null Distribution
plt.hist(null_outcomes)
plt.axvline(num_purchased, color = 'r')
# plt.show()



# Confidence Intervals 95%
null_95CI = np.percentile(null_outcomes, [2.5,97.5])
# print(null_95CI)


# If our observed statistic falls outside this interval, then we can conclude it is unlikely that the null hypothesis is true.
# In this example, because 41 falls within the 95% interval (37 - 63), it is still reasonably likely that we observed a
# lower purchase rate by random chance, even though the null hypothesis was true.



####################################################################################
# Calculating a One-Sided P-Value

# Null: the probability of a purchase was 10%
# Alternative: the probability of a purchase rate was LESS THAN 10%
null_outcomes = np.array(null_outcomes)
p_value_one = np.sum(null_outcomes <= num_purchased) / len(null_outcomes)
# print(p_value_one)




####################################################################################
# Calculating a Two-Sided P-Value
# calculate the proportion of values in null_outcomes that are less than or equal to 41 (the number of purchases we
# observed in our sample, which is 9 fewer than 50) OR greater than or equal to 59 (which is 9 purchases more than 50)


p_value_2 = np.sum((null_outcomes <= 41) | (null_outcomes >= 59))/len(null_outcomes)
# print(p_value_2)



#####################################################################################
# sample code

import numpy as np
import pandas as pd
from scipy.stats import binom_test


def simulation_binomial_test(observed_successes, n, p):
    # initialize null_outcomes
    null_outcomes = []

    # generate the simulated null distribution
    for i in range(10000):
        simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1 - p])
        num_purchased = np.sum(simulated_monthly_visitors == 'y')
        null_outcomes.append(num_purchased)

    # calculate a 1-sided p-value
    null_outcomes = np.array(null_outcomes)
    p_value = np.sum(null_outcomes <= observed_successes) / len(null_outcomes)

    # return the p-value
    return p_value


# Test your function below by uncommenting the code below. You should see that your simulation function gives you a very similar answer to the binom_test function from scipy:

p_value1 = simulation_binomial_test(45, 500, .1)
# print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative='less')
# print("binom_test p-value: ", p_value2)


##############################################################################

# as the number of experiment increase(trials) the more change of false positive
# at what number of trials can a 1 false positive occur with 0.05 significant threshold?
#


import numpy as np
from scipy.stats import binom_test

# Initialize num_errors
false_positives = 0
# Set significance threshold value
sig_threshold = 0.05

# Run binomial tests & record errors
for i in range(1000):
    sim_sample = np.random.choice(['correct', 'incorrect'], size=100, p=[0.8, 0.2])
    num_correct = np.sum(sim_sample == 'correct')
    p_val = binom_test(num_correct, 100, .8)
    if p_val < sig_threshold:
        false_positives += 1

# Print proportion of type I errors
print(false_positives)