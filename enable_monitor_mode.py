# enable_monitor_mode.py

import subprocess
import re
import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def enable_monitor_mode():
    """
    Prompts user for interface (default wlan0), enables monitor mode,
    and kills interfering processes using airmon-ng.
    """
    clear_screen()
    print("\n=== Configration For Monitor Mode ===")
    print("\nEnter the wireless interface to enable monitor mode (default: wlan0):")
    interface = input("> ").strip() or "wlan0"

    # Optional: Validate interface format
    if not re.match(r'^wlan[0-9]+$', interface):
        print(f"[!] Invalid interface '{interface}'. Please use names like wlan0, wlan1.")
        return None

    try:
        print(f"\n[+] Starting monitor mode on {interface}...")
        subprocess.run(["airmon-ng", "start", interface], check=True)
        print("[+] Monitor mode enabled.")

        print("\n[+] Killing interfering processes...")
        subprocess.run(["airmon-ng", "check", "kill"], check=True)
        print("[+] Interfering processes killed.")

        # Usually monitor interface becomes wlan0mon or wlan1mon
        monitor_interface = interface + "mon"
        print(f"[+] Monitor mode enabled on interface: {monitor_interface}")
        return monitor_interface

    except subprocess.CalledProcessError as e:
        print(f"[!] Error while enabling monitor mode: {e}")
        return None
