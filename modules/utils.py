def show_options():

    print('''
[ 1 ] - Add client
[ 2 ] - Remove client
[ 3 ] - Update client

[ 4 ] - Add order
[ 5 ] - Remove order
[ 6 ] - Update order

[ 7 ] - Read Client's database
[ 8 ] - Read Order's database
[ 9 ] - Leave
''')


def get_option_value(option_value):

    if (option_value == '1'): print('[Add client] ', end='')
    elif (option_value == '2'): print('[Remove client] ', end='')
    elif (option_value == '3'): print('[Update client] ', end='')

    elif (option_value == '4'): print('[Add order] ', end='')
    elif (option_value == '5'): print('[Remove order] ', end='')
    elif (option_value == '6'): print('[Update order] ', end='')

    elif (option_value == '9'): print('Leave')
