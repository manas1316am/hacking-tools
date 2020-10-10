#!/usr/bin/env python

from scapy.all import *


def scan(ip):
    scapy.all.arping(ip)


scan("192.168.0.1/24")
