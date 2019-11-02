"""
    Author : Alexandros Kalamaras
    Date : 01 November 2019
"""

import numpy as np
import matplotlib.pylab as plt


def plot_feature_on_classes(data, classes, feature):
    """
    Creates plots to visually compare a feature on different classes

    :param data: The data matrix
    :param classes: A list of data, each entry of which contains data of 1 class
    :param feature: A number indicating the feature number on the data matrix
    """

    length = len(classes)

    for i in range(length):
        classfeature = data[classes[i], feature]
        plt.subplot(length, 1, i + 1)
        plt.plot(classfeature)
        plt.xlim(-0.5, 50)
    plt.show()


def histogram_feature_on_classes(data, classes, feature):

    """
    Creates and plots a list of histograms to visually compare a feature on different classes

    :param data: The data matrix
    :param classes: A list of data, each entry of which contains data of 1 class
    :param feature: A number indicating the feature number on our data matrix
    """

    length = len(classes)

    for i in range(length):
        classfeature = data[classes[i], feature]
        plt.subplot(length, 1, i + 1)
        plt.hist(classfeature, bins=np.linspace(-0.5, 50, 30))
        plt.xlim(-0.5, 50)
    plt.show()


"""
data = np.loadtxt(open("data/liver_data.txt", "rb"), delimiter = ",")

alcohol_consumption = data[:, 5]
wellPeople = data[:, 6] == 1
illPeople = data[:, 6] == 2
classes = [wellPeople, illPeople]
# histogram_feature_on_classes(data, classes, 5)
plot_feature_on_classes(data, classes, 4)

"""