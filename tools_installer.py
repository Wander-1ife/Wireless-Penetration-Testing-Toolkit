import os
import sys
import subprocess
from time import sleep
from typing import Dict, Tuple

# Define tool information with installation commands and descriptions
TOOLS: Dict[int, Tuple[str, str, str, bool]] = {
    1: ("aircrack-ng", 
        "sudo apt install -y aircrack-ng",
        "Wi-Fi WEP/WPA cracking (essential for pentesting)",
        False),
    
    2: ("kismet", 
        "sudo apt install -y kismet",
        "Wireless sniffer with 802.11ax/6E support",
        False),
    
    3: ("wifite2", 
        "git clone --depth 1 https://github.com/derv82/wifite2.git",
        "Automated wireless auditor (WPA3 ready)",
        True),
    
    4: ("mdk3", 
        "sudo apt install -y mdk3",
        "Wi-Fi stress tester",
        False),
    
    5: ("pixiewps", 
        "sudo apt install -y pixiewps",
        "Offline WPS PIN brute-forcer",
        False),
    
    6: ("airgeddon", 
        "git clone --depth 1 https://github.com/v1s1t0r1sh3r3/airgeddon.git && "
        "cd airgeddon && bash airgeddon.sh",
        "Multi-attack GUI platform",
        True),
    
    7: ("bettercap", 
        "sudo apt install -y bettercap",
        "WiFi/Bluetooth MITM framework",
        False),
    
    8: ("zmap", 
        "sudo apt install -y zmap",
        "Internet-scale scanner",
        False),
    
    9: ("ghost-phisher", 
        "sudo apt install -y python3-scapy && "
        "git clone --depth 1 https://github.com/savio-code/ghost-phisher.git",
        "Rogue Access Point creator",
        True),
    
    10: ("scapy", 
        "sudo apt install -y python3-scapy",
        "Packet crafting toolkit",
        False),
    
    11: ("hcxtools", 
        "sudo apt install -y hcxtools",
        "WPA3 hash converter",
        False)
}

# Global variable for installation directory
INSTALL_DIR = ""

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_install_dir():
    """Ask user for installation directory and create it if needed"""
    global INSTALL_DIR
    if not INSTALL_DIR:
        default_dir = os.path.expanduser("~/wireless_tools")
        dir_prompt = input(f"Enter installation directory for Git tools [{default_dir}]: ").strip()
        INSTALL_DIR = dir_prompt if dir_prompt else default_dir
        
        # Create directory if it doesn't exist
        os.makedirs(INSTALL_DIR, exist_ok=True)
        print(f"[*] Git tools will be installed to: {INSTALL_DIR}")
        
        # Add to PATH if not already present
        if INSTALL_DIR not in os.environ["PATH"]:
            os.environ["PATH"] += f":{INSTALL_DIR}"
            with open(os.path.expanduser("~/.bashrc"), "a") as f:
                f.write(f"\nexport PATH=\"$PATH:{INSTALL_DIR}\"\n")
            print(f"[*] Added {INSTALL_DIR} to PATH")
    return INSTALL_DIR

def show_menu():
    """Display the main menu of available tools"""
    clear_screen()
    print("\n=== 2024 Wireless Security Suite ===")
    print("{:<5} {:<15} {}".format("No.", "Tool", "Description"))
    print("-" * 50)
    for key in sorted(TOOLS.keys()):
        name, _, desc, _ = TOOLS[key]
        print("{:<5} {:<15} {}".format(f"{key})", name, desc))
    print("\n0) Install ALL tools")
    print("00) Fix Dependencies")
    print("99) Exit\n")

def run_command(command: str) -> bool:
    """Execute a shell command and return success status"""
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e.stderr.decode().strip()}")
        return False

def install_tool(key: int) -> bool:
    """Install a specific tool"""
    if key not in TOOLS:
        print(f"[!] Invalid tool number: {key}")
        return False

    name, cmd, desc, needs_cd = TOOLS[key]
    print(f"\n[+] Installing {name}...")
    
    original_dir = os.getcwd()
    success = True
    
    try:
        if needs_cd:
            install_dir = get_install_dir()
            os.chdir(install_dir)
        
        for command in cmd.split(" && "):
            if not run_command(command):
                success = False
                break
            sleep(1)  # Prevent race conditions
        
        if success:
            print(f"[✓] {name} installed successfully")
            if needs_cd:
                print(f"    Location: {os.path.join(install_dir, name)}")
        else:
            print(f"[!] Failed to install {name}")
        
        return success
        
    except Exception as e:
        print(f"[!] Error installing {name}: {str(e)}")
        return False
    finally:
        if needs_cd:
            os.chdir(original_dir)

def fix_dependencies() -> bool:
    """Install common dependencies for all tools"""
    print("\n[+] Installing common dependencies...")
    deps = [
        "git", "build-essential", "libpcap-dev", "cmake", 
        "python3-pip", "python3-dev", "libssl-dev", "pkg-config",
        "libtool", "automake", "autoconf"
    ]
    success = run_command(f"sudo apt update && sudo apt install -y {' '.join(deps)}")
    if success:
        print("[✓] Dependencies installed successfully")
    else:
        print("[!] Failed to install dependencies")
    return success

def install_all_tools() -> bool:
    """Install all available tools"""
    print("\n[+] Starting installation of all tools...")
    all_success = True
    for key in sorted(TOOLS.keys()):
        if not install_tool(key):
            all_success = False
    return all_success

def main():
    """Main program loop"""
    if os.geteuid() != 0:
        print("Please run as root!")
        sys.exit(1)
        
    while True:
        show_menu()
        get_install_dir()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "99":
            print("\nExiting...")
            break
        elif choice == "00":
            fix_dependencies()
        elif choice == "0":
            install_all_tools()
        elif choice.isdigit() and int(choice) in TOOLS:
            install_tool(int(choice))
        else:
            print("\n[!] Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)