class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.budget = 0

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    self.budget += amount
                
  def check_funds(self, amount):
    if self.budget >= amount:
      return True
    else:
      return False

  def withdraw(self, amount, descript = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": 0 - amount, "description": descript})
      self.budget -= amount
      return True
    else:
      return False

  def get_balance(self):
    return self.budget

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  def __str__(self):
    line = self.name.center(30, "*")
    for item in self.ledger:
      amt = "{:.2f}".format(float(item["amount"]))
      line += "\n" + item["description"][:23].ljust(23) + amt.rjust(7)
    bud = "{:.2f}".format(float(self.budget))
    line += ("\nTotal: "+ bud)
    return line


def create_spend_chart(categories): 
  expenses = []
  names = []
  totspent = 0

  for cate in categories:
    spent = 0
    for entry in cate.ledger:
      if entry["amount"] < 0:
        spent -= entry["amount"]
    expenses.append(spent)
    names.append(cate.name)
    totspent += spent

  perc = []
  for spent in expenses:
    perc.append(spent/totspent*100)

  rows = ["Percentage spent by category",]
  for take in range(100, -1, -10):
    line = ("\n" + " "*(3-len(str(take))) + str(take) + "| ")
    for num in perc:
      if num >= take:
        line += "o  "
      else:
        line += "   "
    rows.append(line)

  rows.append("\n    " + "-"*(3*len(perc)+1))

  maxlen = 0
  for name in names:
    if len(name) > maxlen:
      maxlen = len(name)
  for idx in range(maxlen):
    line = "\n     "
    for name in names:
      try:
        line += name[idx] + "  "
      except:
        line += "   "
    rows.append(line)

  insta = ""
  for row in rows:
    insta += row

  return insta
