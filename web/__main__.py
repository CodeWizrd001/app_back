import asyncio
import sanic
import random
from sanic import Sanic
from sanic.response import json
import pymongo
import sys
from motor.motor_asyncio import AsyncIOMotorClient

app = Sanic(__name__)

nameList = ['Olivia', 'Ruby', 'Emily', 'Grace', 'Jessica', 'Chloe', 
'Sophie', 'Lily', 'Amelia', 'Evie', 'Mia', 'Ella', 'Charlotte', 
'Lucy', 'Megan', 'Ellie', 'Isabelle', 'Isabella', 'Hannah', 'Katie', 
'Ava', 'Holly', 'Summer', 'Millie', 'Daisy', 'Phoebe', 'Freya', 
'Abigail', 'Poppy', 'Erin', 'Emma', 'Molly', 'Imogen', 'Amy', 'Jasmine', 
'Isla', 'Scarlett', 'Leah', 'Sophia', 'Elizabeth', 'Eva', 'Brooke', 
'Matilda', 'Caitlin', 'Keira', 'Alice', 'Lola', 'Lilly', 'Amber', 
'Isabel', 'Lauren', 'Georgia', 'Gracie', 'Eleanor', 'Bethany', 
'Madison', 'Amelie', 'Isobel', 'Paige', 'Lacey', 'Sienna', 'Libby', 
'Maisie', 'Anna', 'Rebecca', 'Rosie', 'Tia', 'Layla', 'Maya', 'Niamh', 
'Zara', 'Sarah', 'Lexi', 'Maddison', 'Alisha', 'Sofia', 'Skye', 
'Nicole', 'Lexie', 'Faith', 'Martha', 'Harriet', 'Zoe', 'Eve', 'Julia', 
'Aimee', 'Hollie', 'Lydia', 'Evelyn', 'Alexandra', 'Maria', 'Francesca', 
'Tilly', 'Florence', 'Alicia', 'Abbie', 'Emilia', 'Courtney', 'Maryam', 'Esme']

p = []

class Stu :
    def __init__(self,name=None,age=0) :
        self.name = name
        self.age = age
    def _dict(self) :
        return {"Name":self.name,"Age":self.age}
    def __dict(self) :
        return {"Name":str(self.name),"Age":str(self.age)}

async def Listify(List) :
    a = []
    for i in List :
        temp = Stu(i['Name'],i['Age'])
        a.append(temp._dict())
    return a 

@app.route('/respond',methods=['GET'])
async def handleResp(request) :
    global p

    print("Request Received")
    print(request)
    b = list(p)
    c = collection.find({"Name":{"$gt":""}})
    c = await c.to_list(length=100000)
    b = await Listify(c)
    return json({'data':b})

@app.route('/respond_2',methods=['GET','POST'])
def Fetch(request) :
    print("Request Received")
    print(request)
    
    return json(Stu("Name",100)._dict())

@app.route('/add',methods=['POST'])
async def Add(request) :
    global p

    print("Request Received") 
    print(request)
    a = request.json
    b = type(a)
    print("Body :",a,b) 

    x = Stu(a['name'],int(a['age']))
    y = x._dict()
    z = collection.find(y)
    z = await z.to_list(length=10000)
    if z == [] :
        await collection.insert_one(y)
        print("Done")
    else :
        print("Already Exist")

    y = x._dict()

    return json(y)

async def reset_db(db, client):
    await client.drop_database(db)
    print("DB Reset")

async def initialize_db():
    global mClient
    global db
    global collection

    loop = asyncio.get_event_loop()
    mClient = AsyncIOMotorClient(io_loop=loop)
    db = mClient["APP_BACK"]
    collection = db['StuList']
    await reset_db(db,mClient) 
    a = {}
    for i in range(100) :
        A = Stu(random.choice(nameList),random.randint(1,random.choice([2,50,100])))
        a[i] = A._dict()
        await collection.insert_one(a[i]) 
    print("Done")
    return mClient, db

async def main():
    global mClient
    global db

    mClient, db = await initialize_db()

    try :
        x = sys.argv[1]
    except IndexError :
        x = None

    if x == "reset_db":
        await reset_db(db, mClient)
        return

    try :
        port_ = int(sys.argv[1])
    except IndexError :
        port_ = 10000
    except ValueError :
        print("[!] Invalid Port")
        print("[!] Defaulting To Port 10000")
        port_ = 10000
    
    sanic_server = await app.create_server(
        host="0.0.0.0", port=port_, return_asyncio_server=True
    )
    sanic_server.after_start()
    try:
        asyncio_server = sanic_server.server
        await asyncio_server.serve_forever()
    finally:
        sanic_server.before_stop()

    await sanic_server.close()

    for connection in sanic_server.connections:
        connection.close_if_idle()
    sanic_server.after_stop()

if __name__ == "__main__":
    mainCo = main()
    try:
        asyncio.run(mainCo)
    except KeyboardInterrupt:
        print("Ctrl+C received - Exiting .. ")
