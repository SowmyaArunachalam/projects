'''
import random

print("Welcome to Hand Cricket")
option = input("choose odd or even:")
symbol = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("symbol:", symbol)

computer = random.choice(symbol)
player = int(input("enter a number within symbol:"))
print("player:", player)
print("computer:", computer)
aim1 = 0
aim2 = 0
score_player = 0
score_computer = 0
sum = player + computer
batting = 0

if sum % 2 == 0 and option == 'even':
    print("player is batting")
    batting = player
    game = 'on'
    while game == 'on':
        computer = random.choice(symbol)
        player = int(input("enter a number within symbol:"))
        print("player:", player)
        print("computer:", computer)
        if computer == player:
            print("player lose")
            print("computer's aim to score:", score_player)
            print("computer is batting")
            aim1 = score_player
            game = 'on'
            while game == 'on':
                computer = random.choice(symbol)
                player = int(input("enter a number within symbol:"))
                print("player:", player)
                print("computer:", computer)
                score_computer += computer
                print("score of computer:", score_computer)
                if computer == player:
                    print("game over")
                    print("player wins")
                    game = 'off'
                elif score_computer > aim1:
                    print("computer wins")
                    game = 'off'


        else:
            score_player += player
            print("score of player:", score_player)

else:
    print("computer is batting")
    batting = computer
    game = 'on'
    while game == 'on':
        computer = random.choice(symbol)
        player = int(input("enter a number within symbol:"))
        print("player:", player)
        print("computer:", computer)
        if computer == player:
            print("computer lose")
            print("player's aim to score:", score_computer)
            print("player is batting")
            aim2 = score_computer
            game = 'on'
            while game == 'on':
                computer = random.choice(symbol)
                player = int(input("enter a number within symbol:"))
                print("player:", player)
                print("computer:", computer)
                score_player += player
                print("score of player:", score_player)

                if computer == player:
                    print("game over")
                    print("computer wins")
                    game = 'off'
                elif score_player > aim2:
                    print("player wins")
                    game = 'off'

        else:
            score_computer += computer
            print("score of computer:", score_computer)
'''