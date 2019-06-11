import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os, datetime
import shutil
import sqlite3

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        # self.master.minsize(600,400)
        # self.master.maxsize(600,400)
        geo = center_window(self, 615, 365)
        self.master.geometry(geo)
        #self.master.geometry(f'{615}x{365}')
        self.master.resizable(width=False, height=False)
        self.master.title("Move TXT Files from Source to Destination:")
        self.master.configure(bg='#F0F0F0')

        description = "This utility will move any '.txt' files from the Source directory to the Destination directory,\
\nand record each transaction to the database 'txtFiles.db' as well as print to console."

        self.lblDescription = Label(self.master, text=description, anchor='center')
        self.lblDescription.grid(row=0, column=0, columnspan=4, padx=(20, 20), pady=(30, 15))

        self.lblSource = Label(self.master, font='Helvetica 10 bold', text="Source Directory:")
        self.lblSource.grid(row=1, column=0, columnspan=2, padx=(20, 20), pady=(0, 15), sticky=N+W)
        self.btnBrowse1 = Button(self.master, text='Browse...', width=12, command=lambda: chooseSource(self))
        self.btnBrowse1.grid(row=2, column=0, padx=(20, 20), pady=(10, 15), sticky=W)
        self.txtBrowse1 = Entry(self.master, text='', width=75)
        self.txtBrowse1.grid(row=2, column=1, columnspan=3, padx=(0, 15), pady=(10, 15), sticky=N+E+W)

        self.btnBrowse1 = Button(self.master, text='<swap>', width=12, command=lambda: swap(self))
        self.btnBrowse1.grid(row=3, column=3, padx=(20, 20), pady=(0, 0), sticky=S+E)

        self.lblDestination = Label(self.master, font='Helvetica 10 bold', text="Destination Directory:")
        self.lblDestination.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(0, 15), sticky=N+W)
        self.btnBrowse2 = Button(self.master, text='Browse...', width=12, command=lambda: chooseDestination(self))
        self.btnBrowse2.grid(row=5, column=0, padx=(20, 20), pady=(10, 15), sticky=W)
        self.txtBrowse2 = Entry(self.master, text='', width=75)
        self.txtBrowse2.grid(row=5, column=1, columnspan=3, padx=(0, 15), pady=(10, 15), sticky=N+E+W)

        self.btnBrowse2 = Button(self.master, text='Find and Move', width=12, command=lambda: moveTXT(self))
        self.btnBrowse2.grid(row=6, column=3, ipadx=(10), padx=(15, 15), ipady=(10), pady=(15, 15), sticky=E)

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))

    centerGeo = self.master.geometry(f'{w}x{h}+{x}+{y}')
    return centerGeo

def chooseSource(self):
    directory = filedialog.askdirectory()
    self.txtBrowse1.delete(0,END)
    self.txtBrowse1.insert(0,directory)

def chooseDestination(self):
    directory = filedialog.askdirectory()
    self.txtBrowse2.delete(0,END)
    self.txtBrowse2.insert(0,directory)

def swap(self):
    temp = self.txtBrowse1.get()
    self.txtBrowse1.delete(0,END)
    self.txtBrowse1.insert(0,self.txtBrowse2.get())
    self.txtBrowse2.delete(0,END)
    self.txtBrowse2.insert(0,temp)

def moveTXT(self):
    source = self.txtBrowse1.get()
    destination = self.txtBrowse2.get()
    #print(f'{source} and {destination}')
    files = os.listdir(source)

    conn = sqlite3.connect('txtFiles.db')
    with conn:
        cur = conn.cursor()
        # Delete existing table and create a fresh one
        #cur.execute("DROP TABLE IF EXISTS tbl_files")
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files (\
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            col_filename TEXT, \
            col_modDate TEXT, \
            col_srcDir TEXT, \
            col_dstDir TXT \
            )")
        conn.commit()
    conn.close()

    print("\nMoving '.txt' Files ...")
    print(f'     SOURCE: {source}')
    print(f'DESTINATION: {destination}')
    print('\nFile\t\t\t\tModified')
    print('----\t\t\t\t--------')

    for file in files:
        if file.endswith('.txt'):
            # Retrieve file modified date in Unix timestamp
            timestamp = os.path.getmtime(os.path.join(source, file))

            # Convert timestamp to datetime object
            date = datetime.datetime.utcfromtimestamp(timestamp)

            # Calculate timezone offset on current system
            offset = datetime.datetime.utcnow() - datetime.datetime.now()

            # Adjust date for timezone
            date -= offset
            # date -= datetime.timedelta(hours=7) #manually offsets by 7 hours

            # Convert date to human readable format
            date = date.strftime('%Y-%m-%d %I:%M:%S %p')

            print(f'{file}\t\t\t{date}')

            conn = sqlite3.connect('txtFiles.db')
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(col_filename, col_modDate, col_srcDir, col_dstDir) VALUES \
                    (?,?,?,?)", (file,date,source,destination))  # or [file]
                conn.commit()
            conn.close()

            shutil.move(os.path.join(source, file), os.path.join(destination, file))

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()