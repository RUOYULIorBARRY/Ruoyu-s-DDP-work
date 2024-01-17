# It's a game about ages and birth.
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")
age = input("enter your age: ")
age = int(age)
input("Let's play a game")
import datetime
current_year = datetime.datetime.now().year
birth_year = current_year - age
year = input("what's today's year: ")
birth_month = int(input("enter the month you were born (1-12): "))

# 计算出生年份
# 如果出生月份还没到，年龄还没增加，需要额外减一年
if current_month < birth_month:
    birth_year = current_year - age - 1
else:
    birth_year = current_year - age

print(f"Hello {last_name} {first_name}, you are {age} years old, so you were born in {birth_year}.")
