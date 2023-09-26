import random 

myNumber = "0964729078"
randomNumber = "09"
counter = 0

print("----------------")
while randomNumber != myNumber :
    randomNumber = "09"
    for i in range (1,8+1) :
        randomNumber += str (random.randint(0,9))
    counter = counter + 1 
    print(f"[{counter}] - {randomNumber}")

print()
print("----------------")
print(f"Success {randomNumber} AFTER {counter} Times")
print("----------------")

