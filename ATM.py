for i in range(101):

    amount = 10000
    import random
    otp= random.randrange(000,999)
    print(otp)
    print ("enter otp")
    o = eval(input())
    if o==otp:
        print('''enter 1 for withdraw      
        2 for deposit
        3 check balance''')
        a=eval(input())
        if a==1:  
            print("enter the amount to withdraw")
            w=eval(input())
            if w  <=amount:
              total = amount-w
              print(total)
            else:
                print("insuficent fund")
        elif a==2:
            print("enter the amount to deposit")
            d=eval(input())
            total = amount+d
            print(total)
        else:
            print("total balance")
            print(amount)
    else:
        print("invalid")   

                






