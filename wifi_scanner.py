import os
import datetime

def scan_wifi():
    """
    Launches airodump-ng to scan nearby Wi-Fi networks and saves results as a CSV.
    """
    cmd  = os.system("clear")
    print("\n=== Wifi Scanner ===")
    print("\nEnter the interface (Default >> wlan0):")
    interface = input(">>> ").strip()
    if interface == "":
        interface = "wlan0"

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"wifi_scan_{timestamp}"  # CSV will be saved as wifi_scan_<timestamp>.csv

    print(f"\n[!] Output will be saved to: {output_file}.csv")
    print(f"[*] Starting airodump-ng on interface: {interface}")
    print("[*] When done scanning, press CTRL+C to stop...\n")

    try:
        os.system("sleep 3")
        command = f"airodump-ng {interface} -M -w {output_file}"
        os.system(command)
    except KeyboardInterrupt:
        print("\n[*] Scan interrupted by user.")
    finally:
        os.system("sleep 2")
        print(f"[*] Scan complete. Results saved as {output_file}.csv in current directory.")
