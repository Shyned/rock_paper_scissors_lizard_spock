from human_ai import Human_Ai
from human_vs_human import Human_Vs_Human
#import for user classes for game mode pick

#made oject for class used on line 41  and 37
two_players = Human_Vs_Human
one_player = Human_Ai()



class game_on():
    def __init__(self):
        self.answer_list =["y","n"]
        self.display_welcome()


    def display_welcome(self):
        print("Welcome To Rock, Paper, Scissor, Lizard, Spock!!")


    def lets_get_it_on(self):
        question = input("Do you want to play (y/n):")
        while question not in self.answer_list:
            question = input("Do you want to play (y/n):")
        #if n then quit
        else:
            if question == 'y':
                game_mode_list = ["1","2"]
                game_mode = input("Do you want to play Single or Versus (1:Single,2:Versus): ")
                while game_mode not in game_mode_list:
                    game_mode = input("Do you want one or to players (1/2)")

                #if player enters 1 or 2 run player vs player or player vs ai
                else:
                    if game_mode == "1":
                        #needs a method in the human vs ai file to run full game
                        one_player

                        
                    else:
                        two_players.repeat_till_over
                        
            
            else:
                print("Goodbye")
                quit()
            

