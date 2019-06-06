import os, datetime

# visit docs.python.org
fpath = 'C:\\Users\\Student\\Desktop\\GitHub\\Python-Exercises\\OS-IO\\TestFiles'
files = os.listdir(fpath)
print()
print('List of all files in path:')
print(files)
print()

print('List of all files with TXT extension:')
print('File\t\t\t\tModified')
print('----\t\t\t\t--------')
for file in files:
    if file.endswith('.txt'):
        # Retrieve file modified date in Unix timestamp
        timestamp = os.path.getmtime(os.path.join(fpath,file))

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


