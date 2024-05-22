import time
import os
import importlib.util
from colorama import *
from colorama import Fore, Back, Style
import colorama
colorama.init()
if os.name == 'nt':
        os.system('cls')
username = input(Fore.YELLOW + "To continue you will need to enter your USERNAME: " + Fore.RESET)
current_directory = os.path.dirname(os.path.abspath(__file__))
functions_path = current_directory + "\\functions.py"
module_name = 'functions'
spec = importlib.util.spec_from_file_location(module_name, functions_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
import getpass
access_granted = False


module.clear_screen() 
print(Fore.YELLOW + 'Hello, I am Shifter, a digital server of knowledge.')

while True:
    try:
        new = input("Are you a new user? yes/no: ")
    except KeyboardInterrupt:
        module.leave()
    try:
        if new == "no":
            module.clear_screen()
            name = input("What is your name? ")
            if name == "Sideswipe":
                module.clear_screen()
                password = getpass.getpass(prompt='')
                access_granted = module.access(password)
                if access_granted == True:
                    print("!!!Welcome", name ,"to Python Empire!!!")
                    break
                else:
                    continue
            elif module.check_name(name):
                print("Thanks for entering the Shifter Program", name)
                break
            else:
                module.clear_screen()
                print("You are not registered yet!")
                continue
        elif new == "yes":
            if module.new_user() == True:
                module.clear_screen()
                print("Thanks for joining our Shifter Program")
                break
            else:
                module.clear_screen()
                print("You are not a new user/This user already exists. Please pick a new name:")
                continue
    except KeyboardInterrupt:
        module.clear_screen()
        print("You will return to the Homescreen...")
        time.sleep(3)
        module.clear_screen()
        continue


if access_granted == True:
    try:
        while True:
            try:
                def print_with_delay(text, color=Fore.WHITE, delay=0.2):
                    print(color + Style.BRIGHT + text + Style.RESET_ALL)
                    time.sleep(delay)
                def print_tool_info(tool, label):
                    print_with_delay(label, Fore.CYAN)
                    time.sleep(0.5)
                    for t in tool:
                        print_with_delay(t[0], Fore.YELLOW, 0.2)
                print_with_delay("***NOTE: YOU NEED TO ENTER THE LABEL IN () TO ACCESS A TOOL***", Fore.GREEN)
                time.sleep(3)
                print_with_delay("SELF-DESTRUCT SYSTEM = ONLY USE IN EMERGENCY(self_destruct)", Fore.RED)
                print_tool_info([
                    ("- SUBDOMAIN LISTER(subdomain_list)",),
                    ("- REVERSE SHELL SERVER(server_shell)",)
                ], "LISTENERS/LISTERS/SNIFFERS")
                print_tool_info([
                    ("- MAC CHANGER(mac_changer)",),
                    ("- ARP SPOOFER(arp_spoof)",),
                    ("- JAVA SCRIPT INJECTOR(java_inject)",)
                ], "SPOOFER KIT")
                print_tool_info([
                    ("- PDF CRACKER(pdf_cracker)",),
                    ("- ZIP CRACKER(zip_cracker)",),
                    ("- HASH CRACKER(hash_crack)",)
                ], "CRACKERS")
                print_tool_info([
                    ("- REMOTE COMMAND SENDER(remote_commands)",),
                    ("- REVERSE SHELL CLIENT(client_shell)",)
                ], "REMOTE ATTACKS")
                print_tool_info([
                    ("- KEYLOGGER(keylogger)",),
                    ("- BACKDOOR(backdoor) *Coming Soon",),
                    ("- SCREENSHOT(screenshot)",),
                    ("- SHELLCODE EXECUTER(shellcode_exe) *Requires Shellcode ready on a Python Server",)
                ], "IMPLANTS")
                print_tool_info([
                    ("- ENCRYPTING/DECRYPTING(crypting)",),
                    ("- PASSWORD GENERATOR(gen_passwd)",),
                    ("- FILE COPIER(copier)",),
                    ("- BINARY CONVERTER(to_bin)",)
                ], "STANDARD TOOLS")
                print_tool_info([
                    ("- WIFI PASSWORD EXTRACTOR(wifi_extract)",),
                    ("- CHROME COOKIE EXTRACTOR(cookie_extract)",),
                    ("- CHROME PASSWORD EXTRACTOR(passwd_extract)",)
                ], "EXTRACTION TOOLS")
                print_tool_info([
                    ("- EMAIL EXFILTRATION(email_exfil) *Coming Soon",),
                    ("- FILE TRANSFER EXFILTRATION(file_exfil) *Coming Soon",),
                    ("- WEB SERVER EXFILTRATION(web_exfil) *Coming Soon",)
                ], "EXFILTRATION")
                print_tool_info([
                    ("- Process Monitoring(process_mon) *Coming Soon",),
                    ("- Change Monitor(change_mon) *Coming Soon",),
                    ("- Code Injector(code_inject) *Coming Soon",)
                ], "PRIVILEGE ESCALATION")
            except KeyboardInterrupt:
                module.clear_screen()
                print(
                    Fore.GREEN + Style.BRIGHT + "***NOTE: YOU NEED TO ENTER THE LABEL IN () TO ACCESS A TOOL***" + Style.RESET_ALL + "\n" +
                    Fore.RED + Style.BRIGHT + "SELF-DESTRUCT SYSTEM = ONLY USE IN EMERGENCY(self_destruct)" + Style.RESET_ALL + '\n' +
                    Fore.BLUE + Style.BRIGHT + "OSINT: OPEN SOURCE INTELLIGENCE" + Style.RESET_ALL + "\n" +
                    Fore.BLUE + " - SHODAN SEARCH ENGINE(shodan)\n" +
                    " - DNS ENUMERATION(dns_enum)\n" +
                    " - WEB CRAWLER(web_crawl)\n" +
                    " - IP GEOLOCATOR(geoip)\n" +
                    " - METADATA EXTRACTOR(metadata)\n" +
                    Fore.GREEN + Style.BRIGHT + "SCANNERS" + Style.RESET_ALL + "\n" +
                    Fore.GREEN + " - PORT SCANNER(port_scanner)\n" +
                    " - NETWORK SCANNER(network_scan)\n" +
                    " - VULNERABILITY SCANNER(vuln_scan) * Coming Soon\n" +
                    " - SANDBOX SCANNER(sand_scan)\n" +
                    Fore.YELLOW + Style.BRIGHT + "LISTENERS/LISTERS/SNIFFERS" + Style.RESET_ALL + "\n" +
                    Fore.YELLOW + " - SUBDOMAIN LISTER(subdomain_list)\n" +
                    " - REVERSE SHELL SERVER(server_shell)\n" +
                    Fore.MAGENTA + Style.BRIGHT + "SPOOFER KIT" + Style.RESET_ALL + "\n" +
                    Fore.MAGENTA + " - MAC CHANGER(mac_changer)\n" +
                    " - ARP SPOOFER(arp_spoof)\n" +
                    " - JAVA SCRIPT INJECTOR(java_inject)\n" +
                    Fore.CYAN + Style.BRIGHT + "CRACKERS" + Style.RESET_ALL + "\n" +
                    Fore.CYAN + " - PDF CRACKER(pdf_cracker)\n" +
                    " - ZIP CRACKER(zip_cracker)\n" +
                    " - HASH CRACKER(hash_crack)\n" +
                    Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "REMOTE ATTACKS" + Style.RESET_ALL + "\n" +
                    Fore.LIGHTMAGENTA_EX + " - REMOTE COMMAND SENDER(remote_commands)\n" +
                    " - REVERSE SHELL CLIENT(client_shell)\n" +
                    Fore.LIGHTRED_EX + Style.BRIGHT + "IMPLANTS" + Style.RESET_ALL + "\n" +
                    Fore.LIGHTRED_EX + " - KEYLOGGER(keylogger)\n" +
                    " - BACKDOOR(backdoor) *Coming Soon\n" +
                    " - SCREENSHOT(screenshot)\n" +
                    " - SHELLCODE EXECUTER(shellcode_exe) *Requires Shellcode ready on a Python Server\n" +
                    Fore.LIGHTYELLOW_EX + Style.BRIGHT + "STANDARD TOOLS" + Style.RESET_ALL + "\n" +
                    Fore.LIGHTYELLOW_EX + " - ENCRYPTING/DECRYPTING(crypting)\n" +
                    " - PASSWORD GENERATOR(gen_passwd)\n" +
                    " - FILE COPIER(copier)\n" +
                    " - BINARY CONVERTER(to_bin)\n" +
                    Fore.WHITE + Style.BRIGHT + "EXTRACTION TOOLS" + Style.RESET_ALL + "\n" +
                    " - WIFI PASSWORD EXTRACTOR(wifi_extract)\n" +
                    " - CHROME COOKIE EXTRACTOR(cookie_extract)\n" +
                    " - CHROME PASSWORD EXTRACTOR(passwd_extract)" + Fore.RESET + "\n" +
                    Fore.RED + Style.BRIGHT + "EXFILTRATION" + Style.RESET_ALL + "\n" +
                    Fore.RED + " - EMAIL EXFILTRATION(email_exfil) *Coming Soon\n" +
                    " - FILE TRANSFER EXFILTRATION(file_exfil) *Coming Soon\n" +
                    " - WEB SERVER EXFILTRATION(web_exfil) *Coming Soon\n" +
                    Fore.GREEN + Style.BRIGHT + "PRIVILEDGE ESCALATION" + Style.RESET_ALL + "\n" +
                    Fore.GREEN + " - Process Monitoring(process_mon) *Coming Soon\n" +
                    " - Change Monitor(change_mon) *Coming Soon\n" +
                    " - Code Injector(code_inject) *Coming Soon")

            try:
                try:
                    print('\n')
                    choice = input('\033[1m' + "YOUR CHOICE: " + '\033[0m')
                    #continue_ = input('\033[1m' + "Press ENTER to continue: " + '\033[0m')
                except KeyboardInterrupt:
                    module.leave()
                if hasattr(module, choice) and callable(getattr(module, choice)):
                    func_to_call = getattr(module, choice)
                    func_to_call()
            except KeyboardInterrupt:
                module.clear_screen()
                print("Returning to Tool display...")
                time.sleep(3)
                module.clear_screen()
                continue
    except KeyboardInterrupt:
        module.leave()

else:
    try:
        module.clear_screen()
        while True:
            print(Fore.YELLOW + " - IP GEO-LOCATOR(geoip)")
            time.sleep(0.2)
            print(" - PASSWORD GENERATOR(gen_passwd)")
            time.sleep(0.2)
            print(" - FILE COPIER(copier)")
            time.sleep(0.2)
            print(" - METADATA EXTRACTOR(metadata)")
            time.sleep(0.2)
            print(" - BINARY CONVERTER(to_bin)")
            Fore.RESET
            try:
                try:
                    choice = input('\033[1m' + "YOUR CHOICE: " + '\033[0m')
                except KeyboardInterrupt:
                    module.leave()
                if hasattr(module, choice) and callable(getattr(module, choice)):
                    func_to_call = getattr(module, choice)
                    func_to_call()
                else:
                    module.clear_screen()
                    print(Fore.RED + '\033[1m' + "This service is not available!" + '\033[0m')
            except KeyboardInterrupt:
                module.clear_screen()
                print('\033[1m' + "You will return to the Applicationdisplay..." + '\033[0m')
                time.sleep(3)
                module.clear_screen()
    except KeyboardInterrupt:
        module.leave()