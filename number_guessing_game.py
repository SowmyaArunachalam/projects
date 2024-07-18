import random
import math
x=int(input("Enter a lower limit: "))
y=int(input("Enter a upper limit: "))

chance=math.ceil(math.log(y - x + 1, 2))
print("         You have ",chance," chances to guess the integer!!")

z=random.randint(x,y)
count=0
while True:
    n=int(input("Guess a Number: "))
    if(count<=chance):
        count+=1
        if(n==z):
            print("Congratulations you did it in ",count," try")
            break
        elif(n>z):
            print("You guessed too high!")
            
        elif(n<z):
            print("You guessed too small!")
            
    else:
        print("The nummber is: ",z)
        print("Better lluck next time!!!")
        break