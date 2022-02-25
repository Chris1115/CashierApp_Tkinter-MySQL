from tkinter import *
from tkinter import ttk

import backend
import tkinter.messagebox as msgBox


class GUI(backend.backend):
    def __init__(self, data):

        # Assign data from the main window
        self.data = data

        # Declare window properties
        self.form = Toplevel()
        self.form.geometry('780x540')
        self.form.title('EDIT MENU')

        # Declare Label Frame
        self.id = LabelFrame(self.form, text='ID')
        self.name = LabelFrame(self.form, text='Name')
        self.stock = LabelFrame(self.form, text='Stock')
        self.price = LabelFrame(self.form, text='Price')

        self.id.pack(pady=10)
        self.name.pack(pady=10)
        self.stock.pack(pady=10)
        self.price.pack(pady=10)

        # Declare window title
        self.title = Label(self.form, text='New Data', font=('bold', 30))

        # Declare Entry
        self.id_entry = Entry(self.id)
        self.name_entry = Entry(self.name)
        self.stock_entry = Entry(self.stock)
        self.price_entry = Entry(self.price)

        # Declare Button
        self.edit_btn = Button(self.form, text='submit', font=('regular', 18), bg="white", command=lambda:self.add_data(self.id_entry.get(), self.name_entry.get(), self.stock_entry.get(), self.price_entry.get()))

        # Pack Entry
        self.id_entry.pack()
        self.name_entry.pack()
        self.stock_entry.pack()
        self.price_entry.pack()

        # Assign Data Value in the entry
        self.id_entry.insert(0, data[0])
        self.name_entry.insert(0, data[1])
        self.stock_entry.insert(0, data[2])
        self.price_entry.insert(0, data[3])

        # Pack Button
        self.edit_btn.pack()
        
    # Function to update data from the entry
    def add_data(self, id, name, stock, price):
        if(self.action(f"UPDATE product SET id={id}, name='{name}', stock='{stock}', price='{price}' WHERE id={self.data[0]}")):
            print("Selected Menu has been successfully Updated in the Database -- ADMIN")

            self.id_entry.delete(0, END)
            self.name_entry.delete(0, END)
            self.stock_entry.delete(0, END)
            self.price_entry.delete(0, END)

            self.form.destroy()
        else:
            print("Something problem, check with product ID or input data -- ADMIN")