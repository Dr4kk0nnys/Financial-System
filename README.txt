# - Template:
    Option_1: 
        [ 1 ]: Add profit
        [ 2 ]: Remove profit
        [ 3 ]: Update profit

        [ 4 ]: Add debt
        [ 5 ]: Remove debt
        [ 6 ]: Update debt

        [ 7 ]: Read profit's database
        [ 8 ]: Read debt's database
        [ 9 ]: Leave

    Option_2:
        Add value: ['+ R$ 20' or '- R$ 10']
        Product code: ['001' or '002']

    Option_3:
        > '+ R$ 200 001'

    -> Going with Option_3 as default, but also with Option_2 if the user prefer's it


# - First step:

    A - Recreate the bussiness system, making it more like a financial system.
    B - The concept will be the exact same, with few differences about the way to store data, also, it will be slightly different, in math bases
    C - It will store the date when you saved the information: ( '+ R$ 20  26/01/2020' -> Rough concept )
    D - It will have methods that show the balance so far, the month's balance, etc ...
    E - It must show how the financial performance is
    F - Search for financial values, financial terms and how to properly show them
    G - Show percentages
    H - Work on methods to help you with sales

        -> 1. Work on the 'profit for sale/unity'
        -> 2. Work on the 'How much i wasted and how much i earned at which day' ( rough concept: '+ R$ 20  26/01/2020 001', '- R$ 100  25/01/2020 001' )
            -> 001: Would be the code for an item i would sell ( let's say a piece of shirt, for example )
            -> + R$ 20: Would be the TOTAL value, so i would've profited R$ 5 in this piece
            -> - R$ 100: Would be the TOTAL value i paid out for the pieces ( 6 pieces and other stuff )
        -> 3. Work on the 'every time i sell a product, it's value increases' 
            -> If i sell 20 smartwatches in a month, and 4 pieces of shirt, the smartwatch sale_quantity would be 20, and pieces_of_shirt_quantity would be 4
        -> 4. Make an easy to read method, that returns how much you earned with each item:
            -> You sold 40 pieces of shit, and earned R$ 190 of profit
            -> You sold 2 smartwatches, and earned R$ 200 of profit
    
    I - Work on the 'where is my money going' function ( show like: You've spent R$ 100 on 001, R$ 300 on Luz, etc ... )
        -> Add a method where it also shows the percentage of the total cost
            - You've spent R$ 100 ( 21% of your total income on Luz )
            - You've spen R$ 20 ( 11.3 % of your total income on 001 ), 001 could also be translated into the actual product name
    J - Instead of saving things like '001' or '002' save it with the real name ( Moletom, Smartwatch, Luz, Comida )

# - Databases:

    1. The first database will be called 'profit_and_debt':
        # - It will hold all the values, such as '+ R$ 200 001', '- R$ 10 004'
        # - NOTE: it will automatically add the date, so actually it will be something like '- R$ 20 001 26/02/2020'

        # - User typed: '- R$ 20 001'
        # - Saved in the database: '- R$ 20 001 26/02/2020'

        # - It will have an option to sort through date, item value ( 001, 002, ... ), and profit/debt

    2. The second database will be called 'product_sales_info':
        # - It will hold the number of sells each item has, such as '001 being the piece of shirt', it will have a 'prefixed value', such as :

            # - '001: 25'
            # - '002: 31'
            # - '003: 102'
            # - '004: 26'

        # - Every time the user adds something to the main database, the second one get's it's number increased
            -> User type '+ R$ 200 001'
            -> Previous value of 001: '25', new value of 001: '26'

