import random

scoreCpu=0
scorePlayer=0
actualRound=0+1
emojis = {
    1: "✊ Rock", 
    2: "✋ Paper", 
    3: "✌️ Scissors",  
    4: "🦎 Lizard", 
    5: "🖖 Spock"  
}


print("================================\nRock Paper Scissors Lizard Spock\n================================")
rounds=int(input("How many rounds want to play? "))
print("This are your options: \n 1) ✊ Rock \n 2) ✋ Paper \n 3) ✌️ Scissors \n 4) 🦎 Lizard \n 5) 🖖 Spock")
print("================================================================")

while actualRound<rounds+1:
    print(f"Round {actualRound}")
    player=int(input("Pick a number: "))
    cpu=random.randint(1,5)
    if  (
        (player == 1 and cpu == 4) or
        (player == 1 and cpu == 3) or
        (player == 2 and cpu == 1) or
        (player == 2 and cpu == 5) or
        (player == 3 and cpu == 2) or
        (player == 3 and cpu == 4) or
        (player == 4 and cpu == 5) or
        (player == 4 and cpu == 2) or
        (player == 5 and cpu == 3) or
        (player == 5 and cpu == 1)
        ):
          scorePlayer=scorePlayer+1
          actualRound=actualRound+1
          print("You chose:",emojis[player])
          print("CPU chose:",emojis[cpu])
          print("Player won!")
          print(f"Score \n Player: {scorePlayer} vs CPU: {scoreCpu}")
          print("================================================================")
    elif (
        (cpu == 1 and player == 4) or
        (cpu == 1 and player == 3) or
        (cpu == 2 and player == 1) or
        (cpu == 2 and player == 5) or
        (cpu == 3 and player == 2) or
        (cpu == 3 and player == 4) or
        (cpu == 4 and player == 5) or
        (cpu == 4 and player == 2) or
        (cpu == 5 and player == 3) or
        (cpu == 5 and player == 1)
        ):
        scoreCpu=scoreCpu+1
        actualRound=actualRound+1
        print("You chose:",emojis[player])
        print("CPU chose:",emojis[cpu])
        print("CPU won!")
        print(f"Score \n Player: {scorePlayer} vs CPU: {scoreCpu}")
        print("================================================================")
    else:
        actualRound=actualRound+1
        print("You chose:",emojis[player])
        print("CPU chose:",emojis[cpu])
        print("Draw!")
        print(f"Score \n Player: {scorePlayer} vs CPU: {scoreCpu}")
        print("================================================================")
else:
    print("Game Over")
    print(f"Score \n Player: {scorePlayer} vs CPU: {scoreCpu}")
    if scorePlayer>scoreCpu:
        print("Player wins")
    elif scorePlayer<scoreCpu:
        print("CPU wins")
    else:
        print("Draw")