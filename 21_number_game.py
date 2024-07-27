import random
c=0
def human(l):
    n=int(input("How many number do you want to add? "))
    
    for _ in range(n):
            N=int(input())
            if(N>=21 or N!=(l[-1]+1)):
                return 0,l
            l.append(N)   
    
    return 1,l

def computer(l):
    for _ in range(3):
        last=l[-1]
        l.append(last+1) 
        if(last>=21):
            return 1,l
        
    return 0,l 
          
def game(chance,l):
    
    while(l[-1]<21):
        if chance=="F":
            h,l=human(l)
            if(h==0):
                print("You Lose...")
                break
            ch, l = computer(l)
            if (ch == 1):
                print("You Win")
                break
            print("Order of inputs after computer's turn is: ")
            print(l)
            
        elif chance=="S":
               
            print("Order of inputs after computer's turn is: ")
            print(l)
            print("Your Turn!!!!")
            h,l=human(l)
            if(h==0):
                print("You Lose...")
                break
            ch, l = computer(l)
            if (ch == 1 ):
                print("You Win")
                break


def main():
    l=[0]
    print("Player 2 is computer")
    start=input("Do you want to start the game? (yes/no) ")
    if(start=="yes"):
        print("Enter 'F' to take the first chance.")
        chance=input("Enter 'S' to take the second chance. ")
        if(chance=='S'):
            r=random.randint(1,10)
            for i in range(1,r+1):
                l.append(i)
            game(chance,l)
        else:
            game(chance,l)
        
    else:
        print("Thank You")
        
main()