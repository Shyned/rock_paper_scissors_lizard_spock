from player import Player





class human_vs_human(Player):
    def __init__(self) :
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


    

test=human_vs_human()
test.players_pick()

    