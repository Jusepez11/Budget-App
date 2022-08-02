class Category:

  def __init__(self):
    self.ledger = []

  def create_spend_chart(self, categories):
    pass 

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self):
    pass

  def get_balance(self):
    pass

  def transfer(self):
    pass
  
  def check_funds(self):
    pass