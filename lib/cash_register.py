#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity=1):
    self.title = title 
    newTotal = (price * quantity)
    self.last_transaction = newTotal
    self.total += newTotal
    # for each itemAmount we add the title of that Item to the Items LIST/array
    for itemAmount in range(quantity):
      self.items.append(title)

    
  def apply_discount(self):
    if self.discount > 0:

      # alternative 

      # percent = self.discount / 100
      # moneyOff = self.tota * percent
      # self.total = int( self.total - moneyOff)
      self.total = self.total - (self.total * (self.discount/ 100))
      self.total = int(self.total)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total = self.total - self.last_transaction
    
