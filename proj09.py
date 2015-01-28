#################################################
#Computer Project #9
#Algorithm
#   Run function main
#       Establish deck
#       Shuffle deck
#       Create empty list to keep track of rounds
#       Run while loop
#       Create empty lists for both hands
#           Run function deal
#           Run function prompt
#           Display round summary
#           Prompt user to play again
#################################################    

import cards

#pass in deck and both player's hands
def deal(my_deck,player1_list,player2_list):

    """
    Deal cards to both hands.

    Receive:  a deck and two empty lists
    Return:   two dealt hands with 2 cards in each
    Algorithm:
       Adds two cards to each players hands
       Add cards values for each hand
       Displays player's hand
       Displays dealer's hand
    """

    #Adds two cards to each players hands
    for i in range( 2 ):
        player1_list.append(my_deck.deal())
        player2_list.append(my_deck.deal())

    #Grabs both cards and adds them together
    total_1=player1_list[0].get_value()
    total_1b=player1_list[1].get_value()
    player_total = (total_1 + total_1b)

    total_2=player2_list[0].get_value()
    total_2b=player2_list[1].get_value()
    player_total2 = (total_2 + total_2b)

    #Displays both player's and dealer'hands
    print( "Player:",player1_list,",and the current value is",player_total)
    print()
    print( "Dealer:",player2_list[:1],'X')
    print()
    

def calculate(my_list):

    """
    Calculating values for each card.

    Receive:  Either player's hand or dealer's hand
    Return:   Card's value
    Algorithm:
       Loop:
          for every card in hand check to see if its an Ace
          add 11 to current value if convenient, otherwise add 1
          if not an ace, value stays same
       return value
    """
    value = 0
    #for every card in current hand
    for card in my_list:

        #checks to see if card is an Ace
        if card.get_rank() == 1:
            
            #if current value plus 11 is less than 21, add 11 to current value
            if (value + 11) <= 21:
                value += 11
            #otherwise just make current value set to itself plus one
            else:
                value += 1
        else:
            #if card is not an ace, set it to its value 
            value += card.get_value()                  
    return value

def prompt(my_deck,player1_list,player2_list,round_list):

    """
    Asking user to hit or stand and determing winner.

    Receive:  the deck, both hands, and round tracking list
    Return:   Winner of match 
    Algorithm:
       Loop checks if user hits
          add new card to current hand
          display hand and value total
          if greater than 21, hand is busted
          ask player to hit or stand again
          if player stands, check if player won or tie
       Loop checks if dealer shall stand or hit
          add new card to current hand if total is under 17
          display hand and value total
          if total is greater than 17, check for winner
          if total is greater than 21, hand is busted
          if initial hand is over 17, check if dealer won or tie
       return winner of round
    """
    #prompt user to hit or stand
    action_input=input("H,Y, or enter to hit, anything else to stand:").upper()
    print()

    while action_input == "Y" or action_input == "H" or action_input == "" :

        #If player decides to hit, add another card to hand
        print("Player Hits!") 
        player1_list.append(my_deck.deal())
        #Display new hand and calculate new total
        print("Player:",player1_list ,", current value is now", \
              calculate(player1_list))
        print()

        #if total is greater than 21, player loses
        if calculate(player1_list) > 21:
            print("Player Loses!")
            print() 
            break

        #prompt user to hit or stand
        action_input=input("H,Y, or enter to hit, anything else to stand:") \
                      .upper()
        print()

    #if player doesn't hit
    else:       
        print("Player Stands")
        #if player's hand is greater than dealers hand
        if calculate(player1_list) > calculate(player2_list):
            print("Player Wins!")
            print()
            round_list[0] += 1
        #if both player's and dealer's hands are the same value 
        elif calculate(player1_list) == calculate(player2_list):
            print("Game is a tie!")
            print()
            round_list[2] +=1

    #dealer's hand, if total is under 17, dealer automatically hits        
    while calculate(player2_list) < 17 and calculate(player1_list) < 21 :
        
        print("Dealer Hits")
        #Add card to dealers hand
        player2_list.append(my_deck.deal())
        #Display current hand and new total
        print("Dealer:",player2_list,", current value is now", \
              calculate(player2_list))
        print()

        #if total is greater than 17...
        if calculate(player2_list) >= 17:
            
            #check to see if total is greater than player's hand
            if calculate(player2_list) > calculate(player1_list):
                print("Dealer wins!")
                print()
                #adds one to dealers rounds won
                round_list[1] +=1
                
        #if total is greater than 21, dealer loses           
        elif calculate(player2_list) > 21:
            print("Dealer Loses")
            print() 
            break

    #if dealer's hand is greater than 17...    
    else:
        #if its a tie
        if calculate(player1_list) == calculate(player2_list):
            print("Game is a tie!")
            print()
            round_list[2] +=1
            
        #if it is not a tie, but greater than 17    

def main():

    """
    Runs functions and displays scoring summary.

    Return:   Score summary
    Algorithm:
      shuffles cards in deck
      creates empty round list
      assigns response to "Y" to start first round
      Loop:
          if player plays another round and deck has more than 4 cards
             create empty lists for both hands
             Run function deal
             Run function prompt
          Display round summary
          Ask user if they wish to play another round
       return score summary
    """
    my_deck = cards.Deck()
    #shuffles deck
    my_deck.shuffle()
    
    #empty list to keep track of rounds won
    round_list = [0,0,0]
    
    #To start first round
    response = "Y"
    
    #round checks if there is atleast more than 4 cards in deck to deal
    while response == "Y" or response == "" and (len(my_deck)) >= 4:

        #creates empty hand lists
        player1_list=[]
        player2_list=[]

        #runs function deal with deck and hands passed in
        deal(my_deck,player1_list,player2_list)

        #runs function prompt with deck, hands, and round list passed in
        prompt(my_deck,player1_list,player2_list,round_list)

        #displays round summary
        print("Thanks for playing!")
        print()
        print("-"*15) 
        print("Round Summary:")
        print("-"*15) 
        print("Rounds won by player:", round_list[0]) 
        print("Rounds won by dealer:", round_list[1])
        print("Draw:", round_list[2]) 
        print()

        #prompts user to play another round
        response = input("Play again?").upper()
        print()
main() 
    



    
    



