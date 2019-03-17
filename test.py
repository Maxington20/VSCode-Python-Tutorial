import math
import random
import time
import calendar

print ("Hello, Python!")

list1 = ['Kim', 'Max', 'Carl', 'Sheila']

print(list1[:1])

dict1 = {1 : 'Kevin', 2: 'Kim', 3: 'Jeff'}

print(type(dict1))

print(len(dict1))

print(dict1.values())

print(math.sqrt(35))

print(random.choice(list1))

print(1 in list1)

print(1 not in list1)

print("""This is a string that will span on for muliple 
    lines and whatnot, just as a means of pissing off my beautiful
    fiance Kimberly Jane""")

name = "max"
uppername = name.capitalize()

print(uppername)

print(uppername.islower())

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

print(time.localtime())

localtime = time.localtime(time.time())

print("The local time is ", localtime)

localtime = time.asctime(time.localtime(time.time()) )
print("Local current time is: ", localtime)

# creates a var called cal containing a monthly calendar for the month of November 2018 
cal = calendar.month(2018, 11)
print(cal)

def printme( str ):
    print (str)
    return

printme("I hate hearing about wedding venues")
printme("What the fuck is up?!?!?!?")

def changeme( mylist ):
    print ("Values inside the function before change: ",mylist)

    mylist[2]=50
    print ("Values inside the function after changes: ", mylist)
    return

mylist = [10,20,30]
changeme( mylist )
print("Value outside the function: ", mylist)


def changeme2( mylist ):
    mylist = [1,2,3,4]
    print("Value inside the function: ", mylist)
    return

mylist = [10,20,30]
changeme2(mylist)
print ("Values outside the function: ",mylist)


#lamba expression
sum = lambda arg1, arg2: arg1 + arg2 

print("Value of total", sum(1,2,))

def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
if __name__ == "__main__":
    f = fib(100)
    print(f)

Money = 2000
def AddMoney():
    global Money
    Money = Money + 1

print(Money)
AddMoney()
print(Money)

#dir will give you all of the names defined by a module
content= dir(math)
print(content)