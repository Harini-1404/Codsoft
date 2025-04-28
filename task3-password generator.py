import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("Error: No character types selected. Cannot generate password.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the password length: "))
            if length <= 0:
                print("Password length must be greater than 0. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nSelect the characters to include in the password:")
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits (0-9)? (y/n): ").lower() == 'y'
    use_special = input("Include special characters (!@#$%^&*)? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)

    if password:
        print("\nGenerated Password:")
        print(password)
    else:
        print("Password could not be generated. Please try again.")

if __name__ == "__main__":
    main()