
def func():
    global x
    print("func begin, x: " + x) #gives error
    x = "end"
    print("func end, x: " + x)


x = "start"
func()



