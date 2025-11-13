'''Snakes-And-Ladders
Snakes and Ladders is one of the most famous board games in the world and is really encouraged for young children to learn counting. 
So, I created a new program that is very similar to the game's system. You can view my code below.
import random'''
# snakes[0] = head , snakes[1] = tail
# ladder[0] = bottom, ladder[1] = top
import random
snakes = [
    (39, 21),
    (70, 53),
    (82, 42),
    (25, 2),
    (96, 71)
]
ladders = [
    (6, 28),
    (11, 30),
    (60, 95),
    (16, 38),
    (57, 79)
]
print('Welcome to game of snakes and ladders!!!')
print('This is a two player game which mainly focuses on luck, so GOOD LUCK!!!!')

print('Before you start the game, please decide who is player 1 and who is player 2 with your partner.')
print("Each set represents the position of the snakes, the first number is the position of a snake's head and the second number if the position of a snake's tail.")
for snake_position in snakes:
    print('->',snake_position)
print("Each set represents the position of the ladders, the first number is the position of a laddder's bottom and the second number in each set is the position of the ladder's top.")
for ladder_position in ladders:
    print('->',ladder_position)

def check_snakes_and_ladders(position, snakes, ladders):
    global state
    for i in snakes:
        if position == i[0]:
            position =i[1]
            print('You’ve landed upon the snake’s head and lost your path.')
            print("So, your position went down to ", position)
    for i in ladders:
        if position == i[0]:
            position = i[1]
            print('WOW!!!!! You have found a huge ladder and climbed up. ')
            print("So, your position went up to ", position)
    state = position

player_1 = 0
player_2 = 0
count = 0
while count != 100:
    x = random.randint(1,7)
    roll = str(input('Please enter anything to roll the dice, player 1: '))
    player_1 += x
    print('The number you got is:', x)
    print("Player 1, your current position right now is: ",player_1 )

    check_snakes_and_ladders(player_1 ,snakes, ladders)
    player_1  = state

    if player_1  == 100:
        print('Congratulations player 1, you win this game!!!')
        count = 100
        break
    elif player_1  > 100:
        print('Player 1, You need to get a lucky number to reach hundred PRECISELY- not less, not more!!!')
        player_1 -= x
        print("Thus you're current position is still", player_1)

    y = random.randint(1,7)
    roll1 = str(input('Please enter anything to roll the dice, player 2: '))
    player_2+= y

    print('The number you got is:', y)
    print("Player 2, your current position right now is: ",player_2)
    check_snakes_and_ladders(player_2,snakes, ladders)

    player_2 = state
    if  player_2 == 100:
        print('Congratulations player 2, you win this game!!!')
        count = 100
        break
    elif player_2 > 100:
        print('Player 1, You need to get a lucky number to reach hundred PRECISELY- not less, not more')
        player_2-= y
        print('Thus you are current position is still',player_2)
