import tkinter as tk
from tkinter import *
from tkinter import filedialog



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(600,100)
        self.master.maxsize(600,100)
        self.master.title("Select Directory")
        self.master.configure(bg='#F0F0F0')


        self.btnBrowse = Button(self.master, text='Browse...', width=12, command=lambda: chooseDirectory(self))
        self.btnBrowse.grid(row=0, column=0, padx=(20, 20), pady=(35, 15), sticky=W) # ipadx=(19),
        self.txtBrowse = Entry(self.master, text='', width=70)
        self.txtBrowse.grid(row=0, column=1, columnspan=3, padx=(10, 15), pady=(35, 15), sticky=N+E+W)




def chooseDirectory(self):
    directory = filedialog.askdirectory()
    self.txtBrowse.delete(0,END)
    self.txtBrowse.insert(0,directory)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()