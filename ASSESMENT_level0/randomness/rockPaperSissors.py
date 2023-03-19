import random as r
def getUserMove():
    user = input()
    # print(user)
    return user

def getComputerMove():
    computer = r.choice(["Rock", "Paper", "Sissors"])
    # print(computer)
    return computer

def getResult():
    user_count = 0
    computer_count = 0
    draw = 0
    for i in range(10):
        user = getUserMove()
        computer = getComputerMove()
        print(user, computer)
        if (user == "Rock" and computer == "Paper") or (user == "Paper" and computer == "Sissors") or (user == "Sissors" and computer == "Rock"):
            computer_count += 1
        elif (user == "Rock" and computer == "Sissors") or (user == "Paper" and computer == "Rock") or (user == "Sissors" and computer == "Paper"):
            user_count += 1
        else:
            draw += 1
    total_countable = 10 - draw
    user_wins = user_count
    user_losses = total_countable - user_wins
    computer_wins = computer_count
    computer_losses = total_countable - computer_wins
    print("Number of draws :", draw)
    print("Number of wins of user : ", user_wins)
    print("Number of wins of computer : ", computer_wins)
    print("Number of losses of user : ", user_losses)
    print("Number of looses of computer : ", computer_losses)
getResult()
        
    

