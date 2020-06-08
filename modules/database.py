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
            print(f'Index {i}: {lines[i]}', end='')

    # return the query with all the matches inside the database
    def read_(self, value):
        '''
            TODO: Improve this part of the code, making it more abrassive
            ( search for lower letters, cpf without the dots, etc ...)
        '''

        file = open(self.database_name, 'r')
        lines = file.readlines()

        for i in range(len(lines)):
            if (value in lines[i]):
                print(f'Index {i}: {lines[i]}', end='')

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

    # return the client id automatically
    def get_client_info(self):

        name = input('Name: ')
        cpf = input('CPF: ')
        phone_number = input('Phone number: ')
        adress = input('Adress: ')

        return {
            'name': name,
            'cpf': self.beautify_cpf(cpf),
            'phone_number': phone_number,
            'adress': adress,
            'client_id': self.get_serial()
        }

    def get_order_info(self):

        client_id = input('Client id: ')
        specifications = input('Specifications: ')
        problem = input('Problem: ')

        return {
            'client_id': client_id,
            'specifications': specifications,
            'problem': problem,
            'order_id': self.get_serial()
        }

    def beautify_cpf(self, cpf='000.000.000-00'):

        # format received = 00000000000
        # format returned = 000.000.000-00

        # checking if it's already formated
        if (cpf.count('.') == 2 and cpf.count('-') == 1):
            return cpf

        # wrong cpf format
        if (len(cpf) != 11):
            return print('Wrong cpf! [204]')

        formated_cpf = cpf
        for i in range(3, len(formated_cpf), 4):
            formated_cpf = formated_cpf[:i] + '.' + formated_cpf[i:]

        return formated_cpf[:11] + '-' + formated_cpf[11:]

    def check_index(self, index):
        if (index == ''):
            return False
        try:
            int(index)
        except:
            return False

        return index


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

    print(database.beautify_cpf('00000000000'))
