class Category:

  def __init__(self):
    self.ledger = []

  def create_spend_chart(self, categories):
    pass 

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount):    
    #Checks if the balance is equal or higher than the amount that will be withdrawn
    if check_funds(amount):
        self.ledger.append({"amount": amount * -1})
        return True
    return False

  def get_balance(self):
    balance = 0
    #Loping around the ledger to add all the transactions
    for i in range(len(self.ledger)):
        balance += self.ledger[i]["amount"]

    return balance

  def transfer(self):
    pass
  
  def check_funds(self, amount):
    if get_balance() >= amount:
        return True
    
    return False