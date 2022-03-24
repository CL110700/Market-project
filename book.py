from enum import Enum
from texttable import Texttable

class Book:
    def __init__(self,name):
        self._name=name
        self._buy=[]
        self._sell=[]

    def insert_buy(self,quantity,price):
        a=Order(Side.BUY,quantity,price) #order creation
        self._buy.append(a)
        self._buy=sorted(self._buy,key=lambda order: -order.price)
        #Print detail
        print(f"--- Insert {a.side.value} {a.quantity}@{a.price} on {self._name}")
        #Check Execution
        while self.Check_execution():
            self.Execution()
        #print book
        print (self.UI())
    
    def insert_sell(self,quantity,price):

        a=Order(Side.SELL,quantity,price) #order creation
        self._sell.append(a) # add order in the book
        #Sort the orders
        self._sell=sorted(self._sell,key=lambda order: order.price)
        #Print detail
        print(f"--- Insert {a.side.value} {a.quantity}@{a.price} on {self._name}")
        #Check Execution
        while self.Check_execution():
            self.Execution()
        #print execution and retrieve data
        #print book
        print(self.UI())

    def Check_execution(self):
        if not self._buy or not self._sell:
            return False
        if self._buy[0].price>=self._sell[0].price:
            return True
        else:
            return False

    def Execution(self):
        #Print transaction 
        n_transactions=min(self._buy[0].quantity,self._sell[0].quantity)
        print(f"Execute {n_transactions} at {self._buy[0].price} on {self._name}")
        # REtrieve
        self._buy[0].quantity-=n_transactions
        self._sell[0].quantity-=n_transactions
        # Delete
        if  self._buy[0].quantity==0:
            del self._buy[0]
        if  self._sell[0].quantity==0:
            del self._sell[0]
    
    def UI(self):
        t=Texttable()
        t.header(["id","Buy","Sell","id"])
        for i in range(max(len(self._buy),len(self._sell))):
            row=[]
            if i>=len(self._buy):
                row.append("")
                row.append("")
            else:
                row.append((self._buy[i].id))
                row.append(str(self._buy[i]))
            if i>=len(self._sell):
                row.append("")
                row.append("")
            else:
                row.append(str(self._sell[i]))
                row.append((self._sell[i].id))
            t.add_row(row)
        return t.draw()

ids=1

class Order:
    def __init__(self,side,quantity,price):
        global ids
        self.side=side
        self.quantity=quantity
        self.price=price
        self.id=ids
        ids+=1

    def __str__(self):
        return (f" {(self.quantity)} @ {self.price}")

class Side(Enum):
    SELL="SELL"
    BUY="BUY"

