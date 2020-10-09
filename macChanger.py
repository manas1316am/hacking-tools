#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change it's MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error(
            "[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error(
            "[-] Please specify a new mac address, use --help for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call("ip link set dev " + interface + " down", shell=True)
    subprocess.call("ip link set dev " + interface +
                    " address " + new_mac, shell=True)
    subprocess.call("ip link set dev " + interface + " up", shell=True)


options = get_arguments()
change_mac(options.interface, options.new_mac)

# enp3s0
# 00:11:22:33:44:77
