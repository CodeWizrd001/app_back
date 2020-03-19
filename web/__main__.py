import asyncio
import sanic
import random
from sanic import Sanic
from sanic.response import json
import sys

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
        A = Stu(random.choice(nameList),random.randint(1,random.choice([2,50,100])))
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
