
# page 89 and 90
def getInfo():
    var1 = input("Please provide the first numeric value: ")
    var2 = input("Please provide the second numeric value: ")
    return var1,var2

def compute():
    go = True
    while go:
        var1, var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            print("{} + {} = {}".format(var1, var2, var3))
            go = False
        except ValueError as e:
            print("{}: \n\nYou did not provide a numaric value!".format(e))
        except:
            print("\n\nOops, you provided an invalid input, program will close now!")

if __name__ == "__main__":
    compute()



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



