import logging
from scapy.all import *

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def process_packet(packet):
    if IP in packet and ICMP in packet:
        print("Source IP: " + packet[IP].src)
        print("Destination IP: " + packet[IP].dst)
        print("Protocol: " + str(packet[IP].proto))
        if Raw in packet:
            print("Payload: " + str(packet[Raw].load))
        print("--------------------------------")

def analyze_cap_file(file_path):
    packets = rdpcap(file_path)

    for packet in packets:
        process_packet(packet)

cap_file_path = "t5.pcap"

analyze_cap_file(cap_file_path)
