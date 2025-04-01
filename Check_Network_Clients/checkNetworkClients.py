import scapy.all as scapyObject
import socket

def getCurrIpAddress():
    currIp=scapyObject.get_if_addr(scapyObject.conf.iface)
    return currIp

def getCurrIpSubnet(currIp):
    getSubnet=currIp.split(".")
    getSubnet.pop()
    temp='.'.join(getSubnet)
    currIpSubnet=f'{temp}.1/24'
    return currIpSubnet

def arpPingLocalIp(ip_addr):
    result = []
    try:
        arp_result = scapyObject.arping(ip_addr)
        for device in arp_result[0]:
            temp={}
            temp['mac_address']=device[1].hwsrc
            temp['ip_address']=device[1].psrc
            result.append(temp)
        return result
    except:
        return result

def getDeviceDetails(macIpList):
    deviceList = []
    try:
        for device in macIpList:
            hostName, aliases, ipAddresses = socket.gethostbyaddr(device['ip_address'])
            deviceList.append({'ip_address': device['ip_address'], 'mac_address': device['mac_address'], 'name': hostName})
    except socket.herror:
        deviceList.append({'ip_address': device['ip_address'], 'mac_address': device['mac_address'], 'name': 'N/A'})
    return deviceList

def getDeviceNameList():
    print("getting current ip address")
    currIp = getCurrIpAddress()
    print("getting current ip subnet")
    currIpSubnet=getCurrIpSubnet(currIp)
    print(currIpSubnet)
    macIpList = arpPingLocalIp(currIpSubnet)
    return getDeviceDetails(macIpList)

if __name__ == "__main__":
    getDeviceNameList()
    

