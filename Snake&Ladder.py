import random
def SnakeAndLadder():
  try:
    P1 = True

    Snake = {30: 6, 37: 13, 49: 9, 59: 19, 68: 3, 66: 35, 88: 32, 82: 44, 94: 55, 98: 14}

    ladder = {2: 21, 17: 36, 11: 48, 39: 80, 31: 71, 53: 92, 74: 93, 65: 84, 62: 83, 86: 97}


    Player = {'P1': 0, 'P2': 0}
    DiceCount = 0
    Position = 0

    while (Player['P1'] != 100 and Player['P2'] != 100):
        if P1:
            print("Player 1 : enter any key its your chance")
            input()

            dice = random.randint(1, 6)
            print("Dice Number:", dice)

            Position = int(Player['P1']) + dice

            if Position in Snake:
                print("oops!!Snake Bite ")
                Player['P1'] = int(Snake[Position])
            if P1:
                print("Player 1 : click any key")
                input()

            elif Position in ladder:
                print("wow!!you get a ladder ")
                Player['P1'] = int(ladder[Position])

            else:
                if Position <= 100:
                    Player['P1'] = Position
            DiceCount += 1

            P1 = False
            P2 = True
            print("Player 1:your Position is " + str(Player['P1']))

        elif P2:
            print("Player 2 : click any key:")
            input()

            dice = random.randint(1, 6)
            print("Dice Numer:", dice)
            Position = int(Player['P2']) + dice
            if Position in Snake:
                print("oops!!Snake Bite:")
                Player['P2'] = int(Snake[Position])
            elif Position in ladder:
                print("wow!!!you get a ladder")
                Player['P2'] = int(ladder[Position])
            else:
                if Position < 100:
                    Player['P2'] = Position
            DiceCount += 1
            P1 = True
            P2 = False
            print("Player 2: Your Position Is " + str(Player['P2']))

    print("Player 1:your Position is " + str(Player['P1']))

    print("No of time dice use for win :" + str(DiceCount))

  except Exception as e:
      print("there is error in your program=" ,type(e))

  if Player['P1'] == 100:
        print('Player P1 Is Winner')
  elif Player['P2'] == 100:
        print(' Player P2 Is Winner')

#driver code

print("                      Welcome To Snake And Ladder Game             ")
print("                      Two Player Play This Game                    ")
print("                      Now We will Start this Game                  ")

SnakeAndLadder()

