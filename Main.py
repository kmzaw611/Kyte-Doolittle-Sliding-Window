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
from tkinter import filedialog
from tkinter.messagebox import showerror
import os.path


def plot_button_pressed(event):
    aa_seq = aa_seq_box.get(0.0, END).lower().replace('\n', '')
    window_size = int(window_size_box.get())
    plotHydropathGraph(get_avg_hydropathy_dict(aa_seq, window_size), window_size, sequence_name)


# The name of the sequence that is graphed. For a text file, it will just be the name of the text file.
# For a FASTA file, it will be the description accompanying the sequence.
sequence_name = ""


def parse_fasta_file(file):
    """
    Sets the sequence_name variable to the description in the FASTA file.
    :param file: A Fasta file with the description of the sequence and the sequence.
    :return: The amino acid sequence of the Fasta file.
    """

    # the first line of a fasta file is usually the description of the amino acid sequence.
    first_line = file.readline()
    global sequence_name
    sequence_name = first_line.replace(">", "")
    return file.read()


def open_button_pressed(event):
    filename = filedialog.askopenfilename(title="Select sequence file", filetypes=(("FASTA files", "*.fasta"),
                                                                                   ("Text files", "*.txt")))
    if filename:
        try:
            file = open(filename, 'r')
            extension = os.path.splitext(filename)[1]
            if extension == '.fasta':
                aa_seq = parse_fasta_file(file)
                aa_seq_box.delete(0.0, END)
                aa_seq_box.insert(INSERT, aa_seq)
            elif extension == '.txt':
                aa_seq = file.read().lower().replace('\n', '')
                aa_seq_box.delete(0.0, END)
                aa_seq_box.insert(INSERT, aa_seq)
                global sequence_name
                sequence_name = os.path.basename(filename) + "\n"

        except FileNotFoundError and IOError:
            showerror("Error Reading File", "Failed to read the file: '%s'" % os.path.basename(filename))


root = Tk()
root.title("Kyte-Doolittle Hydropathy Sliding Window Program")
content = Frame(root)
content.grid()

prot_seq_label = Label(content)
prot_seq_label['text'] = 'Enter Protein Sequence: '
prot_seq_label.grid(row=0, column=0, padx=5, pady=5, sticky=S)

v = StringVar()
aa_seq_box = Text(content, width=60, height=15)
aa_seq_box.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

open_file_button = Button(content)
open_file_button['text'] = "Or parse Fasta file"
open_file_button.grid(row=1, column=0, padx=5, pady=5, sticky=N)
open_file_button.bind("<Button-1>", open_button_pressed)

window_size_label = Label(content)
window_size_label['text'] = 'Window Size: '
window_size_label.grid(row=2, column=0, pady=10)

window_size_box = Entry(content)
window_size_box.grid(row=2, column=1)

plot_button = Button(content)
plot_button['text'] = "Plot Graph"
plot_button.grid(row=3, column=1, pady=10)
plot_button.bind("<Button-1>", plot_button_pressed)

root.mainloop()
