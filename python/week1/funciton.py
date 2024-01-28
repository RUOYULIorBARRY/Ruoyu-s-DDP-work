def my_function():
    print("Hurry up! Finish your assignment")


my_function()


def my_function(name):
    print(name + "Hurry up! Finish your assignment")


my_function(" Barry ")


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Justin", "Bieber")


def my1_function(*ages):
    print("The oldest is " + ages[3])


my1_function("22", "33", "44", "55")


def my2_function(age1, age2, age3):
    print("the youngest child is" + age1)


my2_function(age1=" 12 ", age2=" 13 ", age3=" 14 ")


def my_function(country="China"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(fruits):
    for x in fruits:
        print(x)


fruits = ["apple", "waterlemon", "banana"]
food = ("chikens", "beefs", "porks")
my_function(fruits)
my_function(food)


def my_function(x):
    return 5 * x


print(my_function(4))


def my_function(x, /):
    print(x)


my_function(3)


def my_function(x):
    print(x)


my_function(x=3)


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)
