import requests
import serial

url = 'https://localhost/index.php' 
try:
    port =serial.Serial( port = "COM5", baudrate=9600)
except:
    print("verifier le port utilisé")

d=""
compt=0
datao=[]
while compt<=1:
    #print("voila :" ,port.readline()) 
    x= str(port.readline())
    datao.append(x[3:24:1])
    print(datao)
    compt=compt+1


print("données ",datao);

print(d)
myobj = {'oxygene': datao} # data 

x = requests.post(url,params=myobj)

print(x.text)
