import subprocess
import sys
import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_cmd(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"[!] Error: {e.stderr.strip()}")
        sys.exit(1)

def change_mac(interface):
    clear_screen()
    print("=== MAC Changer ===")
    print(f"[*] Bringing down {interface}...")
    run_cmd(f"ip link set {interface} down")

    print(f"[*] Changing MAC address of {interface}...")
    macchange_output = run_cmd(f"macchanger -r {interface}")
    print(macchange_output)

    print(f"[*] Bringing up {interface}...")
    run_cmd(f"ip link set {interface} up")

    print(f"[*] Verifying current MAC address...")
    result = run_cmd(f"macchanger -s {interface}")
    print(result)
