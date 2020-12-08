import requests

SHEETY_POST = "_YOUR_SHEETY_POST_URL_"

FIRST_NAME = input("What is your first name?\n> ").capitalize()
LAST_NAME = input("What is your last name?\n> ").capitalize()
first_email = input("What is your email?\n> ").lower()
confirmed_email = input("Type your email again.\n> ").lower()


def email_match():
    if first_email == confirmed_email:
        return True
    else:
        return False


if email_match():
    print(confirmed_email)
    sheet_input = {
        "user": {
            "firstName": FIRST_NAME,
            "lastName": LAST_NAME,
            "email": confirmed_email,
        }
    }
    sheet_post = requests.post(SHEETY_POST, json=sheet_input)
    print("Welcome to the club!")
else:
    print("Sorry email's don't match.")

email_match()