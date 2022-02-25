from tkinter import *
from tkinter import ttk
import backend

class GUI(backend.backend):
    def __init__(self, data):

        # Get data from main window
        self.data = data

        # Declare window properties
        self.form = Toplevel()
        self.form.geometry('1080x540')
        self.form.title('DELETE MENU')

        # Declare labelframe
        self.Segment1 = LabelFrame(self.form, text='')
        self.Segment1.pack(fill='both', expand='yes', padx= 10, pady=10)

        # Declare Table
        self.orderBox = ttk.Treeview(self.Segment1, columns=(1,2,3,4), show='headings')
        self.orderBox.heading(1, text="ID")
        self.orderBox.heading(2, text="Name")
        self.orderBox.heading(3, text="Available")
        self.orderBox.heading(4, text="Price")
        self.orderBox.pack(pady=100)

        self.orderBox.insert('', 'end', values=self.data)

        # Declare Label
        self.label = Label(self.Segment1, text='Are you sure want to delete this data?', font=('regular', 18))
        self.label.pack()

        # Declare Button
        self.del_btn = Button(self.Segment1, text='DELETE', font=('regular', 18), bg="white", command=self.delete)
        self.back_btn = Button(self.Segment1, text='BACK', font=('regular', 18), bg="white", command=self.form.destroy)

        self.del_btn.pack(side=RIGHT)
        self.back_btn.pack(side=LEFT)

    # Function to delete the data that has been selected
    def delete(self):
        if(self.action(f"DELETE FROM product WHERE id={self.data[0]}")):
            print("Data has been successfully Deleted from the Database -- ADMIN")

            self.form.destroy()
        else:
            print("Something problem, check with product ID or input data -- ADMIN")
