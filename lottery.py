import requests

# 判断是否中大乐透
def DaLeTou(luckNumber:str):
    # 按照空格分解luckNumber为luckNumberList
    luckNumberList = luckNumber.split()
    # luckNumberList中前五个数为红球，后两个数为蓝球，并且对他们进行从小打到排序
    redBallList = luckNumberList[:5]
    blueBallList = luckNumberList[5:]
    # 获取当前日期的大乐透中奖后号码
    DaLeTou_URL = 'https://webapi.sporttery.cn/gateway/lottery/getDigitalDrawInfoV1.qry?param=85,0&isVerify=1'
    res = requests.get(url=DaLeTou_URL)
    DaLeTou_data = res.json()
    res = {
        'drawNumber':DaLeTou_data['value']['dlt']['lotteryDrawResult'],
        'luckNumber':luckNumber
    }
    drawNumberList = DaLeTou_data['value']['dlt']['lotteryDrawResult'].split()
    drawRedBallList =  drawNumberList[:5]
    drawBlueBallList =  drawNumberList[5:]
    # 判断是否中奖 
    # 判断红球中奖个数
    redBallCount = 0
    for i in redBallList:
        if i in drawRedBallList:
            redBallCount += 1
    # 判断蓝球中奖个数
    blueBallCount = 0
    for i in blueBallList:
        if i in drawBlueBallList:
            blueBallCount += 1
    # 判断是否中奖
    if redBallCount == 5 and blueBallCount == 2:
        res['prize'] = '一等奖'
    elif redBallCount == 5 and blueBallCount == 1:
        res['prize'] = '二等奖'
    elif redBallCount == 5 and blueBallCount == 0:
        res['prize'] = '三等奖'
    elif redBallCount == 4 and blueBallCount == 2:
        res['prize'] = '四等奖'
    elif redBallCount == 4 and blueBallCount == 1:
        res['prize'] = '五等奖'
    elif redBallCount == 3 and blueBallCount == 2:
        res['prize'] = '六等奖'
    elif redBallCount == 4 and blueBallCount == 0:
        res['prize'] = '七等奖'
    elif (redBallCount == 2 and blueBallCount == 2) or (redBallCount == 3 and blueBallCount == 1):
        res['prize'] = '八等奖'
    elif (redBallCount == 1 and blueBallCount == 2) or (redBallCount == 2 and blueBallCount == 1) or (redBallCount == 3 and blueBallCount == 0) or (redBallCount == 0 and blueBallCount == 2):
        res['prize'] = '九等奖'
    else:
        res['prize'] = '未中奖'
    return res
    
# 判断是否中双色球
def ShuangSeQiu(luckNumber:str):
    # 按照空格分解luckNumber为luckNumberList
    luckNumberList = luckNumber.split()
    # luckNumberList中前六个数为红球，后一个数为蓝球，并且对他们进行从小打到排序
    redBallList = luckNumberList[:6]
    blueBallList = luckNumberList[6:]
    # 获取当前日期的双色球中奖后号码
    ShuangSeQiu_URL = 'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&pageNo=1&pageSize=30&systemType=PC'
    res = requests.get(url=ShuangSeQiu_URL)
    ShuangSeQiu_data = res.json()
    redBall = ShuangSeQiu_data['result'][0]['red'].replace(',',' ')
    blueBall = ShuangSeQiu_data['result'][0]['blue'].replace(',',' ')
    res = {
        'drawNumber':redBall + " "+blueBall,
        'luckNumber':luckNumber
    }
    drawNumberList = (redBall + " "+blueBall).split()
    drawRedBallList =  drawNumberList[:6]
    drawBlueBallList =  drawNumberList[6:]
    # 判断是否中奖 
    # 判断红球中奖个数
    redBallCount = 0
    for i in redBallList:
        if i in drawRedBallList:
            redBallCount += 1
    # 判断蓝球中奖个数
    blueBallCount = 0
    for i in blueBallList:
        if i in drawBlueBallList:
            blueBallCount += 1
    # 判断是否中奖
    if redBallCount == 6 and blueBallCount == 1:
        res['prize'] = '一等奖'
    elif redBallCount == 6 and blueBallCount == 0:
        res['prize'] = '二等奖'
    elif redBallCount == 5 and blueBallCount == 1:
        res['prize'] = '三等奖'
    elif (redBallCount == 5 and blueBallCount == 0) or (redBallCount == 4 and blueBallCount == 1):
        res['prize'] = '四等奖'
    elif (redBallCount == 4 and blueBallCount == 0) or (redBallCount == 3 and blueBallCount == 1):
        res['prize'] = '五等奖'
    elif (redBallCount == 2 and blueBallCount == 1) or (redBallCount == 1 and blueBallCount == 1) or (redBallCount == 0 and blueBallCount == 1):
        res['prize'] = '六等奖' 
    else:
        res['prize'] = '未中奖'
    return res