
from enum import Enum

game_ended = Enum('game_ended', 'NOBODY_WON PLAYER_WON')

class Game():

    """
    Basically a class for TikTakTo.
    """

    def __init__(self,__field=
                                [["-"], ["-"], ["-"], 
                                 ["-"], ["-"], ["-"],
                                 ["-"], ["-"], ["-"]]
                                            ):


        self.__field =  __field

        self.__players = ["x", "o"]




    def __get_input(self, player): 
        """A function which takes the input of the players.

        Parameters:
        ----------
        player: A string with 'x' or 'o'. -> (str)


        Returns:
        --------
        (playerposition, Bool): A tuple with playerposition and a bool. -> (int, bool)
        """

        
        player_position = input()

        if self.__check_player_input(player_position):
            return (int(player_position), True)

        return (0, False)




    def __check_player_input(self, input):
        """A function which checks if the input of the player is valid for the game.

        Parameters:
        ----------
        input: A number in a string. -> (str)


        Returns:
        --------
        Bool 
        """

        if input in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            return True

        
        return False



    def __put_player_position(self, player, position):
        """A function which puts the players icon into the game field.

        Parameters:
        ----------
        player: String with players icon: 'x' or 'o'. -> (str)
        position: Wished game postion as a int. Number can range between 0 and 8. -> int


        Returns:
        --------
        Bool
        """

        if self.__field[position][0] == "-":
            self.__field[position][0] = player
            return True

        
        elif self.__field[position][0] == "x" or self.__field[position][0] == "o":
            return False

        

        


    def __check_column(self):
        """A function which checks if a player filled a column.

        Parameters:
        ----------
        None


        Returns:
        --------
        Bool
        """

        for player in self.__players:
            for index in range(0, 2):
                if player in self.__field[index][0] and player in self.__field[index+3][0] and player in self.__field[index+6][0]:
                    return True


    def __check_row(self):
        """A function which checks if a player filled a row.

        Parameters:
        ----------
        None


        Returns:
        --------
        Bool
        """
        for player in self.__players:
            for index in range(0, 9, 3):
                if player in self.__field[index][0] and player in self.__field[index+1][0] and player in self.__field[index+2][0]:
                    return True


    def __check_diagonal(self):
        """A function which checks if a player filled a diagonal.

        :param None : None
        :type data: None

        :return: None.
        :rtype: None
        """
        for player in self.__players:
            if player in self.__field[0][0] and player in self.__field[4][0] and player in self.__field[8][0]:
                break
            
            elif player in self.__field[2][0] and player in self.__field[4][0] and player in self.__field[6][0]:
                self.__send_victory_notification(player)
                break




    def __send_victory_notification(self, player):
        """A function which sends a victory message to the player who won.

        Parameters:
        ----------
        player: Players icon as a string: 'x' or 'o' -> (str)



        Returns:
        --------
        None
        """
        print(f'{player} has won the game! Congratulation!')




    def __get_input_loop(self, player):
        """A function which puts another function: self.__get_input in a loop. If player
        puts wrong number or char then self.__get_input will be called to ask the player again.

        Parameters:
        ----------
        player: Players icon as a string: 'x' or 'o' -> (str)



        Returns:
        --------
        player_input[0]: Players requested position as an int. -> (int)
        """

        i = 0

        print(f'{player} its your turn! Please give your position: ')

        while i < 1:

            
            player_input =  self.__get_input(player)

            if player_input[1]:
                return player_input[0]

            print("Position not valid. Please give a position between 0 and 8!")



    def __handle_player_position(self, player):
        """A function which puts self.__get_input_loop, self.__get_input and 
        self.__put_player_position into a loop. To ensure if the players put wrong 
        input, the mention function can be called again.


        Parameters:
        ----------
        player: Players icon as a string: 'x' or 'o' -> (str)



        Returns:
        --------
        Bool
        """
        i = 0

        while i < 1:

            player_position  = self.__get_input_loop(player)

            if self.__put_player_position(player, player_position):
                return True


            print("Position is already used! Please select another won!")




    def run(self):
        """A functin which starts the game.


        Parameters:
        ----------
        None

        Returns:
        --------
        None
        """

        print("Welcome to TikTakTo!")

        round = 0
        while round <= 8:
            print(f'Runde: {round}')
            print("="*20)
            

            for player in self.__players:

                print(self.__field)

                if self.__handle_player_position(player):

                    if self.__check_row() or self.__check_column() or self.__check_diagonal():
                        self.__send_victory_notification(player)
                        gameEnded = True
                        break
            
            if game_ended == game_ended.PLAYER_WON:
                break
                      
            round += 1
        if game_ended == game_ended.NOBODY_WON:
            print("="*20)
            print("unfortunately nobody won!")

                





            

            
                








def test():
    g = Game()
    g.run()



"""test_field = [["o"], ["-"], ["o"], 
              ["x"], ["o"], ["x"],
              ["o"], ["x"], ["o"]]"""

test()