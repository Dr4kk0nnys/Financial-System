from modules.database import Database
from modules.utils import *


class System():

    def __init__(self):

        self.main_database = Database('profit_and_debt.txt')
        self.secondary_database = Database('product_sales_info.txt')

        while True:

            user_input = input('> ')
            if (user_input.lower() == 'exit'):
                return

            self.handle_input(user_input)

    def handle_input(self, user_input):

        print(user_input)

        # is profit returns True only if the first caracter is a '+'
        # if isProfit(user_input[0]):
        #     print('Fuck this shit is profit')
        # else:
        #     print('Fuck this shit is not profit')

        # TODO: Add an inspection first, to see if the user_input is right
        # TODO: Make a module that automatically get's the date, and already format's it
        # TODO: Print the debt in red on the terminal ( use color code )
        self.main_database.write(user_input)


if __name__ == '__main__':

    System()
