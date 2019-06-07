import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

import phonebook_main
import phonebook_gui


def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (w/2))

    centerGeo = self.master.geometry(f'{w}x{h}+{x}+{y}')
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)


#=====================================================================

def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_phonebook( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_fname TEXT, \
                    col_lname TEXT, \
                    col_fullname TEXT, \
                    col_phone TEXT, \
                    col_email TEXT \
                    );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("INSERT INTO tbl_phonebook(col_fname, col_lname, col_fullname, col_phone, col_email) \
                VALUES (?,?,?,?,?)", data)
        conn.commit()
    conn.close()

def count_records(cur):
    #count = ""
    cur.execute("SELECT COUNT(*) FROM tbl_phonebook")
    count = cur.fetchone()[0]
    return cur, count

def onSelect(self, event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullName = (?)", [value])
        varBody = cur.fetchall()

        for data in varBody:
            self.txt_fname.delete(0, END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0, END)
            self.txt_lname.insert(0, data[1])
            self.txt_phone.delete(0, END)
            self.txt_phone.insert(0, data[2])
            self.txt_email.delete(0, END)
            self.txt_email.insert(0, data[3])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()

    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = (f"{var_fname} {var_lname}")
    print(f"var_fullname: {var_fullname}")
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format!!!")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            cur.execute(f"SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{var_fullname}'")
            count = cur.fetchone()[0]
            chkName = count
            if chkName == 0:
                print(f"chkName: {chkName}")
                cur.execute("INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) \
                            VALUES (?,?,?,?,?)", (var_fname, var_lname, var_fullname, var_phone, var_email))
                self.lstList1.insert(END, var_fullname)
                onClear(self)
            else:
                messagebox.showerror("Name Error", f"'{var_fullname}' already exists in the database! Please choose a different name.")
                #onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error", "Please ensure that there is data in all four fields.")


def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM tbl_phonebook")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel(f"Delete Confirmation", f"All information associated with ({var_select}) \
                    \n will be permenantly deleted from the database. \n\nProceed with the deletion request?")
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute(f"DELETE FROM tbl_phonebook WHERE col_fullname = '{var_select}'")
                onDeleted(self)
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", f"{var_select} is the last record in the database and \
            cannot be deleted at this time. \n\nPlease add another record first before you can delete {var_select}.")
    conn.close()


def onDeleted(self):
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)

def onRefresh(self):
    self.lstList1.delete(0, END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM tbl_phonebook")
        count = cur.fetchone()[0]
        print(f'Count: {count}')
        i = 0
        while i < count:
            print(f'i: {i}')
            cur.execute("SELECT col_fullname FROM tbl_phonebook")
            varList = cur.fetchall()[i]
            print(varList)
            for item in varList:
                self.lstList1.insert(0, str(item))
                i = i+1
    conn.close()



def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0]
        var_value = self.lstList1.get(var_select)
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return

    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if(len(var_phone) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()

            cur.execute(f"SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{var_phone}'")
            count = cur.fetchone()[0]
            print(count)
            cur.execute(f"SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{var_email}'")
            count2 = cur.fetchone()[0]
            print(count2)
            if count ==0 or count2 == 0:
                response = messagebox.askokcancel("Update Request", f"The following changes ({var_phone}) and \
                    ({var_email}) will be implemented for ({var_value}).\n\nProceed with the update request?")
                print(response)
                if response:
                    with conn:
                        cur = conn.cursor()
                        cur.execute(f"UPDATE tbl_phonebook SET col_phone = '{var_phone}', \
                                    col_email = '{var_email}' WHERE col_fullname = '{var_value}'")
                        onClear(self)
                        conn.commmit()
                else:
                    messagebox.showinfo("Cancel Request", f"No changes have been made to {var_value}")
            else:
                messagebox.showinfo("No changes detected", f"No changes have been made to {var_value}")
            onClear(self)
        conn.close()
    else:
        messagebox.showerror('Missing information', f"Please select a name from the list. \
            \nThen edit the phone or email information.")
    onClear(self)





if __name__ == "__main__":
    pass





















