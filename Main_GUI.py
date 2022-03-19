from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pandas as pd

import backend # import backend class from backend.py file
import report_GUI # import report GUI class from the report_GUI.py file
import Edit_GUI # import edit GUI class from the Edit_GUI.py file
import delete_GUI # import delete GUI class from the delete_GUI.py file
import insert_GUI # import insert GUI class from the insert_GUI.py file
import tkinter.messagebox as msgBox


class GUI(backend.backend):

    """
    This constructor method to declare the GUI as soon as the object has been declared
    """
    def __init__(self):

        # Root declaration
        self.root = Tk()
        self.root.geometry("1080x720")
        self.root.title("LAB_CLASS")

        # Declare Label Frame
        self.Segment1 = LabelFrame(self.root, text='')
        self.Segment2 = LabelFrame(self.root, text='MENU')

        self.Segment1.pack(fill='both', expand='yes', padx= 10, pady=10)
        self.Segment2.pack(fill='both', expand='yes', padx= 10, pady=10)


        # Declare title
        self.title = Label(self.Segment1, text='Cafe Management', font=('bold', 30))
        self.title.pack(pady=20)


        # Declare Table
        self.orderBox = ttk.Treeview(self.Segment1, columns=(1,2,3,4), show='headings')
        self.orderBox.heading(1, text="ID")
        self.orderBox.heading(2, text="Name")
        self.orderBox.heading(3, text="Available")
        self.orderBox.heading(4, text="Price")
        self.orderBox.pack(side=BOTTOM, pady=100)


        # Declare Button
        self.add_btn = Button(self.Segment2, text='ADD', font=('regular', 18), bg="white", command=self.add)
        self.del_btn = Button(self.Segment2, text='DELETE', font=('regular', 18), bg="white", command=self.delete)
        self.edit_btn = Button(self.Segment2, text='EDIT', font=('regular', 18), bg="white", command=self.edit)
        self.rep_btn = Button(self.Segment2, text='REPORT', font=('regular', 18), bg="white", command=self.report)
        self.ref_btn = Button(self.Segment2, text='REFRESH', font=('regular', 18), bg="white", command=self.refresh_data)
        self.imp_btn = Button(self.Segment2, text='IMPORT', font=('regular', 18), bg="white", command=self.load)

        self.add_btn.pack(side=LEFT, padx=10)
        self.del_btn.pack(side=LEFT, padx=10)
        self.edit_btn.pack(side=RIGHT, padx=10)
        self.rep_btn.pack(side=RIGHT, padx=10)
        self.ref_btn.pack()
        self.imp_btn.pack()

        self.getData()

        self.root.mainloop()


    def load(self):
        filename = filedialog.askopenfilename(initialdir='/home/livevil/Documents/Software Engineering/Lab_Class/', title='Select File', filetypes=(('csv files','*.csv'), ('All files','*.*')))

        id_df = pd.read_csv(f'{filename}', usecols=[0])
        name_df = pd.read_csv(f'{filename}', usecols=[1])
        stock_df = pd.read_csv(f'{filename}', usecols=[2])
        price_df = pd.read_csv(f'{filename}', usecols=[3])

        id = id_df.values.tolist()
        name = name_df.values.tolist()
        stock = stock_df.values.tolist()
        price = price_df.values.tolist()

        for i in range(0, len(id)):
            self.action(f"INSERT INTO product VALUES ({id[i][0]}, '{name[i][0]}', {stock[i][0]}, {price[i][0]})")
        
        self.refresh_data()
        
        return True


    # Delete function for delete button command
    def delete(self):

        # Get the data that selected in the treeview
        selected = self.orderBox.focus()
        val = self.orderBox.item(selected, 'values')

        # Declare delete_GUI object to show the GUI
        delete_GUI.GUI(val)
        
        return True



    # Add function for add button command
    def add(self):

        # Declare insert_GUI object to show the GUI
        insert = insert_GUI.GUI()

        print('Add GUI is opened')


    # Edit function for edit button command
    def edit(self):

        # Get the data that selected in the treeview
        selected = self.orderBox.focus()
        val = self.orderBox.item(selected, 'values')

        # Declare Edit_GUI object to show the GUI
        Edit_GUI.GUI(val)

        print('Edit GUI is opened')





    # Refresh function for update the data in the treeview
    def refresh_data(self):
        x = self.orderBox.get_children()

        if x != '()':
            for child in x:
                self.orderBox.delete(child)

        self.getData()
        print("Record Updated")



    # GetData function to execute select query and gain all data to be returned
    def getData(self):
        value = self.select('SELECT * FROM product')

        for i in value:
            self.orderBox.insert('', 'end', values=i)

        print("Data successfully taken from database")



    # Edit function for edit button command
    def report(self):
        
        # Declare delete_GUI object to show the GUI
        rep = report_GUI.GUI()
        print("Generating Report...")

start = GUI()