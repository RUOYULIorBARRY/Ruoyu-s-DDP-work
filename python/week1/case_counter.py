def case_counter(text):
    upper_count = 0  # Initialization
    lower_count = 0

    for char in text:
        if char.isalpha():  # isalpha() is used to check if includes alphabet
            if char.isupper():  # Check whether it's uppercase or lowercase
                upper_count += 1
            elif char.islower():
                lower_count += 1
    return upper_count, lower_count


while True:  # use while can make the programme continue
    text = input("Enter text: ")
    result = case_counter(text)
    print(f"Upper case count: {result[0]}, Lower case count: {result[1]}")
