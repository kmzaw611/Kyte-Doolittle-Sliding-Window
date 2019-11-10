# Kyte-Doolittle Hydropathy Sliding Window Program
# Written By: Kaung Myat Zaw
# Date: 11/10/2019

"""
This file contains code for graphing the average hydropathy values obtained from the algorithm.
"""

from matplotlib import pyplot


def plotHydropathGraph(avg_hydropath_dict, protein_seq_name):
    x_values = []
    y_values = []
    for key in avg_hydropath_dict:
        x_values.append(key)
        y_values.append(avg_hydropath_dict[key])

    pyplot.plot(x_values, y_values)
    pyplot.xlabel('Sequence Number')
    pyplot.ylabel('Avg. Hydrophobicity Value')
    pyplot.title("Kyte-Doolittle Graph for " + protein_seq_name)
    pyplot.show()
