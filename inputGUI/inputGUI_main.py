import tkinter as tk
from tkinter import *




class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(530,190)
        self.master.maxsize(530,190)
        self.master.title("Check files")
        self.master.configure(bg='#F0F0F0')

        # Frame.grid_rowconfigure((0,1,2), weight=1)
        # Frame.grid_columnconfigure((0,1,2,3), weight=1)

        self.btnBrowse1 = Button(self.master, text='Browse...', width=12)
        self.btnBrowse1.grid(row=0, column=0, padx=(20, 20), pady=(50, 15), sticky=W) # ipadx=(19),
        self.txtBrowse1 = Entry(self.master, text='', width=60)
        self.txtBrowse1.grid(row=0, column=1, columnspan=3, padx=(15, 15), pady=(50, 15), sticky=N+E+W)

        self.btnBrowse2 = Button(self.master, text='Browse...', width=12)
        self.btnBrowse2.grid(row=1, column=0, padx=(20, 20), pady=(0, 15), sticky=W) # ipadx=(19),
        self.txtBrowse1 = Entry(self.master, text='', width=60)
        self.txtBrowse1.grid(row=1, column=1, columnspan=3, padx=(15, 15), pady=(0, 15), sticky=N+E+W)

        self.btnCheck = Button(self.master, text='Check for files...', width=12)
        self.btnCheck.grid(row=2, column=0, padx=(20, 20), ipady=(8), pady=(0, 15), sticky=W)

        self.btnClose = Button(self.master, text='Close Program', width=12)
        self.btnClose.grid(row=2, column=3, ipady=(8), padx=(0,15), pady=(0, 15), sticky=E)







if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()