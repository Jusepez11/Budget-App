class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def create_spend_chart(self, categories):
    pass 

  def deposit(self, amount, description=""):
    #adding a deposit to the ledger
    self.ledger.append({"amount": amount, "description": description})
  
  def check_funds(self, amount):
    if self.get_balance() >= amount:
        return True
    
    return False

  def get_balance(self):
    balance = 0
    #Loping around the ledger to add all the transactions
    for i in range(len(self.ledger)):
        balance += self.ledger[i]["amount"]

    return balance

  def withdraw(self, amount, description=""):    
    #Checks if the balance is equal or higher than the amount that will be withdrawn
    if self.check_funds(amount):
        self.ledger.append({"amount": amount * -1, "description": description})
        return True
    return False

  def transfer(self, amount, bCategory):
    #if there are funds the transfer will be made and the function will return true, otherwise it will return false
    if self.check_funds(amount):
      self.withdraw(amount, ("Transfer to %s" % bCategory))
      self.deposit(amount, ("Transfer from %s" % bCategory))
      return True
    return False