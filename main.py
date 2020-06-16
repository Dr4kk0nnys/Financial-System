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

        # TODO: Return the "%.2f" % percentage of the month
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
        # Show the "%.2f" % percentage of each item
            -> Get the total profit ( 100 )
            -> Show how much % you've earned per item ( 10 % )

            -> Get the total debt ( 100 )
            -> Show how much % you've payed per item ( 10 % )
        '''
        if (user_input[0] == 'month' and user_input[1] == 'analysis' and len(user_input) == 3):

            def get_month_analysis(query_name):

                query = self.main_database.get_month_balance(
                    int(user_input[2]))
                response_query = query[query_name]

                # profit first
                total_profit = 0
                for profit in response_query:
                    total_profit += float(profit.get('value'))

                sanitized_profits = []
                for i in range(len(response_query)):

                    response_name = response_query[i].get('name')
                    total_value = 0
                    for j in range(len(response_query)):

                        # secondary response will hold the value to add
                        secondary_response = response_query[j]

                        if (response_name == secondary_response.get('name')):
                            value = float(secondary_response.get('value'))
                            total_value += value

                    '''
                    # final query will contain the final value to be added
                    # the have been added flag will hold the information
                    #   -> of whether or not it has been already added
                    #   -> if so, it won't add it, since it's value will be True
                    '''
                    final_query = {'name': response_name, 'value': total_value}

                    have_been_added = False
                    for element in sanitized_profits:
                        if (element.get('name') == response_name):
                            have_been_added = True

                    if (have_been_added == False):
                        sanitized_profits.append(final_query)

                # it will print the percentage of each item of the total profit
                # if the total profit is 100, and a specific item has the value of 10
                # it will print: 'item_name: 10%'
                text = ''
                text += '--- ' + query_name.capitalize() + ':\n'
                for value in sanitized_profits:
                    item_profit = float(value.get('value'))

                    percentage = item_profit / total_profit * 100
                    text += f'{value.get("name")}: R$ {value.get("value")}   ({"%.2f" % percentage}%) \n'

                text += f'\nTotal: R$ {total_profit}\n'
                print(text)

            get_month_analysis('profits')
            get_month_analysis('debts')

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
