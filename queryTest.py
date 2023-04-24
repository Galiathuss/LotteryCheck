import httpx

def queryTest(url:str):
    payload={}
    headers = {
    'authority': 'webapi.sporttery.cn',
    'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
    'referer':"https://www.lottery.gov.cn/",
    'origin': 'https://www.lottery.gov.cn',
    }
    isSuccess = False
    count = 0
    while not isSuccess:
        try:
            res = httpx.get(url=url,headers=headers)
            count += 1
            if res.status_code == 200:
                isSuccess = True        
        except httpx.ConnectTimeout :
            isSuccess = False
        except httpx.ReadTimeout :
            isSuccess = False
        except httpx.ConnectError :
            isSuccess = False
        except: 
            isSuccess = False
    return count

print(queryTest('https://webapi.sporttery.cn/gateway/lottery/getDigitalDrawInfoV1.qry?param=85,0&isVerify=1'))