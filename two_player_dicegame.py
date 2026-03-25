import random
def two_player_dicegame():
    r=int(input("enter no of rounds"))
    p1_score=0
    p2_score=0
    for i in range(1,r+1):
        print(f"-------{i} round-------")

        input("player 1 press enter to roll")
        p1=random.randint(1,6)
        print(f"player 1 rolled {p1}")
        p1_score+=p1

        input("player 2 press enter to roll")
        p2=random.randint(1,6)
        print(f"player 2 rolled {p2}")
        p2_score+=p2

    print("\n-----final scores-----\n")
    print(f"player 1 score {p1_score}")
    print(f"player 2 score {p2_score}")

    if(p1_score>p2_score):
        print(f"🏆 player 1 won the game with score {p1_score}")
    elif(p2_score>p1_score):
        print(f"🏆 player 2 won the game with score {p2_score}")
    else:
        print("IT'S A TIE")
two_player_dicegame()