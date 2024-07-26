import random
def get_input():
    print("guess the word! word is a name of the fruit")

    someWords = '''apple banana mango strawberry  
    orange grape pineapple apricot lemon coconut watermelon 
    cherry papaya berry peach lychee muskmelon'''

    words=someWords.split(" ")

    chosen_word=random.choice(words)
    return chosen_word

def hangman(chosen_word):
    for i in chosen_word:
        print("_",end=" ")

    print()
    chance=len(chosen_word) + 2
    c=0
    guess=""
    while(chance>0):
        win=0
        letter=input("Enter a letter: ")
        guess+=letter
        for i in chosen_word:
            if i in guess: 
                print(i,end=" ")
                win+=1
            else:
                print("_",end=" ")
        if(win==len(chosen_word)) :
            print('\nyou win!!!!!!')
            c=1
            break       
        chance-=1
        print()
    return c



def main():
    word=get_input()
    result=hangman(word)
    if(result==0):
        print("You lose...")
        print("The word is ",word)
main()