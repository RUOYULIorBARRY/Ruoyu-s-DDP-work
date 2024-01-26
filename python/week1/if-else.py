a = 33.33
b = 4444

# if
if b > a:
    print("b is greater than a")
if b < a:
    print("a is greater than b")

# elif "if the previous conditions were not true, then try this condition".


if a == b:
    print("b and b are equal")
elif a != b:
    print("a and b are not equal!")

# else catches anything which isn't caught by the preceding conditions

if a == b:
    print("a=b")
elif a > b:
    print("a>b")
else:
    print("b is greater than a")


# short hand if and if...else
x = 111
y = 222
print("y<x") if y < x else print("y>x")

q = 1
w = 1
print("A") if q > w else print("=") if q == w else print("B")

# not
a = 55
b = 22
if not a < b:
    print("b is not greater than a")

# nested if
x = 123

if x > 1:
    print(">1")
    if x > 12:
        print(">12")
    else:
        print("not > 123")
