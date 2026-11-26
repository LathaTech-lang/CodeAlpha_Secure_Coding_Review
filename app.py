import os
import hmac

username = input("Enter username: ")
password = input("Enter password: ")

correct_password = os.getenv("APP_PASSWORD")

if correct_password is None:
    print("Login configuration is missing.")

elif username == "admin" and hmac.compare_digest(
    password, correct_password
):
    print("Login Successful!")

else:
    print("Invalid Username or Password")