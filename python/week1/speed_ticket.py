def speeding_ticket(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return "No Ticket"
    elif speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"


# speed = int(input("Enter your speed (in mph): "))
# is_birthday = input("Is today your birthday (yes/no)?").lower() == 'yes'

# ticket = speeding_ticket(speed, is_birthday)
# print(ticket)

while True:
    user_input = input(
        "Enter your speed (in mph) and if it's your birthday (yes/no), separated by a comma: ")
    if user_input.lower() == 'exit':
        break
    speed_str, birthday_str = user_input.split(',')
    # 当调用 user_input.split(',') 时，方法会在逗号处分割字符串。结果是字符串 "75" 和 " yes" 被分割开，并作为列表的两个元素返回。
    speed = int(speed_str.strip())
    # .strip() 用于移除字符串两端的空白
    is_birthday = birthday_str.strip().lower() == 'yes'
    ticket = speeding_ticket(speed, is_birthday)
    print(ticket)
