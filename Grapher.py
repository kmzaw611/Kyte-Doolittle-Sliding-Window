# Kyte-Doolittle Hydropathy Sliding Window Program
# Written By: Kaung Myat Zaw
# Date: 11/10/2019

"""
This file contains code for graphing the average hydropathy values obtained from the algorithm.
"""
import matplotlib as mpl
from matplotlib import pyplot


def plotHydropathGraph(avg_hydropath_dict, window_size):
    x_values = []
    y_values = []
    for key in avg_hydropath_dict:
        x_values.append(key)
        y_values.append(avg_hydropath_dict[key])

    pyplot.plot(x_values, y_values, '-y', linewidth=2.0)

    pyplot.xlabel('Amino Acid Number (Window Size = ' + str(window_size) + ')', color='white')
    for i in pyplot.gca().get_xticklabels():
        i.set_color("white")

    pyplot.ylabel('Average Hydrophobicity Value', color='yellow')
    for i in pyplot.gca().get_yticklabels():
        i.set_color("yellow")

    pyplot.title("Kyte-Doolittle Graph", color='yellow')

    fig = pyplot.gcf()
    fig.set_size_inches(16, 8)
    fig.patch.set_facecolor((0.0, 0.0, 0.0))
    fig.patch.set_edgecolor((1.0, 1.0, 1.0))

    axes = pyplot.gca()
    axes.set_ylim([min(y_values)-1, max(y_values)+1])
    axes.set_facecolor((0.0, 0.0, 0.0))

    pyplot.show()
