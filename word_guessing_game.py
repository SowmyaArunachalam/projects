'''
import random
name=input("What is your name? ")
print("Good luck! ",name)
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

chosen_word=random.choice(words)
l=""
c=0
turn=12
while turn>0:
    
        c=0
        
        for i  in chosen_word:
            if(i in l):
               
                print(i)
            else:
                print("_")
                c+=1
        if(c==0):
            print("you won")
            break
        guess=input("Enter a letter: ")
        l+=guess
        if guess  not in chosen_word:
            turn-=1
            print("Wrong!!! you have ",turn," turns")
        elif(turn<=0):
            print("you loose")
            break
    
        
'''
