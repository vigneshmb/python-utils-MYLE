from MongoDB_Operations.mongoDbCRUD import createData,getCurrDateTime
from Check_Network_Clients.checkNetworkClients import getDeviceNameList
from Check_Network_Speed.checkNetworkSpeed import getSpeedValues

if __name__ == "__main__":
    networkClients=getDeviceNameList()
    createData('python-myle','network-clients',networkClients)
    networkSpeedData=[]
    networkSpeedData.append(getSpeedValues())
    createData('python-myle','network-speed-test',networkSpeedData)
