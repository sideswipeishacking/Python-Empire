import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

import secrets
import os
import base64
import getpass

username = input("Enter the name of your user: ")

def generate_salt(size=16):
    """Generate the salt used for key derivation,
    `size` is the length of the salt to generate"""
    return secrets.token_bytes(size)


def derive_key(salt, password):
    """Derive the key from the `password` using the passed `salt`"""
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())


def load_salt():
    """Load the salt from salt.salt file"""
    with open("modules/salt.salt", "rb") as salt_file:
        salt = salt_file.read()
    return salt


def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True):
    """
    Generates a key from a `password` and the salt.
    If `load_existing_salt` is True, it'll load the salt from a file
    in the current directory called "salt.salt".
    If `save_salt` is True, then it will generate a new salt
    and save it to "salt.salt"
    """
    if load_existing_salt:
        # Load existing salt
        try:
            salt = load_salt()
        except FileNotFoundError:
            # If the salt file does not exist, generate a new salt and save it
            salt = generate_salt(salt_size)
            with open("salt.salt", "wb") as salt_file:
                salt_file.write(salt)
    elif save_salt:
        # Generate new salt and save it
        salt = generate_salt(salt_size)
        with open(f"C:\\Users\\{username}\\Python Empire\\salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    else:
        # If neither load_existing_salt nor save_salt is True, raise an error
        raise ValueError("Either load_existing_salt or save_salt must be True")

    # Generate the key from the salt and the password
    derived_key = derive_key(salt, password)
    # Encode it using Base 64 and return it
    return base64.urlsafe_b64encode(derived_key)


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and writes it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # Read all file data
        file_data = file.read()
    # Encrypt data
    encrypted_data = f.encrypt(file_data)
    # Write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and writes it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # Read the encrypted data
        encrypted_data = file.read()
    # Decrypt data
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("Invalid password or file corrupted.")
        return
    # Write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("File decrypted successfully")


if __name__ == "__main__":
    file = input("Enter the path of the file to encrypt/decrypt: ")

    password = getpass.getpass("Enter the password: ")

    key = generate_key(password, load_existing_salt=True)

    while True:
        choice = input("Enter 'e' to encrypt or 'd' to decrypt the file: ")

        if choice.lower() == "e":
            encrypt(file, key)
            print("File encrypted successfully.")
            break
        elif choice.lower() == "d":
            decrypt(file, key)
            break
        else:
            print("Invalid choice. Please enter 'e' or 'd'.")

