class Database():

    def __init__(self, database_name):

        # name needs to have '.txt' at the end
        self.database_name = database_name

    # appends a new data to the database
    def write(self, data):

        file = open(self.database_name, 'a')
        file.write(str(data) + '\n')

        print('Successfully saved into the database! [200]')

    # return the query with all the data inside the database
    def read(self):

        file = open(self.database_name, 'r')
        lines = file.readlines()

        for i in range(len(lines)):
            date = lines[i].split(' ')[-1].strip()
            value = ' '.join(lines[i].split(' ')[:-1])

            if (value[0] == '-'):
                print(f'{date}: \033[1;31;48m{value}\033[0m')
                continue

            print(f'{date}: \033[92m{value}\033[0m')

    # return the query with all the matches inside the database
    def read_(self, value):
        file = open(self.database_name, 'r')
        lines = file.readlines()

        for i in range(len(lines)):
            if (value in lines[i]):

                date = lines[i].split(' ')[-1].strip()
                value_ = ' '.join(lines[i].split(' ')[:-1])

                if (value_[0] == '-'):
                    print(f'{date}: \033[1;31;48m{value_}\033[0m')
                    continue

                print(f'{date}: \033[92m{value_}\033[0m')

    # removes the value inside the index
    def delete(self, index):

        if (self.check_index(index) == False):
            return print('Invalid index! [204]')

        file = open(self.database_name, 'r')
        lines = file.readlines()

        # if it's a valid index
        if (len(lines) > int(index)):
            del lines[int(index)]
        else:
            return print('Invalid index! [204]')

        # clean the database
        file = open(self.database_name, 'w')

        for line in lines:
            file.write(line)

        print('Successfully removed from the database! [200]')

    # changes the value inside the index
    def update(self, index, new_value):

        if (self.check_index(index) == False):
            return print('Invalid index! [204]')

        file = open(self.database_name, 'r')
        lines = file.readlines()

        # if it's a valid index
        if (len(lines) > int(index)):
            lines[int(index)] = str(new_value) + '\n'
        else:
            return print('Invalid index! [204]')

        # clean the database
        file = open(self.database_name, 'w')

        for line in lines:
            file.write(line)

        print('Successfully updated into the database! [200]')

    # get_serial will return the serial value for the new query, and increase itself's value
    def get_serial(self):

        file = open('.serial.txt', 'r')
        lines = file.readlines()

        index = 1
        if (self.database_name == 'clients.txt'):
            index = 0

        result = int(lines[index])
        lines[index] = result + 1

        file = open('.serial.txt', 'w')

        file.write(str(lines[0]).strip('\n') +
                   '\n' + str(lines[1]).strip('\n'))

        return lines[index]

    def check_index(self, index):
        if (index == ''):
            return False
        try:
            int(index)
        except:
            return False

        return index

    def get_month_balance(self, month=1):

        # checking if the month exist
        if (month >= 1 and month <= 12):
            with open('profit_and_debt.txt', 'r') as file:
                lines = file.readlines()

                values = []
                for line in lines:
                    # db_month will always be the second index ([1])
                    db_month = int(line.split('/')[1])

                    if (db_month == month):

                        # value will always be the third index ([2])
                        # and the first index is the '+' or '-' ( negative or positive )
                        value = float(line.split(' ')[0] + line.split(' ')[2])
                        values.append(value)

                self.read_(f'/{str(month)}/')

                total = self.get_total_income(values)
                painted_total = self.get_painted_value(total)
                print(f'Month total balance: R$ {painted_total}')

                return

        # TODO: Instead of raising an exception, think of another method to show case the error
        raise 'Invalid Month'

    def get_total_income(self, values=[]):

        total = 0
        for value in values:
            total += value

        return total

    # return the value, painted ( green if positive, red if negative )
    def get_painted_value(self, value=0.0):

        # green
        if (value >= 0):
            return f'\033[92m{value}\033[0m'
        else:
            # red
            return f'\033[1;31;48m{value}\033[0m'


if __name__ == '__main__':

    database = Database('orders.txt')

    # database.write('This is index 0')
    # database.write('This is index 1')
    # database.write('This is index 2')
    # database.write('This is index 3')

    # database.read()

    # database.delete(0)

    # database.update(0, 'This is the new index 0')

    # print(database.get_serial())
