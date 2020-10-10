#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    ''' Using ARP(Address Resolution Protocol) 
    request to ask who is the specific IP'''
    # pdst is the IP address module of scapy
    arp_request = scapy.ARP(pdst=ip)
    # Print the summary of the responce.
    print(arp_request.summary())


scan("192.168.0.1/24")
