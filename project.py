import random

guess = random.randint(1, 9)
chances=5


while chances>0:
    userInput=int(input('Guess a number between 1 and 9: '))
    if(userInput==guess):
            print('You got it!')
            break
    elif(userInput>guess):
            print('your guess is too high,try to guess lower')
            chances=chances-1
            continue
    else:
        print('your guess is too low,try to guess higher')
        continue         
    if(chances==0):
        print('you lost!!')
