#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    ''' Using ARP(Address Resolution Protocol) 
    request to ask who is the specific IP'''
    # pdst is the IP address module of scapy
    arp_request = scapy.ARP(pdst=ip)

    # Created an ethernet frame
    ''' using Ether means that broadcast message 
    should be sent to all devices'''
    # dst is the DestMACField of the scapy.Ether()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Concatenating the broadcast and arp_request
    # use '/' in scapy to concatenate
    arp_request_broadcast = broadcast/arp_request

    # sending the packets
    # 'srp' package helps us to send and recieve packets for custom Ether functions
    # verbose = False, is gonna help by hiding the default mssg
    answered_list = scapy.srp(arp_request_broadcast,
                              timeout=1, verbose=False)[0]

    clients_list = []
    # Iterating over the answered_list
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n----------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


scan_result = scan("192.168.0.1/24")
print_result(scan_result)
