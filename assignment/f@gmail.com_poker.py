import dice_module
import random

def roll_dice(number_of_dice):
    temp_hand=[0,0,0,0,0]
    for i in range(number_of_dice):
        temp_hand[i]=random.randint(1,6)
    return temp_hand

def count_faces(hand):
    dice_count = [0, 0, 0, 0, 0, 0, 0]
    for i in hand:
        dice_count[i]+=1
    return dice_count

def rank_hand(hand):
    dice_count = count_faces(hand)
    #sorting dice count
    for i in range(0,7):
        for j in range(i+1,7):
            if(dice_count[i]<dice_count[j]):
                temp_dice_count=dice_count[i]
                dice_count[i]=dice_count[j]
                dice_count[j]=temp_dice_count

    if dice_count[0]==5:
        return 6
    if dice_count[0]==4:
        return 5
    if dice_count[0]==3 and dice_count[1]==2:
        return 4
    if dice_count[0]==3:
        return 3
    if dice_count[0]==2 and dice_count[1]==2:
        return 2
    if dice_count[0]==2:
        return 1
    return 0

def get_rank_name(rank):
    if rank==6:
        return "Five of a Kind"
    if rank==5:
        return "Four of a Kind"
    if rank==4:
        return "Full House"
    if rank==3:
        return "Three of a Kind"
    if rank==2:
        return "Two Pairs"
    if rank==1:
        return "One Pair"
    if rank==0:
        return "Nothing Special"

def display_details(filename, author, student_id, email):
    print("File       : ",filename)
    print("Author     : ",author)
    print("Student ID : ",student_id)
    print("Email      : ",email)
    print("This is my own work as defined by the Eynesbury Academic Misconduct Policy.")

#Asks player to pay or not and display result
def make_choice():
    loop=True #for controling while loop
    while loop:
        choice=input("Would you like to play dice poker [y|n]?")
        if choice=='y':
            play()
            print("Game Summary")
            print("============")
            print("You played ",(player_wins+dealer_wins+draws)," games")
            print("|--> Games won: ",player_wins)
            print("|--> Games lost: ",dealer_wins)
            print("|--> Games drawn: ",draws)
            print("Thanks for playing!")
            loop=False
        elif choice=='n':
            print("No worries... another time perhaps... :)")
            loop=False
        else:
            print("Please enter either 'y' or 'n'.")

#Variables to track results
player_wins=0
draws=0
dealer_wins=0

#Asks for play again
def play_again():
    loop=True #for controling while loop
    while loop:
        choice=input("Play again [y|n]?")
        if(choice=='y'):
            play()
            loop=False
        elif(choice=='n'):
            loop=False
        else:
            print("Please enter either 'y' or 'n'.")

#Called after player confirms to play an round
def play():
    global player_wins
    global dealer_wins
    global draws
    
    player_hand = roll_dice(5)
    player_rank=rank_hand(player_hand)
    player_rank_name=get_rank_name(player_rank)
    
    dealer_hand = roll_dice(5)
    dealer_rank=rank_hand(dealer_hand)
    dealer_rank_name=get_rank_name(dealer_rank)
    
    print("Player's hand:")
    dice_module.display_dice(player_hand)
    print("-- Player has ",player_rank_name)
    
    print("Dealer's hand:")
    dice_module.display_dice(dealer_hand)
    print("-- Dealer has ",dealer_rank_name)
    
    if player_rank > dealer_rank:
        print("** Player wins! **")
        player_wins+=1
    elif player_rank <dealer_rank:
        print("** Dealer wins! **")
        dealer_wins+=1
    else:
        print("** Draw! **")
        draws+=1
    
    play_again()

display_details("poker.py","Batman","0123456X","0123456@eynesbury.sa.edu.au")
make_choice()
