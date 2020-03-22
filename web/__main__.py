from . import *

from .stud import bp as sbp

from .user import bp as ubp

app.blueprint(sbp)
app.blueprint(ubp)

async def reset_db(db, client):
    await client.drop_database(db)
    print("DB Reset")

async def init() :
    global mClient
    global UserList
    global StuList
    global db

    loop = asyncio.get_event_loop()
    mClient = AsyncIOMotorClient(io_loop=loop)
    db = mClient["APP_BACK"]
    StuList = db['StuList']
    UserList = db['UserList']

async def main():
    try :
        x = sys.argv[1]
    except IndexError :
        x = None

    await init() 

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
