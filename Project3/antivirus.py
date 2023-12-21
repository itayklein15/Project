import requests
import os
def Answears(resource):
    url = 'https://www.virustotal.com/vtapi/v2/file/report' 
    params = {'apikey': "b52ffef6c335e024625f2e47fb63ef73ce41137090320cbaf029f8371e81662d" ,'resource': resource}
    response = requests.get(url, params=params)
    ans=str(response.json())
    result=ans.split(",")
    result=str(result[-3])
    result=result[-1]
    if(result=='0'):
        print("YOU HAVE NO VIRUSES :)")
    else:
        print("YESH LEHA",result,"VIRUSIM :( ")

def Viruscheker(fole,reshima):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': 'b52ffef6c335e024625f2e47fb63ef73ce41137090320cbaf029f8371e81662d'}
    if(fole>len(reshima)-1):
        print("THATS IT")
    else:
        print(list[fole])
        files = {'file': (list[fole], 'rb')}
        response = requests.post(url, files=files, params=params)
        dict=str(response.json())  
        try1=dict.split(",")
        resource=str(try1[2][14:-1])
        Answears(resource)
        Viruscheker(fole+1,reshima)

list=os.listdir("C:/Users/איתי קליין/Documents/Looz")
Viruscheker(0,list)