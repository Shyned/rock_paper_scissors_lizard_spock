from player import Player





class Human_Vs_Human(Player):
    def __init__(self) :
        #add a counter for each player
          super().__init__()
          self.player1 = ""
          self.player2 =""
          self.player1_points = 0
          self.player2_points = 0
          self.repeat_till_over()


    #loop to check if player pick item in list 
    def players_pick(self):
        self.player1 = ''
        self.player2= ''
        #player 1 pick 
        while self.player1.lower() not in self.choice:
            print(self.choice)
            self.player1 = input("Player 1 please enter a choice from the list: ")
        else:
            #if player one pick is in list then player 2 pick
            while self.player2 not in self.choice:
                self.player2 = input("Player 2 please enter a choice from the list: ")

            else:
                pass
    #possibly include a loop to with a counter to check if either player has won
    def point_check (self):
        if self.player1 == 'scissors' and self.player2 == 'paper':
            print("Scissors cuts Paper.")
            self.player1_points+=1

        elif self.player1 == 'paper' and self.player2 == 'rock':
            print("Paper covers Rock.")
            self.player1_points+=1

        elif self.player1 == 'rock' and self.player2 == 'lizard':
            print("Rock crushes Lizard.")
            self.player1_points+=1


        elif self.player1 == 'lizard' and self.player2 == 'spock':
            print("Lizard poisons Spock.")
            self.player1_points+=1

        elif self.player1 == 'spock' and self.player2 == 'scissors':
            print("spock smashes scissors")
            self.player1_points+=1
            

        elif self.player1 == 'scissors' and self.player2 == 'lizard':
            print("Scissors decapitates Lizard.")
            self.player1_points+=1

        elif self.player1 == 'lizard' and self.player2 == 'paper':
            print("Lizard eats Paper.")
            self.player1_points+=1

        elif self.player1 == 'paper' and self.player2 == 'spock':
            print("Paper disproves Spock.")
            self.player1_points+=1
        
        elif self.player1 == 'spock' and self.player2 == 'rock':
            print("Spock vaporizes Rock.")
            self.player1_points+=1
        #player 2 winning 
        elif self.player2 == 'scissors' and self.player1 == 'paper':
            print("Scissors cuts Paper.")
            self.player2_points+=1

        elif self.player2 == 'paper' and self.player1 == 'rock':
            print("Paper covers Rock.")
            self.player2_points+=1

        elif self.player2 == 'rock' and self.player1 == 'lizard':
            print("Rock crushes Lizard.")
            self.player2_points+=1


        elif self.player2 == 'lizard' and self.player1 == 'spock':
            print("Lizard poisons Spock.")
            self.player2_points+=1

        elif self.player2 == 'spock' and self.player1 == 'scissors':
            print("spock smashes scissors")
            self.player2_points+=1
            

        elif self.player2 == 'scissors' and self.player1 == 'lizard':
            print("Scissors decapitates Lizard.")
            self.player2_points+=1

        elif self.player2 == 'lizard' and self.player1 == 'paper':
            print("Lizard eats Paper.")
            self.player2_points+=1

        elif self.player2 == 'paper' and self.player1 == 'spock':
            print("Paper disproves Spock.")
            self.player2_points+=1
        
        elif self.player2 == 'spock' and self.player1 == 'rock':
            print("Spock vaporizes Rock.")
            self.player2_points+=1
        
        else:
            if self.player1 == self.player2:
                print("Tie try again")


            
            

    

    #repeat cycle until either player has won
    def repeat_till_over(self):
        while True:
            if self.player1_points<2 and self.player2_points<2:
                self.players_pick()
                self.point_check()
                print(f'Player 1 has {self.player1_points} points')
                print(f'player 2 has {self.player2_points} points')
            
            elif self.player1_points==2:
                print("Player 1 is the winner")
                

            else:
                print("Player 2 is the winner")

