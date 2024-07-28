import random
def guess_num():
    act_num=random.randint(1000, 10000)
    return act_num

def Mastermind(act_num,num):
    l=['X']*4
    c=0
    turn=0
    while(True):
        num=str(num)
        act_num=str(act_num)
        if(len(num)!=4):
            print("The number is not in 4 digit")
            break
        else:
            turn+=1
            c=0
            if(act_num==num):
                print("You've become a Mastermind.")
                print(f"It took you only {turn} tries.")
                break
            
            for i in range(4):
                if num[i] == act_num[i]:
                    l[i]=num[i]
                    c+=1
            if(c!=0):
                print(f"Not quite the number. But you did get {c} digit(s) correct!")
                print("Also these numbers in your input were correct.")
            else:
                print("None of the numbers in your input match.")
            for i in range(4):
                print(l[i],end=" ")
            print()
            guess=input("Enter your next choice of numbers: ")
            num=guess
            
                
def main():
    
        num=int(input("Guess the 4 digit number: "))
        act_num=guess_num()
        if(act_num==num):
            print("Great!You guessed the number in just 1 try! You're a Mastermind!")
        else:
            Mastermind(act_num,num)
main()
    