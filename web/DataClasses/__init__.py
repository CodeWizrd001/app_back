from ..Utils import hash

class Stu :
    def __init__(self,name=None,age=0) :
        self.name = name
        self.age = age
    def _dict(self) :
        return {"Name":self.name,"Age":self.age}
    def __dict(self) :
        return {"Name":str(self.name),"Age":str(self.age)}

class User :
    def __init__(self,name="user",mail="a@b.com",password="pass",uid="0") :
        self.uname = name 
        self.umail = mail
        self.upass = hash(password)
        self.uid = uid
    def _dict(self) :
        return {"User":self.uname,"Email":self.umail}
    def __dict(self) :
        return {"User":self.uname,"Email":self.umail,"Passwprd":self.upass,"UserID":self.uid}
