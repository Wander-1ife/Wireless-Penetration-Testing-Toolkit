import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def disable_monitor_mode():
    """
    Stops monitor mode on a given wireless interface and restarts network-manager.
    Returns True if the command was executed, False otherwise.
    """
    clear_screen()
    print("\n=== Disable Monitor Mode ===")
    print("\nEnter the interface to stop monitor mode (Default: wlan0/wlan0mon):")
    interface = input("> ")

    if not interface:
        print("[✗] No interface provided. Skipping...")
        return False

    command = f"airmon-ng stop {interface}"
    result = os.system(command)
    command= "systemctl restart NetworkManager"
    result = os.system(command)
    
    return result == 0
