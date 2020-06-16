from modules.database import Database
from modules.utils import *
# TODO: Make it error and idiot proof
# TODO: Format this code, and refactor it 1000 times
# TODO: After done formatting this shithole, add a bunch of comments
# TODO: Add a command printer for help


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

        user_input = user_input.split(' ')

        # if the user wants to read the database, and didn't specify any parameters
        # it will print out the entire database
        if (user_input[0] == 'read' and len(user_input) == 1):
            return self.main_database.read()

        # if the user wants to read the database, but specified a parameter
        elif (user_input[0] == 'read'):
            return self.main_database.read_(user_input[1])

        # TODO: Return the percentage of the month
        '''
            0  ~ 30  %: red
            31 ~ 50  %: yellow
            51 ~ 100 %: green
        '''
        # TODO: Error proof: cannot type float value ( it shouldn't )
        # TODO: Error proof: cannot type empty value ( it shouldn't ) ' [space] '
        if (user_input[0] == 'month' and user_input[1] == 'balance' and len(user_input) == 3):

            # printing the entire month
            self.main_database.read_(f'/{user_input[2]}/')

            response = self.main_database.get_month_balance(int(user_input[2]))
            print(f'Month total balance: R$ {response.get("painted_total")}')

        # TODO: Work on the monthly analysis
        '''
        # Show the percentage of each item
            -> Get the total profit ( 100 )
            -> Show how much % you've earned per item ( 10 % )

            -> Get the total debt ( 100 )
            -> Show how much % you've payed per item ( 10 % )
        '''
        if (user_input[0] == 'month' and user_input[1] == 'analysis' and len(user_input) == 3):
            response = self.main_database.get_month_balance(int(user_input[2]))

            # profit first
            total_profit = 0
            for profit in response['profits']:
                total_profit += float(profit.get('value'))

            a = []
            for i in range(len(response['profits'])):

                r = response['profits'][i]

                total_value = 0
                for j in range(len(response['profits'])):

                    r2 = response['profits'][j]

                    if (r.get('name') == r2.get('name')):
                        value_2 = float(r2.get('value'))
                        total_value += value_2

                final_version = f'{r.get("name")} | {total_value}'

                flag = False
                for element in a:
                    if (element.split(' | ')[0] == r.get('name')):
                        flag = True

                if (flag == False):
                    a.append(final_version)

            print(a)

            # print(
            #     f'Name: {r.get("name")}\nOld value: {r.get("value")}')
            # print(
            #     f'New value: {float(r.get("value")) + float(r2.get("value"))}')

            print('\n\n\n\n\n\n')
            for value in response['profits']:
                item_profit = float(value.get('value'))

                percentage = item_profit / total_profit * 100
                print(f'{value.get("name")}: {percentage}%')

        # TODO: Check for Option 2 ( readme.txt )
        # TODO: Add an inspection first, to see if the user_input is right

        # if the user input doesn't has any of the above data
        # it wants to add a key-value to the database
        # it does some checking before and then add's it to the database '''
        if (len(user_input) == 4):
            profit_or_debt = user_input[0]
            value = ' '.join(user_input[1:3])
            product_code = user_input[-1]

            if (profit_or_debt == '+' or profit_or_debt == '-'):
                if ('R$' in value):
                    query = f'{profit_or_debt} {value} {product_code} {get_formated_date()}'
                    self.main_database.write(query)


if __name__ == '__main__':

    System()
