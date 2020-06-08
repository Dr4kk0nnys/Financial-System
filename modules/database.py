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
