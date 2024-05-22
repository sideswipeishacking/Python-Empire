import pathlib
import secrets
import os
import base64
import getpass

import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


def generate_salt(size=16):
    """Generate the salt used for key derivation, 
    `size` is the length of the salt to generate"""
    return secrets.token_bytes(size)


def derive_key(salt, password):
    """Derive the key from the `password` using the passed `salt`"""
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())


def generate_key(password, salt=None):
    """Generates a key from a `password` and optional `salt`.
    If `salt` is not provided, a new salt will be generated."""
    if salt is None:
        salt = generate_salt()
    derived_key = derive_key(salt, password)
    return base64.urlsafe_b64encode(derived_key), salt


def encrypt(filename, key):
    """Given a filename (str) and key (bytes), it encrypts the file and writes it"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def encrypt_folder(foldername, key):
    # if it's a folder, encrypt the entire folder (i.e all the containing files)
    for child in pathlib.Path(foldername).glob("*"):
        if child.is_file():
            print(f"[*] Encrypting {child}")
            # encrypt the file
            encrypt(child, key)
        elif child.is_dir():
            # if it's a folder, encrypt the entire folder by calling this function recursively
            encrypt_folder(child, key)


def remove_salt():
    """Remove the salt file"""
    salt_file = pathlib.Path("salt.salt")
    if salt_file.exists():
        salt_file.unlink()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="File Encryptor Script with a Password")
    parser.add_argument("path", help="Path to encrypt, can be a file or an entire folder")
    parser.add_argument("-s", "--salt", help="Provide a salt value for key derivation (optional)")
    # parse the arguments
    args = parser.parse_args()
    # get the password
    password = getpass.getpass("Enter the password for encryption: ")
    # generate the key with or without salt
    if args.salt:
        key, salt = generate_key(password, salt=args.salt.encode())
    else:
        key, salt = generate_key(password)
    # encrypt the file or folder
    if os.path.isfile(args.path):
        # if it is a file, encrypt it
        encrypt(args.path, key)
    elif os.path.isdir(args.path):
        encrypt_folder(args.path, key)
    else:
        raise TypeError("The specified path does not exist.")
    # remove the salt file after encryption
    remove_salt()
