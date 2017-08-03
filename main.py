class Coins:
    """ Class contadef main():
  print "Hello World!"

  # instatiate Coins class
  coins = Coins()

  # call the Coins class test functions
  test_getset_quarters(coins)
  test_getset_dimes(coins)
  test_getset_nickels(coins)
  test_getset_pennies(coins)
  test_get_total(coins)ins coins values and number """
    
    def __init__(self):
        self.quarters_value  = 25
        self.dimes_value     = 10
        self.nickels_value   = 5
        self.pennies_value   = 1
    
        self.quarters_number = 0
        self.dimes_number    = 0
        self.nickels_number  = 0
        self.pennies_number  = 0

    def set_quarters(self, quarters):
      self.quarters_number = quarters

    def get_quarters(self):
      return self.quarters_number
  
    def set_dimes(self, dimes):
      self.dimes_number = dimes

    def get_dimes(self):
      return self.dimes_number
  
    def set_nickels(self, nickels):
      self.nickels_number = nickels

    def get_nickels(self):
      return self.nickels_number
  
    def set_pennies(self, pennies):
      self.pennies_number = pennies

    def get_pennies(self):
      return self.pennies_number

    def get_total(self):
      total = 0
      total += self.quarters_value * self.quarters_number
      total += self.dimes_value    * self.dimes_number
      total += self.nickels_value  * self.nickels_number
      total += self.pennies_value  * self.pennies_number
      return total

    def print_status(self):
      print("number of quarters : {}").format(self.quarters_number)
      print("number of dimes    : {}").format(self.dimes_number)
      print("number of nickels  : {}").format(self.nickels_number)
      print("number of pennies  : {}").format(self.pennies_number)

class Cash_Register:
  def __init__(self):
    self.coins = Coins()
    #self.bills = Bills()

    def print_status(self):
      self.coins.print_status()
      #self.bills.print_status()

    def print_receipt(self):
      print("You did indeed buy a thing! Here's a receipt")
      
    def calculate_coins_to_return(coins_tendered, coins_due):
      print ("todo")

    def render_transaction(self, coins_tendered, coins_due):
      amount_overpaid = coins_tendered - coins_due

      #  check if they overpaid? give change
      if amount_overpaid > 0:
          coins_to_return = calculate_coins_to_return(coins_tendered, coins_due)

      #  check if they underpaid?  DO NOT LET THIS GO. YOU ARE BEING SHORTED MONIES.
          if amount_overpaid < 0:
             return None

      #  check if no change is due
          if amount_overpaid == 0:
              print ("No Change Due")

      #  print a receipt.
          self.print_receipt()
           
    # print status
    #coins.print_status()

def test_getset_quarters(coins):
  coins.set_quarters(2)
  quarters = coins.get_quarters()
  #print "quarters = {}".format(quarters)
  #print "quarters = %s" %(quarters)
  #print "quarters = " + str(quarters)
  if quarters == 2:
    print ("Test PASS")
  else:
    print ("Test FAIL")

def test_getset_dimes(coins):
  coins.set_dimes(3)
  dimes = coins.get_dimes()
  #print "dimes    = {}".format(dimes)
  if dimes == 3:
    print ("Test PASS")
  else:
    print ("Test FAIL")

def test_getset_nickels(coins):
  coins.set_nickels(1)
  nickels = coins.get_nickels()
  #print "nickels  = {}".format(nickels)
  if nickels == 1:
    print ("Test PASS")
  else:
    print ("Test FAIL")

def test_getset_pennies(coins):
  coins.set_pennies(4)
  pennies = coins.get_pennies()
  #print "pennies  = {}".format(pennies)
  if pennies == 4:
    print ("Test PASS")
  else:
    print ("Test FAIL")

def test_get_total(coins):
  
  if coins.get_total() == 89:
    print ("Test PASS")
  else:
    print ("Test FAIL")

def main():
  print ("Hello World!")

  # instatiate Coins class
  coins = Coins()

  # call the Coins class test functions
  test_getset_quarters(coins)
  test_getset_dimes(coins)
  test_getset_nickels(coins)
  test_getset_pennies(coins)
  test_get_total(coins)

if __name__== "__main__":

    main()
