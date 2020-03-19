import asyncio
import sanic
from sanic import Sanic
from sanic.response import json
import sys

app = Sanic(__name__)

class Stu :
    def __init__(self,name=None,age=0) :
        self.name = name
        self.age = age
    def _dict(self) :
        return {"Name":self.name,"Age":self.age}

@app.route('/respond',methods=['GET','POST'])
def handleResp(request) :
    print("Request Received")
    print(request)
    a = {}
    b = []
    for i in range(100) :
        A = Stu("None",i)
        a[i] = A._dict()
        b.append(A._dict()) 
    return json({'data':b})

@app.route('/respond_2',methods=['GET','POST'])
def handleResp(request) :
    print("Request Received")
    print(request)
    
    return json(Stu("Name",100)._dict())
    
if __name__ == "__main__" :
    try :
        port_ = int(sys.argv[1])
    except IndexError :
        port_ = 10000
    except ValueError :
        print("Invalid Port")
        exit(0) 
    try :
        app.run(host ="0.0.0.0" , port=port_)
    except KeyboardInterrupt :
        print("[!!] Received Keyboardinterrupt")
        exit(0)
