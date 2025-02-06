import os
import json
from cryptography.fernet import Fernet
import base64

PASSWORD_FILE = "passwords.json"


def generate_key():
    """Generates a new encryption key and saves it to a file."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """Loads the encryption key from the key.key file."""
    if not os.path.exists("key.key"):
        generate_key() 
    return open("key.key", "rb").read()


def encrypt_password(password, key):
    """Encrypts the password using the Fernet key."""
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password, key):
    """Decrypts the password using the Fernet key."""
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password


def load_passwords():
    """Loads passwords from the JSON file."""
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            try:
                passwords = json.load(file)
            except json.JSONDecodeError:
                passwords = {} 
        return passwords
    else:
        return {}


def save_passwords(passwords):
    """Saves passwords to the JSON file."""
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file)


def add_password(website, password, key):
    """Adds a new password for a given website."""
    passwords = load_passwords()
    encrypted_password = encrypt_password(password, key)
    passwords[website] = encrypted_password.decode()
    save_passwords(passwords)
    print(f"Password for {website} added successfully.")


def get_password(website, key):
    """Retrieves the password for a given website."""
    passwords = load_passwords()
    if website in passwords:
        encrypted_password = passwords[website].encode()
        return decrypt_password(encrypted_password, key)
    else:
        print(f"No password found for {website}")
        return None


def delete_password(website, key, admin_pin):
    """Deletes a password, requiring admin pin for authorization."""
    ADMIN_PIN = "123" 
    if admin_pin == ADMIN_PIN:
        passwords = load_passwords()
        if website in passwords:
            del passwords[website]
            save_passwords(passwords)
            print(f"Password for {website} deleted successfully.")
        else:
            print(f"No password found for {website}")
    else:
        print("Incorrect admin PIN.")


def display_passwords(key):
    """Displays all passwords in alphabetical order."""
    passwords = load_passwords()
    if passwords:
        sorted_websites = sorted(passwords.keys())
        print("\nSaved Passwords:")
        for website in sorted_websites:
            try:
                decrypted_password = get_password(website, key)
                if decrypted_password:
                    print(f"{website}: {decrypted_password}")
            except Exception as e:
                print(f"Error decrypting {website}: {e}")
    else:
        print("No passwords saved yet.")


def main():
    """Main function to run the password manager."""
    if not os.path.exists("key.key"):
        print("Encryption key not found. Generating a new key...")
        generate_key()

    key = load_key()

    while True:
        print("\n--- Password Manager ---")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Display All Passwords")
        print("4. Delete Password")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter website: ")
            password = input("Enter password: ")
            add_password(website, password, key)
        elif choice == "2":
            website = input("Enter website: ")
            password = get_password(website, key)
            if password:
                print(f"Password for {website}: {password}")
        elif choice == "3":
            display_passwords(key)
        elif choice == "4":
            website = input("Enter website to delete: ")
            admin_pin = input("Enter admin PIN: ")
            delete_password(website, key, admin_pin)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
