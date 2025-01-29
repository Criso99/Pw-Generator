import secrets
import string
import os

def generate_password(length=12):
    """Generates a secure password with a default or provided length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def clear_screen():
    """Function to clear the screen in a portable way."""
    print("\033c", end="")  # ANSI escape sequence to clear the screen

def save_passwords_to_file(filename, num_passwords, password_length=12):
    """Generates a specified number of passwords and saves them in a text file inside the PwList folder."""
    # Create the 'PwList' folder if it doesn't exist
    folder = "PwList"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Full file path
    file_path = os.path.join(folder, filename)
    
    with open(file_path, 'w') as file:
        for _ in range(num_passwords):
            password = generate_password(password_length)
            file.write(password + '\n')
    print(f"The {num_passwords} passwords have been saved in the file '{file_path}'.")

def main():
    """Main function to handle user interaction."""
    while True:
        command = input("Type 'next' to generate a new password, 'file' to save multiple passwords to a file, or 'exit' to quit: ").strip().lower()
        
        if command == "next":
            clear_screen()  # Clears the screen
            password = generate_password(12)
            print("Your newly generated password is:", password)
        elif command == "file":
            filename = input("Enter the filename to save the passwords (e.g., 'passwords.txt'): ").strip()
            num_passwords = int(input("How many passwords do you want to generate? ").strip())
            password_length = int(input("What should be the length of the passwords? ").strip())
            save_passwords_to_file(filename, num_passwords, password_length)
        elif command == "exit":
            print("Exiting the program.")
            break
        else:
            print("Unrecognized command. Type 'next', 'file', or 'exit'.")

if __name__ == "__main__":
    main()
