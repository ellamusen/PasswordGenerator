# coding=utf-8
# Password generator

# Generates a random password for the user

# Define method
def get_password_length():
    # Try to convert length to int
    try:
        # Prompt user to enter number of digits in integers
        length = int(input("How many digits do you want your password to be?: "))
        # Display chosen length and prompt user to confirm
        # str(length) = We are putting an int in a str
        confirmed = input("Confirm length: " + str(length) + " (Yes/No): ")
        # If user doesn't confirm, call method again
        if confirmed.upper() != "YES":
            get_password_length()
        # Returning data, so that it will be possible to use elsewhere
        return int(length)

    # Handle value-error exception
    except ValueError:
        print("Please enter a number")
        get_password_length()


# Define method
def get_charset():
    charset_alphabet_lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                                  "r", "s", "t", "u", "v", "w", "x", "y", "z", "æ", "ø", "å"]  # List
    charset_alphabet_uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                                  "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Æ", "Ø", "Å"]  # List
    charset_numeric = range(0, 10)  # Numbers can be between 0 to 9
    charset_symbols = ["!", "#", "€", "%", "&", '"', "?", "_", "-", "*", ">", "<", "§", "$", ":", ";"]  # List
    chosen_charset = []  # Empty due to lists being inserted in list if chosen (extend function)

    # Prompt user to enter preferences in password as a string
    choose_alphabet_lowercase = str(input("Use lowercase characters? (Yes/No): "))
    choose_alphabet_uppercase = str(input("Use uppercase characters? (Yes/No): "))
    choose_numeric = str(input("Use numbers? (Yes/No): "))
    choose_symbols = str(input("Use symbols? (Yes/No): "))

    # If statements = if chosen, then extend charset (chosen charset = [], line X) with selected charsets (line X-X)
    # Change any characters the user types to uppercase (.upper), to give user more freedom in reference to characters
    if choose_alphabet_lowercase.upper() == "YES":
        chosen_charset.extend(charset_alphabet_lowercase)
    if choose_alphabet_uppercase.upper() == "YES":
        chosen_charset.extend(charset_alphabet_uppercase)
    if choose_numeric.upper() == "YES":
        chosen_charset.extend(charset_numeric)
    if choose_symbols.upper() == "YES":
        chosen_charset.extend(charset_symbols)

    # Display the chosen charsets
    print("You have chosen following")
    print("Lowercase: " + choose_alphabet_lowercase)
    print("Uppercase: " + choose_alphabet_uppercase)
    print("Numeric: " + choose_numeric)
    print("Symbols: " + choose_symbols)
    # Prompt user to confirm chosen charsets
    confirmed = input("Confirm chosen charsets (Yes/No): ")
    # If user doesn't confirm, call method again
    if confirmed.upper() != "YES":
        get_charset()

    # Return charset list
    return chosen_charset


def generator(list, length):  # list, length = parameters
    from random import randint  # randint = function that generates random integer between a and b
    # Randomize charset with length
    password = ""  # Initialize a password / A value-holder for the values generated in the for-loop
    for i in range(length):  # From 0 to password length, do: ...
        randomint = randint(0, len(list)-1)  # Randint generating a random int fra 0 to length of list
        password += str(list[randomint])  # Append generated character to password (value-holder)
    # Return password
    return password


# Call method to run code inside function
length = get_password_length()
charset = get_charset()

# Display the generated password to user  # end="" = remove new line
print("Your password is: ", end="")
# Display the generated password to user
print(generator(charset, length))

