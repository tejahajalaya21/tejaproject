import requests
import serial

url = 'https://localhost/index.php 
try:
    port =serial.Serial( port = "COM5", baudrate=9600)
except:
    print("verifier le port utilisé")

data=""
compt=0
while compt<=1:
    print(port.readline()) 
    data = data + str(port.readline())
    compt=compt+1

def nettoyer (data):
    newdata=""
    newdata=data[27:29:1]
    print("nouveau" ,newdata)
    return (newdata)

datatemp= nettoyer(data)
print("nouvelle",datatemp);

myobj = {'temperature': datatemp} # data 

x = requests.post(url,params=myobj)
print(x.text)
