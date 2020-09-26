# coding=utf-8
# Password generator

# Generates a random password for the user

# Demands:
# Parameters
# [X] Ask the user how long they want their password to be (length)
# [X] Have a mix of upper and lowercase letters, as well as numbers and symbols (charset)
# [] Error if all parameters are "no" - user has to choose at least one!

# Other factors
# [] The password should be a minimum of 6 characters long
# [] Generate a sentence to remember password
# [] Make generate method
# https://dev.to/spaceofmiah/generating-random-password-in-python-practical-guide-amd

# Define function
def get_password_length():
    # Prompt user to enter number of digits in integers
    length = int(input("How many digits do you want your password to be?: "))
    # Returning data, so that it will be possible to user elsewhere
    return int(length)


# Define function
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
    choose_numeric = input("Use numbers? (Yes/No): ")
    choose_symbols = input("Use symbols? (Yes/No): ")

    # If statements = if chosen, then extend charset (chosen charset = [], line 34) with selected charsets (line 28-34)
    # Change any characters the user types to uppercase (.upper), to give user more freedom in reference to characters
    if choose_alphabet_lowercase.upper() == "YES":
        chosen_charset.extend(charset_alphabet_lowercase)
    if choose_alphabet_uppercase.upper() == "YES":
        chosen_charset.extend(charset_alphabet_uppercase)
    if choose_numeric.upper() == "YES":
        chosen_charset.extend(charset_numeric)
    if choose_symbols.upper() == "YES":
        chosen_charset.extend(charset_symbols)

    # Display chosen charsets to user
    print("Chosen charset: ")
    # Print and display the extended list
    print(chosen_charset)


# Call function to run code inside function
get_charset()
