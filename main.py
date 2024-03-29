
from tools import *
import initdb

while True:
    user_response = input("""
                Welcome user, what would you like to do today?
                1. Register
                2. Login
                3. Quit
        """)

    if user_response == '1':
        register()
    elif user_response == '2':
        user = login()
        while True:
            response = input(f'''
                Welcome {user.get_fname()}
                
                1. Deposit
                2. Withdrawal
                3. Transfer
                4. Balance Inquiry
                5. BVN Inquiry
                6. Account No Inquiry
                7. Logout
    
    ''')
            if response == '1':
                deposit(user)
            elif response == '2':
                withraw(user)
            elif response == '3':
                transfer(user)
            elif response == '4':
                balance(user)
            elif response == '5':
                bvn_in(user)
            elif response == '6':
                account_no(user)
            elif response == '7':
                print('''
                LOGOUT SUCCESSFUL!
                ''')
                break
            else:
                print("Invalid Input")



    elif user_response == '3':
        print ('Bye Bye')
        break
    else:
        print('Invalid Input')