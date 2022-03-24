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
        print(f"--- Insert {a.side.value} {a.quantity}@{a.price} on {self.name}")
        #Check Execution
        while self.Check_execution():
            self.Execution()
        #print book
        print (self.UI())
    
    
    def Check_execution(self):
        if not self._buy or not self._sell:
            return False
        if self._buy[0].price>=self._sell[0].price:
            return True
        else:
            return False
