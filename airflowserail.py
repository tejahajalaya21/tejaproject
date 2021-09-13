import serial

import requests
url="http://.php"
try:
    port =serial.Serial( port = "COM5", baudrate=9600) #vérifier port 
except:
    print("verifier le port utilisé")

data=[]
compt=0
dp=[]
while compt<=3:
    print(port.readline()) 
    data.append((len(str(port.readline()))-3)) 
    compt=compt+1
    
print("donnes=",data)


             
print(data)
myobj = {"airflow":data}# data 

x = requests.post(url,params=myobj)

print(x.text)

port.close()
