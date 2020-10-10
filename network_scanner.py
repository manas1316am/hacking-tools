#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    ''' Using ARP(Address Resolution Protocol) 
    request to ask who is the specific IP'''
    # pdst is the IP address module of scapy
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()

    # Created an ethernet frame
    ''' using Ether means that broadcast message 
    should be sent to all devices'''
    # dst is the DestMACField of the scapy.Ether()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()

    # Concatenating the broadcast and arp_request
    # use '/' in scapy to concatenate
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()


scan("192.168.0.1/24")
