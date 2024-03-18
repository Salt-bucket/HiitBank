from account import Account
from db import customer_db
import re
import hashlib
def register():
    while True:
        try:
            print("REGISTRATION\n\n")
            bvn_response = input("Please enter your BVN or leave blank if you do not have one: ")
            if len(bvn_response) == 0:
                acc = Account()
            else:
                acc = Account(bvn=bvn_response)

            acc.set_nin(input("NIN: "))
            acc.set_fname(input("First name: "))
            acc.set_lname(input("Last name: "))
            acc.set_phone_no(input("Phone No:"))
            acc.set_email(input("Email: "))
            acc.set_passcode(input("New Passcode: "))
            acc.set_pin(input("4 digit pin: "))
            acc.set_address(input("Residential Address: "))

            customer_db[acc.get_account_no()] = acc

            print(f"""
            User created successfulyl
            Your Account Number is {acc.get_account_no()}
            Your BVN is {acc.get_bvn()}
            Your Address is {acc.get_address()}
            
            """)
            break
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except Exception as ex:
            print(f"Other Exception: {ex}")
pass


def login():
    while True:
        try:
            email = input("Email address: ")

            pattern = "^[a-zA-Z0-9\\-\\.\\_]*@[a-zA-Z]*\\.(com|org|net)$"
            assert re.search(pattern, email) is not None, "Invalid Email Format"

            user_accounts_with_email = [account for account in customer_db.values() if account.get_email() == email]

            assert len(user_accounts_with_email) == 1, "Email address was not found"

            user_account = user_accounts_with_email[0]

            passcode = input("Enter passcocde: ")
            assert passcode == user_account.get_passcode(), "Invalid Passcode Provided"

            print("LOGIN SUCCESSFUL!")


        except AssertionError as e:
            print("Assertion Error: " + str(e))
        except Exception as ex:
            print(" Exception: " + str(e))
pass