from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
import pickle

import backend

class GUI(backend.backend):
    def __init__(self):

        # Execute select syntax and return data to be processed
        self.data = self.select("SELECT id, stock FROM product")

        # Separate the data
        id, stock = zip(*self.data)

        # Configure the tables
        self.bar_coords = range(len(id))

        plt.bar(self.bar_coords, stock)

        plt.xticks(self.bar_coords, id)
        plt.title('Menu Stock Report')
        plt.show()
