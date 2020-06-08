# - It's going to have a terminal with the options:
    Client options ( primary database ) {
        [ 1 ] - Add client 
        [ 2 ] - Remove client
        [ 3 ] - Update client 
    }

        -> The clients.txt database will have the following terminology:
            1. {
                'name': name,
                'cpf': cpf,
                'phone_number': phone_number,
                'adress': adress,
                'client_id': client_id,
            }

            * Client_id is also the client's serial number

    Order options ( secondary database ) {
        [ 4 ] - Add order 
        [ 5 ] - Remove order 
        [ 6 ] - Update order 
    }

        -> The orders.txt database will have the following terminology:
            2. {
                'owner_id': owner_id,
                'specifications': specifications,
                'problem': problem,
                'order_id': order_id
            }

            * Specifications will contain the product details, such as model, color, and if it's a desktop or a notebook
    
    Other options {
        [ 7 ] - Read Client's database
        [ 8 ] - Read Order's database
        [ 9 ] - Leave
    }

        -> {
            * Read both client's and order's database will allow the user to quickly search through the database with shortcuts ( like the name or the client_id value )
        }
