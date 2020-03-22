from sanic import Blueprint
from sanic.response import json
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from .DataClasses import Stu

from . import *

bp = Blueprint("Stu",url_prefix="/stu")

async def Listify(List) :
    a = []
    for i in List :
        temp = Stu(i['Name'],i['Age'])
        a.append(temp._dict())
    return a 

@bp.route('/init',methods=['GET'])
async def init(request) :
    global mClient
    global StuList
    global db

    loop = asyncio.get_event_loop()
    mClient = AsyncIOMotorClient(io_loop=loop)
    db = mClient["APP_BACK"]
    StuList = db['StuList']

    return json({'status':'done'})

@bp.route('/list',methods=['GET'])
async def handleResp(request) :
    print("Request Received")
    print(request)
    c = StuList.find({"Name":{"$gt":""}})
    c = await c.to_list(length=100000)
    b = await Listify(c)
    return json({'data':b})

@bp.route('/add',methods=['POST'])
async def Add(request) :
    print("Request Received") 
    print(request)
    a = request.json
    b = type(a)
    print("Body :",a,b) 

    x = Stu(a['name'],int(a['age']))
    y = x._dict()
    z = StuList.find(y)
    z = await z.to_list(length=10000)
    if z == [] :
        await StuList.insert_one(y)
        print("Done")
    else :
        print("Already Exist")

    y = x._dict()

    return json(y)