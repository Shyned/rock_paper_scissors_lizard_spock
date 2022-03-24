from random import choice
from player import Player



#place holder class name for human ai
class Human_Ai(Player):
    def __init__(self) :
        super().__init__()
        self.player_choice =''
        self.cpu_choice = ''

    #logic for choice in this file
    def players_choice(self):
        while self.player_choice.lower() not in self.choice:
            print(self.choice)
            self.player_choice = input("Please enter a choice from the list: ")
            
        #robot pick random item from list
        else:
            self.cpu_choice = choice(self.choice)
            print(f"The cpu has picked{self.cpu_choice}")
   
    

        
        