from modules.database import Database
from modules.utils import *

# TODO: Make the cpf.get() easier
# TODO: Make it error proof ( watch the how to become a better dev video ( https://www.youtube.com/watch?v=g2nMKzhkvxw ))
# TODO: Make a portuguese version ( other git branch )
# TODO: Make a cpf searcher, whenever adding a new client


class System():

    def __init__(self):

        # Initializing both databases
        self.primary_database = Database('clients.txt')
        self.secondary_database = Database('orders.txt')

        show_options()

        while (True):
            response = self.handle_input()

            if (response == False):
                return

    def handle_input(self):

        user_input = input('> ')

        # [ 1 ] - Add client
        # [ 2 ] - Remove client
        # [ 3 ] - Update client

        # [ 4 ] - Add order
        # [ 5 ] - Remove order
        # [ 6 ] - Update order

        # [ 7 ] - Read Client's database
        # [ 8 ] - Read Order's database
        # [ 9 ] - Leave

        get_option_value(user_input)
        # show which option the user choosed

        if (user_input == '1'):

            client_info = self.primary_database.get_client_info()
            self.primary_database.write(client_info)

        elif (user_input == '2'):

            index = input('Index: ')
            self.primary_database.delete(index)

        elif (user_input == '3'):

            index = input('Index: ')
            new_client_info = self.primary_database.get_client_info()

            self.primary_database.update(index, new_client_info)

        elif (user_input == '4'):

            order_info = self.secondary_database.get_order_info()
            self.secondary_database.write(order_info)

        elif (user_input == '5'):

            index = input('Index: ')
            self.secondary_database.delete(index)

        elif (user_input == '6'):

            index = input('Index: ')
            new_order_info = self.secondary_database.get_order_info()

            self.secondary_database.update(index, new_order_info)

        elif (user_input == '7'):

            option = input('CPF or Name: ')
            self.primary_database.read_(option)

        elif (user_input == '8'):

            option = input('Client ID or Order ID: ')
            self.secondary_database.read_(option)

        elif (user_input == '9'):

            return False

        elif (user_input == ''):
            return show_options()

        else:
            return print('NOT SUCCESSFULL QUERY [204]')

        # print('\nSuccessfull query! [200]\n')


if __name__ == '__main__':

    System()
