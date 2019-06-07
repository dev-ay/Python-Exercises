import tkinter
from tkinter import *

#Page 106
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry(f'{700}x{400}')
        self.master.title('Learning Tkinter')
        self.master.config(bg='#eee')

        self.varFName = StringVar()
        self.varLName = StringVar()

        self.lblFName = Label(self.master, text='First Name: ', font=('Helvetica', 16), fg='black', bg='#eee')
        self.lblFName.grid(row=0,column=0, padx=(30,0), pady=(30,0))
        self.lblLName = Label(self.master, text='Last Name: ', font=('Helvetica', 16), fg='black', bg='#eee')
        self.lblLName.grid(row=1,column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master, text='', font=('Helvetica', 16), fg='black', bg='#eee')
        self.lblDisplay.grid(row=3,column=1, padx=(30,0), pady=(30,0))

        self.txtFName = Entry(self.master, text=self.varFName, font=('Helvetica', 16), fg='black', bg='#fff')
        self.txtFName.grid(row=0,column=1, padx=(30,0), pady=(30,0))
        self.txtLName = Entry(self.master, text=self.varLName, font=('Helvetica', 16), fg='black', bg='#fff')
        self.txtLName.grid(row=1,column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text='Cancel', width=10, height=2, comman=self.cancel)
        self.btnCancel.grid(row=2,column=1, padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text=f"Hello {fn} {ln}!")


    def cancel(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

# #page 104
# # parent class
# class Organism:
#     name = "Unknown"
#     species = "Unknown"
#     legs = None
#     arms = None
#     dna = "Sequence A"
#     origin = "Unknown"
#     carbon_based = True
#
#     def information(self):
#         msg = f"\nName: {self.name}\nSpecies: {self.species}\nLegs: {self.legs}\
#                 \nArms: {self.arms}\nDNA: {self.dna}\nOrigin: {self.origin}\
#                 \nCarbon_Based: {self.carbon_based}"
#         return msg
#
# # child class instance
# class Human(Organism):
#     name = 'MacGuyver'
#     species = "Homosapien"
#     legs = 2
#     arms = 2
#     origin = 'Earth'
#
#     def ingenuity(self):
#         msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
#         return msg
#
# # another child class instance
# class Dog(Organism):
#     name = "Spot"
#     species = "Canine"
#     legs = 4
#     arms = 0
#     dna = "Sequence B"
#     origin = "Earth"
#
#     def bite(self):
#         msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
#         return msg
#
# # another child class instance
# class Bacterium(Organism):
#     name = 'X'
#     species = 'Bacteria'
#     legs = 0
#     arms = 0
#     dna = "Sequence C"
#     origin = 'Mars'
#
#     def replication(self):
#         msg = "\nThe cells begin to divide and multiply into two separate organism!"
#         return msg
#
#
# if __name__ == "__main__":
#     human = Human()
#     print(human.information())
#     print(human.ingenuity())
#
#     dog = Dog()
#     print(dog.information())
#     print(dog.bite())
#
#     bacteria = Bacterium()
#     print(bacteria.information())
#     print(bacteria.replication())




# # page 101
# import sqlite3
# #print(dir(sqlite3))
# #print(help(sqlite3))
#
# conn = sqlite3.connect('test.db')
# with conn:
#     cur = conn.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,\
#         col_fname TEXT,\
#         col_lname TEXT,\
#         col_email TEXT\
#         )")
#
#     conn.commit()
#
# conn.close()
#
# conn = sqlite3.connect('test.db')
#
# def init():
#     with conn:
#         cur = conn.cursor()
#         # cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
#         #             ('Bob', 'Smith','bsmith@gmail.com'))
#         # cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES \
#         #             ('Sarah', 'Johnes','sjones@gmail.com')")
#         # cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES \
#         #             ('Sally', 'May','smay@gmail.com')")
#         cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES \
#                     ('Kevin', 'Bacon','kbacon@rocketmail.com')")
#         conn.commit()
#     conn.close()
#
#
# conn = sqlite3.connect('test.db')
# with conn:
#     cur = conn.cursor()
#     cur.execute("SELECT col_fname,col_lname,col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
#     varPerson = cur.fetchall()
#     for item in varPerson:
#         msg = f"First Name: {item[0]}\nLast Name: {item[1]}\nEmail: {item[2]}"
#         print(msg)
#     conn.commit()
# conn.close()



# # page 99
# import os
# # visit docs.python.org
# fname = 'IOtest.txt'
# fpath = 'C:\\Users\\Student\\Desktop\\TechAcademy\\8b-Python'
#
# totalPath = os.path.join(fpath,fname)
# print(totalPath)

# # page 97 and 98
# import os
# print(dir(os.getcwd()))
# print(os.getcwd())
# print(os.listdir())
# #print(help(open))
#
# def writeData():
#     data = '\nHello World!\n'
#     with open('IOtest.txt', 'a') as f:
#         f.write(data)
#         f.close()
#
# def openFile():
#     with open('IOtest.txt', 'r') as f:
#         data = f.read()
#         print(data)
#         f.close()
#
#
# if __name__ == '__main__':
#     writeData()
#     openFile()




# # page 96
# def getName(name=""):
#     name = askName(name)
#     print("Thank you, welcome {}!".format(name))
#
#
# def askName(name):
#     go = True
#     while go:
#         if name == "":
#             name = input("Please enter your name:\n>>> ")
#             if name != "":
#                 go = False
#
#     return name
#
#
# if __name__ == '__main__':
#     getName()


# page 94
#
# def start(nice=0,mean=0,name=""):
#     # get user's name
#     name = describe_game(name)
#     nice,mean,name = nice_mean(nice,mean,name)
#
# def describe_game(name):
#     '''
#         check if this is a new game or not.
#         If it is new, get the user's name.
#         If it is not a new game, thank the player for
#         playing again and continue with the game
#     '''
#     # meaning, if we do not already have this user's name.
#     # then they are a new player and we need to get their name
#     if name != "":
#         print(f"\nThank you for playing again, {name}")
#     else:
#         stop = True
#         while stop:
#             if name == "":
#                 name = input("\nWhat is your name? \n>>> ").capitalize()
#                 if name != "":
#                     print(f"\nWelcome, {name}")
#                     print("\nIn this game, you will be greated \nby several different people.\nYou can choose to be nice or mean")
#                     print("but at the end of the game your fate\nwill be sealed by your actions.")
#                     stop = False
#     return name
#
# def nice_mean(nice,mean,name):
#     stop = True
#     while stop:
#         show_score(nice,mean,name)
#         pick = input("\nA stranger approaches you for a \nconversation. Will you be nice\nor mean? (N/M)\n>>> ").lower()
#         if pick =="n":
#             print("\nThe stranger walks away smiling...")
#             nice = (nice + 1)
#             stop= False
#         if pick == "m":
#             print("\nThe stranger glares at you \nmenacingly and storms off...")
#             mean = (mean + 1)
#             stop = False
#     score(nice, mean, name) # pass the 3 variables to the score()
#     return
#
# def show_score(nice,mean,name):
#     print(f"\n{name}, your current total: \n({nice}, Nice) and ({mean}, Mean)")
#
# def score(nice,mean,name):
#     # score function is being passed the values stored within the 2 variables
#     if nice>2: # if condition is valid, call win function passing in the variables so it can use them
#         win(nice,mean,name)
#     if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
#         lose(nice,mean,name)
#     else:  # else, call nice_mean function passing in the variables so it can use them
#         nice_mean(nice,mean,name)
#
# def win(nice,mean,name):
#     #Substitute the {} wildcards with our variable values
#     print(f"\nNice job {name}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!")
#     # call again function and pass in our variables
#     again(nice,mean,name)
#
# def lose(nice,mean,name):
#     #Substitute the {} wildcards with our variable values
#     print(f"\nAhhh too bad, game over! \n{name}, you live in a dirty beat-up \nvan by the river, wretched and along!")
#     #call again functio and pass in our variables
#     again(nice,mean,name)
#
# def again(nice,mean,name):
#     stop = True
#     while stop:
#         choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
#         if choice == 'y':
#             stop = False
#             reset(nice,mean,name)
#         if choice == 'n':
#             print("\nOh, so sad, sorry to see you go!")
#             stop = False
#             quit()
#         else:
#             print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")
#
# def reset(nice,mean,name):
#     nice = 0
#     mean = 0
#     #Notice, I do not reset the name variable as that same user has elected to play again
#     start(nice,mean,name)
#
#
#
# if __name__ == "__main__":
#     start()





# # page 93
# def start():
#     fname = "Sarah"
#     lname = "Connor"
#     age = 28
#     gender = "Female"
#     get_info(fname,lname,age,gender)
#     # print(f"Hello {get_name()}!")
#
# def get_info(fname, lname, age, gender):
#     print(f"My name is {fname} {lname}. I am {age} year-old {gender}.")
#
# def get_name():
#     name = input("What is your name?  ")
#     return name
#
# if __name__ == "__main__":
#     start()


# # page 89 and 90
# def getInfo():
#     var1 = input("Please provide the first numeric value: ")
#     var2 = input("Please provide the second numeric value: ")
#     return var1,var2
#
# def compute():
#     go = True
#     while go:
#         var1, var2 = getInfo()
#         try:
#             var3 = int(var1) + int(var2)
#             print("{} + {} = {}".format(var1, var2, var3))
#             go = False
#         except ValueError as e:
#             print("{}: \n\nYou did not provide a numaric value!".format(e))
#         except:
#             print("\n\nOops, you provided an invalid input, program will close now!")
#
# if __name__ == "__main__":
#     compute()



# # page 87
# def print_app():
#     name = (__name__) # gets the name of the class
#     return name
# print(print_app())




# # page 85
# # Save a file by a class name, import the file name, and access by the file name
#
# import math
#
# def getNumbers(num1, num2):
#     results = num1 * num2
#     print('test')
#     return results
#
# getNumbers(3,5)
#
# if __name__ == '__main__':
#     pass


# # page 83
# # commenting
# """ Long form commenting
#     multi-line commenting
# """
#
# def printMe():
#     '''This is the description for printMe'''
#
# print(printMe.__doc__)
#
# help(printMe)


# # page 81
# fName = input("What is your \"first name\"?\n>>> ")
# lName = input("What is your \"last name\"?\n>>> ")
# print("{} {}, welcome to python!".format(fName, lName))


# # page 77
# mySentence = 'loves the color'
# color_list = ['red','blue','green','pink','teal','black']
# def color_function(name):
#     lst = []
#     for color in color_list:
#         msg = "{} {} {}".format(name, mySentence,color)
#         lst.append(msg)
#     return lst
#
# for sentence in color_function('Bob'):
#     print(sentence)


# # page 76
# mySentence = 'I love the color'
# color_list = ['red','blue','green','pink','teal','black']
# def color_function():
#     for color in color_list:
#         print("{} {}".format(mySentence,color) )
#
# color_function()


# # page 68
# myList = ('Pink','Black','Green','Teal','Red','Blue')
# for color in myList:
#     if color == 'Black':
#         print('The chosen color is Green.')


# # page 67
# mySentence = 'loves the color'
# color_list = ['red','blue','green','pink','teal','black']
#
# def color_function(name):
#     lst = []
#     for i in color_list:
#         msg = "{0} {1} {2}".format(name,mySentence,i)
#         lst.append(msg)
#     return lst
#
# def get_name():
#     go = True
#     while go:
#         name = input('What is your name?  ')
#         if name.strip() == '':
#             print('You need to provide a name:  ')
#         elif name.lower() == 'sally':
#             print('Sally you may not use this software ;P')
#         else:
#             go = False
#     lst = color_function(name)
#     for i in lst:
#         print(i)
#
# get_name()




# # page 66
# x = 12
# key = False
# if x == 12:
#     if key:
#         print("x is equal to 12 and they have the key!")
#     else:
#         print('x is equal to 12 and they DO NOT have the key!')
# elif x < 12:
#     print('x is less than 12')
# else:
#     print("x is greater than 12")


# # page 65
# for i in range(10):
#     print(i)
#
# j = 0
# while j < 10:
#     print(j)
#     j += 1

# # page 63
# answer = True



# # page 62
# dict = {'index1': 1, 'index2': 2, 'index3':355}
# print(dict)
# print(dict['index2'])
#
# users = { 'employee1': {'fname':'Bob','lname':'Smith','phone':'123-456-7890'} , 'employee2': {'fname':'Mary','lname':'Jones','phone':'152-364-5764'}}
# print(users['employee2'])
# print(users['employee2']['phone'])
#
# print('User: {} {}\nPhone: {}'.format(users['employee2']['fname'],users['employee2']['lname'],users['employee2']['phone']) )


# # --------Drill 60---------
# lang = [ 'python', 'c#', 'c++', 'javascript', 'html', 'css' ]
# lang.insert(0,'java')
# lang.remove('html')
# lang.append('spl')
# print(lang)
# print(lang[ lang.index('python') ].upper() )


# List = [2,3,4]
# List.append(5)
# print(len(List))
# print()
# for i in List:
#     print(i)
# print()
# print(List[2])



# str = "Hello World!"
# for i in enumerate(str):
#     print(i)





# num1 = "1"
# print(type(num1))
# num2 = 2
# print(type(num2))
# print(int(num1) + num2)




# str = "Hello World!"
# len(str)
# str[0]
# str[1]
# str[12]
# str[11]
# print(str + " and " + str)
# print("{} and {}".format(str, str))



# for x in range(9, 10):
#     print(x)



# string = "Hello World"
# for x in string:
#     print(x)



# def myName():
#     print("Hello World!")
#     print()




# a = 'eat'
# b = 'sleep'
# c = 'code'
# alive = True
#
# for x in range(5):
#     print("{}, {}, {}".format(a, b, c))



