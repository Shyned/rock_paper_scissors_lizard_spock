from random import choice
from player import Player



#place holder class name for human ai
class Human_Ai(Player):
    def __init__(self) :
        super().__init__()
        self.player1 =''
        self.cpu_choice = ''
        self.cpu_points = 0
        self.player1_points=0
        self.repeat_till_over()

    #logic for choice in this file
    def players_choice(self):
        self.player1 = ''
        while self.player1.lower() not in self.choice:
            print(self.choice)
            self.player1 = input("Please enter a choice from the list: ")
            
        #robot pick random item from list
        else:
            self.cpu_choice = choice(self.choice)
            print(f"The cpu has picked {self.cpu_choice}")

    #check inputs and give point to player
    def point_check(self):
        if self.player1 == 'scissors' and self.cpu_choice == 'paper':
            print("Scissors cuts Paper.")
            self.player1_points+=1

        elif self.player1 == 'paper' and self.cpu_choice == 'rock':
            print("Paper covers Rock.")
            self.player1_points+=1

        elif self.player1 == 'rock' and self.cpu_choice  == 'lizard':
            print("Rock crushes Lizard.")
            self.player1_points+=1


        elif self.player1 == 'lizard' and self.cpu_choice == 'spock':
            print("Lizard poisons Spock.")
            self.player1_points+=1

        elif self.player1 == 'spock' and self.cpu_choice == 'scissors':
            print("spock smashes scissors")
            self.player1_points+=1
            

        elif self.player1 == 'scissors' and self.cpu_choice == 'lizard':
            print("Scissors decapitates Lizard.")
            self.player1_points+=1

        elif self.player1 == 'lizard' and self.cpu_choice == 'paper':
            print("Lizard eats Paper.")
            self.player1_points+=1

        elif self.player1 == 'paper' and self.cpu_choice == 'spock':
            print("Paper disproves Spock.")
            self.player1_points+=1
        
        elif self.player1 == 'spock' and self.cpu_choice == 'rock':
            print("Spock vaporizes Rock.")
            self.player1_points+=1


        elif self.player1 == "rock" and self.cpu_choice == "scissors":
            print("Rock crush scissors")
            self.player1_points+=1
      

       


        #cpu winning conditions 
        elif self.cpu_choice == "scissors" and self.player1 == "paper":
            print("scissors cuts paper")
            self.cpu_points+=1

        elif self.cpu_choice == "rock" and self.player1 == "scissors":
            self.cpu_points +=1
            print("rock crushes scissors")

        elif self.cpu_choice == 'paper' and self.cpu_choice == 'rock':
            print("Paper covers Rock.")
            self.cpu_points+=1

        elif self.cpu_choice == 'rock' and self.player1 == 'lizard':
            print("Rock crushes Lizard.")
            self.cpu_points+=1


        elif self.cpu_choice == 'lizard' and self.player1 == 'spock':
            print("Lizard poisons Spock.")
            self.cpu_points+=1

        elif self.cpu_choice == 'spock' and self.player1 == 'scissors':
            print("spock smashes scissors")
            self.cpu_points+=1
            

        elif self.cpu_choice == 'scissors' and self.player1 == 'lizard':
            print("Scissors decapitates Lizard.")
            self.cpu_points+=1

        elif self.cpu_choice == 'lizard' and self.player1 == 'paper':
            print("Lizard eats Paper.")
            self.cpu_points+=1

        elif self.cpu_choice == 'paper' and self.player1 == 'spock':
            print("Paper disproves Spock.")
            self.cpu_points+=1
        
        elif self.cpu_choice == 'spock' and self.player1 == 'rock':
            print("Spock vaporizes Rock.")
            self.cpu_points+=1
        
        else:
            if self.player1 == self.cpu_choice:
                print("Tie try again")


        
    def repeat_till_over(self):
        while True:
            if self.player1_points<2 and self.cpu_points<2:
                self.players_choice()
                self.point_check()
                print(f"You have {self.player1_points} points and the cpu has {self.cpu_points} points")


            elif self.player1_points == 2:
                print("Player wins")
                quit()

            else:
                print("Cpu wins")
                quit()
                        


                
