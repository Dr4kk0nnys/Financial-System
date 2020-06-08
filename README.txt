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


# - First step:

    A - Recreate the bussiness system, making it more like a financial system.
    B - The concept will be the exact same, with few differences about the way to store data, also, it will be slightly different, in math bases
    C - It will store the date when you saved the information: ( '+ R$ 20  26/01/2020' -> Rough concept )
    D - It will have methods that show the balance so far, the month's balance, etc ...
    E - It must show how the financial performance is
    F - Search for financial values, financial terms and how to proporly show them
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
