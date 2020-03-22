client_id = "818861716713-g68oa4jvgdhhf9omtc4cjpdimil8jjas.apps.googleusercontent.com"
client_secret = "IaEK5i3mWfJuS-By0-Qy5mXp"

alph = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def isalpha(ch) :
    return ch in alph 

def hash(s) :
    s = ''.join([chr(ord(i)+1) for i in s])
    return s 