print("welcome to atm\n")
option = input("withdraw,balance,deposit :")

amount = 10000

if option == "withdraw" :
    withdraw= int(input("enter the amount you need to withdraw :"))
    if withdraw < 100:
        print("\nenter the amount above 100 or equal to")
    else:
       print(withdraw)
       print("your amount succesfully withdraw")

elif option == "balance":
    print("\nyour account balance is",amount)

elif option == "deposit":
    deposit = int(input("enter the amount u need to deposit :"))
    if deposit <100:
        print("\ndeposit amount above than 100 or equal to")
    else:
       total = deposit + amount
       print("\n",deposit,"now deposited ,total balance is ",total)



#password checking

max_attempts = 3
attempt = 0
crt_password = "abdul123"

while attempt < max_attempts:
    try:
        password = input("enter a password :")

        if password == "":
            print("❗password cannot be empty ")
            continue

        if password == crt_password :
            print("ascess granted")
            break

        else:
            attempt += 1
            print(f"❌ Wrong password. {max_attempts  - attempt} attempt(s) left.")

    except KeyboardInterrupt :
        print("\n process interepted by user ")
        break

else:
    print("too many failed attempt access denied")


# number guessing game
import random

def number_guess ():
    number_to_guess = random.randint (1,100)
    attempts = 0

    print("welcome to number_guessing game ")

    while  True:
        try:
            guess = int(input("enter a guess :"))
            attempts += 1

            if guess <number_to_guess :
                print("too low , try again")
            elif guess >number_to_guess :
                print("too high , try again")
            else:
                print(f"correct ! your guessed it in {attempts} attempts.")
                break
        except ValueError :
            print("enter a valid number ")

number_guess()


#dice roll game

import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value ,max_value )

    return roll
while True:
    players = input("enter the numbers of players : ")
    if players.isdigit() :
        players = int(players )
        if 2 <= players <=4 :
            break
        else:
            print("must be between 2 - 4 players ")
    else:
        print("invalid ,try again")

max_score = 50
player_score =[0 for _ in range(players )]

while max(player_score) < max_score:

    for player_idx in range(players ):
       print("\nplayer_number",player_idx +1, "turn has just started" )
       print("your total score is :",player_score [player_idx ],"\n")
       current_score = 0

       while True:
          should_roll = input("would you like to roll(y) ?")
          if should_roll.lower() != "y":
              break

          value = roll()
          if value == 1 :
              print("you rolled a 1 ! turn done ")
              current_score =0
              break
          else:
              current_score += value
              print("you rolled a",value)
          print("your score is ",current_score )

       player_score [player_idx ] += current_score
       print("your total score is :",player_score[player_idx ])

max_score = max(player_score )
winnig_idx = player_score.index(max_score )
print("player number",winnig_idx + 1, "is the winner with a score of :",max_score )