from fastapi import FastAPI, Request, Form, param_functions, status, Header
from fastapi.responses import JSONResponse
from fastapi.params import Body
from lottery import DaLeTou, ShuangSeQiu
import os,uvicorn

# 创建一个服务，把当前这个python文件当做一个服务　
env = os.getenv('env')
if env != 'DEV':
    app = FastAPI(title=' Web支付接口', version='1.0',
                  docs_url=None, redoc_url=None)
else:
    app = FastAPI(title='Web支付接口', version='1.0')

# 使用get的方法实现查询大乐透的查询
@app.get('/DaLeTou_query/{luckNumber}')
async def DaLeTou_query(luckNumber:str):
    print(luckNumber)
    res = DaLeTou(luckNumber)
    return res

# 使用GET的方法实现查询双色球的查询
@app.get('/ShuangSeQiu_query/{luckNumber}')
async def ShuangSeQiu_query(luckNumber:str):
    res = ShuangSeQiu(luckNumber)
    return res

if __name__ == '__main__':
    # 启动fastapi
    # 不可调试
    # command = "uvicorn api:app --host 127.0.0.1 --port 38888 --reload"# --reload:在代码改变后重启服务器，只能在开发的时候使用
    # os.system(command)
    # 可调式启动
    env = os.getenv('env')
    if env != "DEV":
        uvicorn.run("api:app", host='104.219.236.109',port=3001, reload=False)  # reload:在代码改变后重启服务器，只能在开发的时候使用
    else:
        uvicorn.run("api:app", host='127.0.0.1',port=3001, reload=True)