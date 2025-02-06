# Password Manager

This is a simple console-based password manager written in Python. It uses the `cryptography` library to encrypt passwords before storing them in a JSON file, providing a basic level of security.

## Features

*   **Add Passwords:** Store passwords for different websites.
*   **Get Passwords:** Retrieve stored passwords.
*   **Display All Passwords:** List all stored passwords in alphabetical order by website.
*   **Delete Passwords:** Remove passwords (requires an admin PIN).
*   **Encryption:** Uses Fernet encryption (from the `cryptography` library) to protect stored passwords.
*   **Menu-Driven Interface:** Easy-to-use console menu for navigating the program.

## Prerequisites

*   **Python 3.6+:**  This script requires Python 3.6 or later.
*   **cryptography library:** You need to install the `cryptography` library. You can install it using pip:

    ```
    pip install cryptography
    ```

## Installation

1.  **Clone the Repository (Optional):** If you're using Git, clone the repository to your local machine.  If you're just using the code directly, you can skip this step.

2.  **Install Dependencies:** Make sure you have the `cryptography` library installed. Run the following command in your terminal or command prompt:

    ```
    pip install cryptography
    ```

## Usage

1.  **Run the Script:** Open a terminal or command prompt, navigate to the directory where you saved the `password_manager.py` file, and run the script:

    ```
    python password_manager.py
    ```

2.  **Follow the Menu:** The script will display a menu with the following options:

    *   `1. Add Password`
    *   `2. Get Password`
    *   `3. Display All Passwords`
    *   `4. Delete Password`
    *   `5. Quit`

    Enter the number corresponding to the action you want to perform.

3.  **Adding a Password:**
    *   Select option `1`.
    *   Enter the website name.
    *   Enter the password.
    *   The password will be encrypted and stored.

4.  **Getting a Password:**
    *   Select option `2`.
    *   Enter the website name.
    *   The script will retrieve and decrypt the password (if found).

5.  **Displaying All Passwords:**
    *   Select option `3`.
    *   The script will display all stored passwords, sorted alphabetically by website.

6.  **Deleting a Password:**
    *   Select option `4`.
    *   Enter the website name.
    *   Enter the admin PIN (default: `123`).
    *   The password for the specified website will be deleted (if the PIN is correct).

7.  **Quitting:**
    *   Select option `5`.
    *   The script will exit.

## Security Considerations

*   **Key Storage:** The encryption key is stored in a file named `key.key` in the same directory as the script. **This is not a secure way to store the key in a production environment.** Anyone with access to this file can decrypt your passwords. You should protect this file with appropriate operating system-level security measures (e.g., file permissions). Consider storing the key in a secure hardware device or using a key management system for better security.
*   **Admin PIN:** The admin PIN (used for deleting passwords) is hardcoded in the script.  **Change the default admin PIN** in the `delete_password` function to something more secure.  Ideally, you should store the PIN securely (e.g., hashed with a salt) and require the user to set it up when the password manager is first initialized.
*   **Memory Security:** Be aware that passwords and the encryption key may be present in memory while the program is running. It may be possible for an attacker with access to the system's memory to extract this information.
*   **Vulnerability to Malware:** This password manager is vulnerable to malware that could steal the key file or the password data. You should use appropriate anti-malware software to protect your system.
*   **Simple Encryption:** While Fernet encryption is generally considered strong, this implementation is relatively basic. For very sensitive applications, consider using more advanced security techniques.
*   **No Input Sanitization:** This code does not sanitize user inputs, making it vulnerable to injection attacks (though the impact is limited in this specific application).
*   **Use at Your Own Risk:** This password manager is a learning tool and should not be used to store highly sensitive passwords without carefully considering the security implications.

## Disclaimer

This password manager is provided as-is for educational purposes only. The author is not responsible for any security breaches or data loss resulting from the use of this software. Use it at your own risk. Always prioritize strong security practices when handling sensitive information.
