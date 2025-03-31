import scapy.all as scapyObject

def currIpAddress():
    currIp=scapyObject.get_if_addr(scapyObject.conf.iface)
    return currIp

def currIpSubnet(currIp):
    getSubnet=currIp.split(".")
    getSubnet.pop()
    temp='.'.join(getSubnet)
    currIpSubnet=f'{temp}.1/24'
    return currIpSubnet


def arpPingLocalIp(ip_addr):
    arp_result = scapyObject.arping(ip_addr)
    result = []
    for device in arp_result[0]:
        temp={}
        temp['mac_address']=device[1].src
        temp['ip_address']=device[1].pdst
        result.append(temp)
    return result


if __name__ == "__main__":
    print("getting current ip address")
    currIp = currIpAddress()
    print("getting current ip subnet")
    currIpSubnet=currIpSubnet(currIp)
    print(currIpSubnet)
    print(arpPingLocalIp(currIpSubnet))
    scapyObject.conf.ifaces.show(True)  # type: ignore
