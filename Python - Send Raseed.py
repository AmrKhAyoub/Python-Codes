
def transfer (number,value) :
    number = number.replace (" ","")
    number = number.replace("+249","0")
    if number.len != 10 :
        return "Invalid Number !"
    elif number[1] == '9' :
        return "*200*2209*{}*{}*{}#".format(value,number,number)
    else :
        return "*303*{}*{}*0000#".format(value,number)

number = str(input("Enter Your Number : "))
value = int(input("Enter Amount of Transfer :"))
print("----------------------")
print("Code of Transfer is :")
#print(transfer(number,value))


 

