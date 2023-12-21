def convert(list):
    res = int("".join(map(str, list)))
    return res

def Binary(num,bit):
    start=bin(num)[2:]
    list = [int(x) for x in str(start)]
    Length=len(list)
    zero= bit-Length
    if(zero>=0):
        x=zero*"0" + start
        return x
    else:
        print("cant convert "+str(num)+" to binary")

def Mashlim(binary):
    list = [int(x) for x in str(binary)]
    for i in range (len(list)):
        if(list[i]==0):
             list[i]=1
        else:
            list[i]=0
    list[-1]=list[-1]+1
    if(list[-1]==1):
        return convert(list)
    
    for j in reversed (range (len(list))):
        if(list[j]==2):
            list[j]=0
            list[j-1]+=1
        if(list[j]==1):
            return convert(list)
    if(list[0]==2):
        list[0]==0
    return convert(list)

num=int(input("enter a number to convert it to binary: "))
bit = int(input("enter number of bits "))
print(Mashlim(Binary(num,bit)))