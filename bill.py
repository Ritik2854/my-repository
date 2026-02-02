def bill():
    order_id = int (input("enter the order id"))
    product_name =input("enter the product name")
    price= float(input("enter the product price"))
    quantity=int(input("enter the quantity"))
    amount=price*quantity
    id=str(order_id)
    name=str(product_name)
    p_price=str(price)
    quatity=str(quantity)
    ext=".txt"
    s=id +ext
    x=open(s,"w")
    y=x.write(f'''id{order_id},name{product_name},p_price{price},quantity{quantity},total{amount}''')
    x.close
bill()
sql=insert into bill(order_id,product_name,price,quantity,amount)values("%s","%s","%s","%s","%s")
query