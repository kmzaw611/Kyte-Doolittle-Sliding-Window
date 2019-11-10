# Kyte-Doolittle Hydropathy Sliding Window Program
# Written By: Kaung Myat Zaw
# Date: 11/10/2019

"""
The main program file that has calls towards other functions in other files. It also takes care of the
graphical interface and the window.
"""

from Algorithm import get_avg_hydropathy_dict
from Grapher import plotHydropathGraph
from tkinter import *

root = Tk()
root.title("Kyte-Doolittle Hydropathy Sliding Window Program")
content = Frame(root)
content.grid()

prot_seq_label = Label(content)
prot_seq_label['text'] = 'Enter Protein Sequence: '
prot_seq_label.grid(row=0, column=0, padx=5, pady=5, sticky=S)

aa_seq_box = Text(content, width=60, height=15)
aa_seq_box.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

open_file_button = Button(content)
open_file_button['text'] = "Or parse Fasta file"
open_file_button.grid(row=1, column=0, padx=5, pady=5, sticky=N)

window_size_label = Label(content)
window_size_label['text'] = 'Window Size: '
window_size_label.grid(row=2, column=0, pady=10)

window_size_box = Entry(content)
window_size_box.grid(row=2, column=1)


def plot_button_pressed(event):
    aa_seq = aa_seq_box.get(0.0, END).lower().replace('\n', '')
    plotHydropathGraph(get_avg_hydropathy_dict(aa_seq, int(window_size_box.get())), "test")


plot_button = Button(content)
plot_button['text'] = "Plot Graph"
plot_button.grid(row=3, column=1, pady=10)
plot_button.bind("<Button-1>", plot_button_pressed)

root.mainloop()
