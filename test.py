import human_ai,human_vs_human
#import for user classes for game mode pick


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
                game_mode = input("Do you want one or to players (1/2)")
                while game_mode not in game_mode_list:
                    game_mode = input("Do you want one or to players (1/2)")

                else:
                    if game_mode == "1":
                        #human vs Ai
                        pass
                        
                    else:
                        #run human vs human
                        pass
            
            else:
                print("Goodbye")
                quit()
            




game = game_on()
game.lets_get_it_on()