import scapy.all as scapyObject

def arpPingLocalIp(ip_addr):
    arp_result = scapyObject.arping(ip_addr)
    for device in arp_result[0]:
        print(device[1].pdst,device[1].src)

if __name__ == "__main__":
    print("getting current ip address")
    currIp=scapyObject.get_if_addr(scapyObject.conf.iface)
    print("getting current ip subnet")
    getSubnet=currIp.split(".")
    getSubnet.pop()
    temp='.'.join(getSubnet)
    currIpSubnet=f'{temp}.1/24'
    print(currIpSubnet)
    arpPingLocalIp(currIpSubnet)