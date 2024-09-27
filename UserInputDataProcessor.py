def user_name(first_name, last_name):
    
    if len(first_name) <= 2:
            return "Error: Name does not meet requirements."
    elif len(last_name) <= 2:
            return "Error: Name does not meet requirements."
    else:
        return "Name meets name requirements."

while True:
    first_name_input = input("Please enter FIRST name (Must be longer than 2 characters): ")
    last_name_input = input("Please enter LAST name (Must be longer than 2 characters): ")

    result = user_name(first_name_input, last_name_input)
    print(result)

    continue_input = input("Would you like to enter another name? (yes/no): ")
    if continue_input != 'yes':
        break
