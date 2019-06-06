'''
Step 103

Drill Description:
For this drill, you will need to write a script that creates a database and adds new data into that database.

Requirements:
Your script will need to use Python 3 and the sqlite3 module.

Your database will require 2 fields, an auto-increment primary integer field and a field with the data type of string.

Your script will need to read from the supplied list of file names at the bottom of this page and determine only the files from the list which ends with a “.txt” file extension.

Next, your script should add those file names from the list ending with “.txt” file extension within your database.

Finally, your script should legibly print the qualifying text files to the console.

Additional Setup Instructions:
The following is the list of file names to use for this drill:

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
'''


import sqlite3

# List of file names with varying extensions
fileList = ['information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']

conn = sqlite3.connect('files.db')
with conn:
    cur = conn.cursor()
    # Delete existing table and create a fresh one
    cur.execute("DROP TABLE IF EXISTS tbl_files")
    cur.execute("CREATE TABLE tbl_files (\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_filename TEXT\
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('files.db')
with conn:
    cur = conn.cursor()
    for file in fileList:
        # Only add files with TXT extension into the database
        if file.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files(col_filename) VALUES (?)", (file,) )  # or [file]
    conn.commit()
conn.close()


# All files in database should be TXT files.  Retrieve all and print to screen
conn = sqlite3.connect('files.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_filename FROM tbl_files")
    txtFiles = cur.fetchall()
    print("\nTXT files retrieved from database:")
    for txtfile in txtFiles:
        print(f"{txtfile[0]}")
    conn.commit()
conn.close()
