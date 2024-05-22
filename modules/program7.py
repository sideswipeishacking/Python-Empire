from pikepdf import _qpdf
import pikepdf
from tqdm import tqdm

username = input("Enter the name of your user: ")

passwords = [line.strip() for line in open("C:\\Users\\" + username + "\\Python Empire\\Exports\\list.txt", encoding="latin-1")]
file = input("Enter the PDF to Crack: ")

for password in tqdm(passwords, "Decrypting PDF"):
    try:
        with pikepdf.open(file, password=password) as pdf:
            print("[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        continue