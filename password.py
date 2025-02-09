import string
import random

def password_generator(length, complexity, specific_chars, meaningful, personal_info):
    # complexity of password
    if complexity == 'easy':
        characters = string.ascii_lowercase
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    else: # hard
        characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    if meaningful == 'no':
        password = ''.join(random.choice(characters) for i in range(length - len(specific_chars)))
    else:
        password = personal_info
    
    # Put specific characters at random positions
    for char in specific_chars:
        pos = random.randint(0, len(password))
        password = password[:pos] + char + password[pos:]
    
    # Make sure password meets the specified length
    if len(password) < length:
        password += ''.join(random.choice(characters) for i in range(length - len(password)))
    
    return password

def main():
    try:
        # take input length of the password
        length = int(input("Enter the desired length of the password: "))
        # Ensure the length is a positive number
        if length <= 0:
            raise ValueError("Length must be a positive number.")

        # take input complexity level of the password
        complexity = input("Enter the complexity level (easy, medium, hard): ").lower()
        if complexity not in ['easy', 'medium', 'hard']:
            raise ValueError("Complexity must be 'easy', 'medium', or 'hard'.")

        # Prompt the user to specify whether the password should be meaningful or random
        meaningful = input("Should the password be meaningful (yes/no)? ").lower()
        if meaningful not in ['yes', 'no']:
            raise ValueError("Meaningful option must be 'yes' or 'no'.")

        # If the password should be meaningful, prompt the user to enter personal information
        if meaningful == 'yes':
            personal_info = input("Enter your name, birthdate, or any personal information to include in the password: ")
            if not personal_info:
                raise ValueError("Personal information cannot be empty when password is meaningful.")
        else:
            personal_info = ''

        # Prompt the user to specify any specific characters to include in the password
        specific_chars = input("Enter any specific characters to include in the password (or leave blank for none): ")

        # Generate the password
        password = password_generator(length, complexity, specific_chars, meaningful, personal_info)
        # Display the generated password
        print("Generated Password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
