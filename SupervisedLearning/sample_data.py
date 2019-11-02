"""
    Author: Alexandros Kalamaras
    Date: 02 November 2019
"""

import numpy as np
import matplotlib.pyplot as plt


def calculate_sample_stats(data, N):
    """
    Calculates the mean and variance for a sample of the dataset

    :param data: The data matrix
    :param N: The number that I want to sample
    :return: a list containing the mean estimate and the variance estimate
    """

    rand = np.random.choice(data.shape[0], N, replace=False)
    sample = data[rand, :]

    mean_estimate = np.mean(sample, axis=0)
    var_estimate = np.var(sample,axis=0)
    return mean_estimate, var_estimate


def do_sampling(data, N, repeats):
    """
    Does the sampling and returns the mean and variance estimate for each sample

    :param data: The data matrix
    :param N: The size of each sample
    :param repeats: The number of samples to be taken
    :return: 2 lists containing the mean and variance estimates of a number of samples
    """

    sample_means = np.zeros((repeats, 2))
    sample_vars = np.zeros((repeats, 2))

    for i in range(repeats):
        sample_means[i, :], sample_vars[i, :] = calculate_sample_stats(data, N)

    return sample_means, sample_vars


female_tigers = np.loadtxt(open("data/female_tigers.txt","rb")).T
male_tigers = np.loadtxt(open("data/male_tigers.txt","rb")).T

print(np.mean(female_tigers, axis=0))
print(np.var(female_tigers, axis=0), "\n")

sample = female_tigers[0:20, :]
print(np.mean(sample, axis=0))
print(np.var(sample, axis=0))

sample_means, sample_vars = do_sampling(female_tigers, 10, 100000)
plt.hist(sample_means[:, 0], 1000)
plt.show()