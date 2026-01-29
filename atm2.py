import random
import smtplib

amount=10000
print("welcome to ATM")
print("press 1 for deposit\npress 2 for widrawal\npress 3 for check balance")
choice=int(input())
if choice==1:
    purpose="deposit"
elif choice==2:
    purpose="withdrawal"
elif choice==3:
    purpose="check balance"
else:
    purpose="invalid choice"
    exit()

    # User se email input
user_email = input("Enter your email: ")        

# OTP generate (6 digit)
otp = random.randint(100000, 999999)

# Sender details
sender_email = "your email"
sender_password = "your password"  # Gmail App Password

# Email message
message = f"""Subject: ATM {purpose} Verification

Your OTP for {purpose} is: {otp}"""
# Email send
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password) 
server.sendmail(sender_email, user_email, message)
server.quit()

print("OTP sent successfully for your ATM", purpose)

user_email_otp = int(input("Enter OTP: "))
if user_email_otp == otp:
    if choice==1:
        print("enter amount to deposit")
        deposit_amount=int(input())
        amount+=deposit_amount
        print("your balance is:", amount)
    elif choice==2:
        print("enter amount to withdraw")
        withdraw_amount=int(input())
        if withdraw_amount<=amount:
            amount-=withdraw_amount
            print("your balance is:", amount)
        else:
            print("insufficient balance")
    elif choice==3:
        print("your balance is:", amount)
else:
    print("Invalid OTP ❌")