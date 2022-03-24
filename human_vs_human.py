from player import Player





class Human_Vs_Human(Player):
    def __init__(self) :
        #add a counter for each player
          super().__init__()
          self.player1 = ""
          self.player2 =""


    #loop to check if player pick item in list 
    def players_pick(self):
        #player 1 pick 
        while self.player1.lower() not in self.choice:
            print(self.choice)
            self.player1 = input("Please enter a choice from the list: ")
        else:
            #if player one pick is in list then player 2 pick
            while self.player2 not in self.choice:
                self.player2 = input("Please enter a choice from the list: ")

            else:
                pass
    #possibly include a loop to with a counter to check if either player has won
    def point_check (self):
        pass
    

    #repeat cycle until either player has won
    def repeat_till_over(self):
        while self.player1 <2 or self.player2<2:
            self.players_pick()
            
            self.point_check()

        else:
            print("winner")
            quit()

    