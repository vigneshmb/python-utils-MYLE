from pymongo import MongoClient
from datetime import datetime,timezone

uri = "mongodb://localhost:27017/"

def getCurrDateTime():
    current_datetime = datetime.now(timezone.utc)
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

def convertQueryToList(queryResult):
    return list(queryResult)

def getCollection(dbName,collectionName):
    client = MongoClient(uri)
    database = client.get_database(dbName)
    collection = database.get_collection(collectionName)
    return collection


def createData(db,collection,dataArr):
    collectionObj = getCollection(db,collection)
    for data in dataArr:
        data['createdAt']=getCurrDateTime()
    result=collectionObj.insert_many(dataArr)
    return result

def readData(db,collection,queryFilter={}):
    collectionObj = getCollection(db,collection)
    result=collectionObj.find(queryFilter)
    resultData = convertQueryToList(result)
    return resultData

def updateData(db,collection,queryFilter,newData):
    collectionObj = getCollection(db,collection)
    newData["updatedAt"]=getCurrDateTime()
    updateOperation = { '$set' : 
        newData
    }
    result = collectionObj.update_many(queryFilter, updateOperation)
    return result

def deleteData(db,collection,queryFilter):
    collectionObj = getCollection(db,collection)
    result = collectionObj.delete_many(queryFilter)
    return result



if __name__ == "__main__":
    print(createData("python-myle","pymongo-crud",[{"title":"create data 1"}]))
    print(createData("python-myle","pymongo-crud",[{"title":"create data 2"},{"title":"create data 3"}]))
    print(readData("python-myle","pymongo-crud",{"title":"create data 1"}))
    print(updateData("python-myle","pymongo-crud",{"title":"create data 1"},{"title":"create data 12345",}))
    print(deleteData("python-myle","pymongo-crud",{"title":"create data 12345",}))
    print(readData("python-myle","pymongo-crud"))

