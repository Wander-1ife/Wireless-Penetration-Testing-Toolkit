import subprocess

def start_hostapd():
    return subprocess.Popen(['hostapd', 'hostapd.conf'])

def start_dnsmasq():
    return subprocess.Popen(['dnsmasq', '-C', 'dnsmasq.conf'])

def stop_all():
    subprocess.run(['killall', 'hostapd'])
    subprocess.run(['killall', 'dnsmasq'])
    subprocess.run(['iptables', '--flush'])
    subprocess.run(['sysctl', '-w', 'net.ipv4.ip_forward=0'])
