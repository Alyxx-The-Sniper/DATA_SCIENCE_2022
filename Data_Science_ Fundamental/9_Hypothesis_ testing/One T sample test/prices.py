import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp

# Comparing a sample average to a hypothetical population average
#
# Example # 1
# Suppose that a product manager wants online BuyPie orders to cost around 1000 Rupees on average. In the past day,
# 50 people made an online purchase and the average payment per order was less than 1000 Rupees.
# Are people really spending less than 1000 Rupees on average?
# Or is this the result of chance and
# a small sample size?

# • Null: The average cost of a BuyPie order is 1000 Rupees
# • Alternative: The average cost of a BuyPie order is not 1000 Rupees.


prices = np.genfromtxt("prices.csv")
prices_mean = np.mean(prices)
#output 980

#plot your histogram here
plt.hist(prices)
plt.axvline(x=prices_mean, color = 'r') # this is our mean while our target is 1000
# plt.show()

tstat, pval = ttest_1samp(prices,1000)
print(pval)
# our pval is relatively higher than 0.05 thus we will accept our null hypothesis