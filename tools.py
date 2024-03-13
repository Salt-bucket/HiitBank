from account import Account
from db import customer_db
def register():
    while True:
        try:
            bvn_response = input("Please enter your BVN or leave blank if you do not have one: ")
            if len(bvn_response) == 0:
                acc = Account()
            else:
                acc = Account(bvn=bvn_response)

            acc.set_nin(input("NIN: "))
            acc.set_fname(input("First name: "))
            acc.set_lname(input("Last name: "))
            acc.set_email(input("Email: "))
            acc.set_passcode(input("New Passcode: "))
            acc.set_pin(input("4 digit pin: "))
            acc.set_address(input("Residential Address: "))

            customer_db[acc.get_account_no()] = acc

            print(f"""
            User created successfulyl
            Your Account Number is {acc.get_account_no()}
            Your BVN is {acc.get_bvn()}
            
            """)
            break
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except Exception as ex:
            print(f"Other Exception: {ex}")
pass