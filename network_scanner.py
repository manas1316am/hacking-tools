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
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print(unanswered.summary())


scan("192.168.0.1/24")
