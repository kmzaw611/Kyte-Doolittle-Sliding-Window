# Kyte-Doolittle Hydropathy Sliding Window Program
# Written By: Kaung Myat Zaw
# Date: 11/10/2019

"""
This file contains the main algorithm of the program.
Input: Protein sequence and window size.
Output: A dictionary that returns the average hydropathy value for each amino acid window in the sequence.
"""

# The hydropathy scale that is used by the program
hydro_scale = {'a': 1.8, 'c': 2.5, 'd': -3.5, 'e': -3.5, 'f': 2.8, 'g': -0.4, 'h': -3.2, 'i': 4.5, 'k': -3.9, 'l': 3.8,
               'm': 1.9, 'n': -3.5, 'p': -1.6, 'q': -3.5, 'r': -4.5, 's': -0.8, 't': -0.7, 'v': 4.2, 'w': -0.9,
               'y': -1.3}


def get_avg_hydropathy_dict(aa_seq, window_size):
    avg_hydropathy_dict = {}
    window_index = 0
    while window_index <= len(aa_seq) - window_size:
        window_sequence = aa_seq[window_index: window_index + window_size]
        hydropathy_sum = 0
        for aa in window_sequence:
            hydropathy_value = hydro_scale[aa]
            hydropathy_sum += hydropathy_value
        hydropathy_avg = hydropathy_sum / window_size
        # we increment by 1 for the key value since for the program, we want index to start at 1
        avg_hydropathy_dict[window_index + 1] = hydropathy_avg
        window_index += 1

    return avg_hydropathy_dict
