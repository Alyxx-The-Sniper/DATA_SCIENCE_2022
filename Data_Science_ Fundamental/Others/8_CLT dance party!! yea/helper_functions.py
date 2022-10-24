import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns


# choose_statistic() allows us to choose a statistic we want to calculate for our sampling and population distributions.
# It contains two parameters:

# x: An array of numbers
# sample_stat_text: A string that tells the function which statistic to calculate on x.
# It takes on three values: “Mean”, “Minimum”, or “Variance”.
def choose_statistic(x, sample_stat_text):
    # calculate mean if the text is "Mean"
    if sample_stat_text == "Mean":
        return np.mean(x)
    # calculate minimum if the text is "Minimum"
    elif sample_stat_text == "Minimum":
        return np.min(x)
    # calculate variance if the text is "Variance"
    elif sample_stat_text == "Variance":
        return np.var(x, ddof=1) # ddof=1 to edit the formula behind making variance a unbiased estimator
    # if you want to add an extra stat
    # raise error if sample_stat_text is not "Mean", "Minimum", or "Variance"
    else:
        raise Exception('Make sure to input "Mean", "Minimum", or "Variance"')







#population_distribution() allows us to plot the population distribution of a dataframe with one function call.
# It takes the following parameter:
# population_data: the dataframe being passed into the function
def population_distribution(population_data):
    # plot the population distribution
    sns.histplot(population_data, stat='density')
    # informative title for the distribution
    plt.title(f"Population Distribution")
    # remove None label
    plt.xlabel('')
    plt.show()
    plt.clf()




# sampling_distribution() allows us to plot a simulated sampling distribution of a statistic.
# The simulated sampling distribution is created by taking random samples of some size,
# calculating a particular statistic, and plotting a histogram of those sample statistics.
# It contains three parameters:
# population_data: the dataframe being sampled from
# samp_size: the size of each sample
# stat: the specific statistic being measured for each sample — either “Mean”, “Minimum”, or “Variance”
def sampling_distribution(population_data, samp_size, stat):
    # list that will hold all the sample statistics
    sample_stats = []
    for i in range(500):
        # get a random sample from the population of size samp_size
        samp = np.random.choice(population_data, samp_size, replace=False)
        # calculate the chosen statistic (mean, minimum, or variance) of the sample
        sample_stat = choose_statistic(samp, stat)
        # add sample_stat to the sample_stats list
        sample_stats.append(sample_stat)

    pop_statistic = round(choose_statistic(population_data, stat), 2)
    # plot the sampling distribution
    sns.histplot(sample_stats, stat='density')
    # informative title for the sampling distribution
    plt.title(
        f"Sampling Distribution of the {stat} \nMean of the Sample {stat}s: {round(np.mean(sample_stats), 2)} \n Population {stat}: {pop_statistic}")
    plt.axvline(pop_statistic, color='g', linestyle='dashed', label=f'Population {stat}')
    # plot the mean of the chosen sample statistic for the sampling distribution
    plt.axvline(np.mean(sample_stats), color='orange', linestyle='dashed', label=f'Mean of the Sample {stat}s')
    plt.legend()
    plt.show()
    plt.clf()