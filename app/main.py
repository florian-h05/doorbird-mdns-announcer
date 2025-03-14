#!/usr/bin/env python3
# Copyright (c) 2024 Florian Hotze under MIT License

""" DoorBird mDNS Announcer """
""" This script can announce a DoorBird video doorbell that is on a different subnet or VLAN, which causes mDNS discovery to fail. """

import argparse
import sys
from time import sleep

from zeroconf import IPVersion, ServiceInfo, InterfaceChoice, Zeroconf, NonUniqueNameException

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--advertise", action="store", 
                        required=True, 
                        help="<Required> Advertise DoorBird device, format is <mac>/<ipv4>")
    parser.add_argument("-i", "--interface", action="append", 
                        help="Interfaces to advertise from given by their IP address(es)")
    args = parser.parse_args()

    [mac, ip] = args.advertise.strip().split("/")
    mac = mac.upper().replace(":", "").strip()
    if len(mac) != 12:
        print("Error: invalid mac")
        sys.exit(1)

    info = ServiceInfo(
        "_axis-video._tcp.local.",
        f"Doorstation - {mac}._axis-video._tcp.local.",
        addresses=[ip],
        port=80,
        weight=0,
        priority=0,
        server=f"bha-{mac}.local",
        properties={
            'macaddress': mac
        }
    )

    zeroconf = Zeroconf(interfaces=args.interface or InterfaceChoice.All, ip_version=IPVersion.V4Only)
    print("Registration of the DoorBird service, press Ctrl-C to exit ...")
    try:
        zeroconf.register_service(info)
    except NonUniqueNameException:
        print("Error: A device with the same name is already registered")
        zeroconf.close()
        sys.exit(1)
    
    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Unregistering ...")
        zeroconf.unregister_service(info)
        zeroconf.close()
