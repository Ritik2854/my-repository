# def bil():
#     order_id = int(input("enter the order id"))    
import time as t
import mysql.connector


def bill():
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="database", #enter your password
    database="pasword " #enter your database name
    )
    cur = con.cursor()
    order_id=int(input("enter the order id: "))
    product_name=input("enter the product name: ")
    price=float(input("enter the P_Price: "))
    quantity=int(input("enter the Quantity: "))
    amount=price*quantity
    sql = "INSERT INTO bill (Order_id,product_name,price,quantity,amount) VALUES (%s,%s,%s,%s,%s)"
    values = (order_id,product_name,price,quantity,amount)
    cur.execute(sql,values)
    con.commit()
    print("✅ Data successfully inserted into Products table!")

    amount=price*quantity
    name=str(order_id)
    time=t.ctime()
    f = open(name + ".txt", "w")
    data=f.write(f'''
    Time: {time},
    order id: {order_id},
    product name: {product_name},
    Price: {price}
    Quantity: {quantity},
    final amount: {amount}''')
    f.close()
    cur.close()
    con.close()
    

bill()

