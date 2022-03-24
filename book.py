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
                                                                                            # Print execution + retrieve data
                                                                                                    
                                                                                                            #print book
                                                                                                                    print(self.UI())

