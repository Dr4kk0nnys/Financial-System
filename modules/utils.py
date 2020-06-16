from datetime import datetime


def is_profit(value):

    if value == '+':
        return True

    return False


def get_formated_date():
    date = datetime.now()

    return f'{date.day}/{date.month}/{date.year}'
