import subprocess

def setup_interface(interface='wlan0'):
    subprocess.run(['ifconfig', interface, 'up', '10.0.0.1', 'netmask', '255.255.255.0'])

def enable_ip_forwarding():
    subprocess.run(['sysctl', '-w', 'net.ipv4.ip_forward=1'])

def setup_iptables(wifi_iface='wlan0', net_iface='eth0'):
    subprocess.run(['iptables', '--flush'])
    subprocess.run(['iptables', '--table', 'nat', '--flush'])
    subprocess.run(['iptables', '--delete-chain'])
    subprocess.run(['iptables', '--table', 'nat', '--delete-chain'])

    # NAT: Share internet from eth0 to wlan0
    subprocess.run(['iptables', '-t', 'nat', '-A', 'POSTROUTING', '-o', net_iface, '-j', 'MASQUERADE'])
    subprocess.run(['iptables', '-A', 'FORWARD', '-i', net_iface, '-o', wifi_iface, '-m', 'state', '--state', 'RELATED,ESTABLISHED', '-j', 'ACCEPT'])
    subprocess.run(['iptables', '-A', 'FORWARD', '-i', wifi_iface, '-o', net_iface, '-j', 'ACCEPT'])

    # Ensure IP forwarding is on (again, for good measure)
    subprocess.run(['sysctl', '-w', 'net.ipv4.ip_forward=1'])
