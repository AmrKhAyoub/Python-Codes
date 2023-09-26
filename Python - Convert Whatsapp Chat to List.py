import os
import time
import builtins
##################################
def getSender(line : str) -> str :
    user1 = "user1 name in chat"
    aliases1 = "User1 final name"
    user2 = "user2 name in chat"
    aliases2 = "User2 final name"
    if line.__contains__(user1) :
        return aliases1
    elif line.__contains__(user2) :
        return aliases2
    else :
        return None
##################################
def getMessage(line : str) -> str :
    splitLine = line.split(":")
    message = splitLine[len(splitLine)-1]
    message = message.replace("\n","")
    return message
##################################
def getDate(line : str) -> str :
    splitLine = line.split("-")
    splitLine = splitLine[0].split(" ")
    date = splitLine[0].replace(",","")
    return date
##################################
def getTime(line : str) -> str :
    splitLine = line.split("-")
    splitLine = splitLine[0].split(" ")
    time = splitLine[1]
    return time
##################################
def creatMessage(sender,message,date,time) -> dict :                                    
    return  {
        "sender":f"{sender}",
        "message":f"{message}",
        "date":f"{date}",
        "time":f"{time}",
    }
##################################
def Message(line : str) -> dict :
    if line[0].isdecimal() is False:
        return None
    line = line.replace("\u202f","")
    sender = f"{getSender(line)}"
    message = f"{getMessage(line)}"
    date = f"{getDate(line)}"
    time = f"{getTime(line)}"
    return creatMessage(sender,message,date,time)
##################################
def main() -> None:
    path = "/storage/emulated/0/"
    path += "AAA EDIT/"
    os.chdir(path)
    chatFile = builtins.open("test.txt","r") 
    chat = [Message(line) for line in chatFile if Message(line) is not None]
    print(chat)
##################################

beginTime = time.time()
#main()
endTime = time.time()
finalTime = endTime - beginTime
approx = 10000
finalTime = int(finalTime*approx)/approx
print(f"Finished in {finalTime} Seconds")

