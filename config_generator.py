def generate_hostapd_config(interface, ssid, channel=6):
    content = f"""
interface={interface}
driver=nl80211
ssid={ssid}
hw_mode=g
channel={channel}
macaddr_acl=0
ignore_broadcast_ssid=0
"""
    with open('hostapd.conf', 'w') as f:
        f.write(content.strip())

def generate_dnsmasq_config(interface):
    content = f"""
interface={interface}
dhcp-range=10.0.0.10,10.0.0.100,12h
dhcp-option=3,10.0.0.1
dhcp-option=6,8.8.8.8
address=/#/10.0.0.1
"""
    with open('dnsmasq.conf', 'w') as f:
        f.write(content.strip())
