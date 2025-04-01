import speedtest

def getSpeedValues():
    spdTestObj = speedtest.Speedtest(secure=True)
    spdTestObj.get_best_server()
    spdTestObj.download()
    spdTestObj.upload()
    result = spdTestObj.results.dict()

    return result


if __name__ == "__main__":
    print(getSpeedValues())