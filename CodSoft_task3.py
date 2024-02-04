import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on user preferences
    all_chars = lower_case + upper_case + digits + special_chars

    # Ensure the length is at least 4 to include characters from each set
    length = max(length, 4)

    # Generate password
    password = random.sample(all_chars, length)

    # Convert the list of characters to a string
    password_str = ''.join(password)

    return password_str

def main():
    print("Password Generator")

    try:
        # Prompt the user to specify the desired length of the password
        password_length = int(input("Enter the desired length of the password: "))

        # Generate and display the password
        password = generate_password(password_length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
