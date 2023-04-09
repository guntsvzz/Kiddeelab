class BankAccount:
  def __init__(self, account_number, balance):
    self.__account_number = account_number #public to private
    self.__balance = balance

  def get_account_number(self):
    return f'Account Number : {self.__account_number}'

  def get_balance(self):
    return f'Balance : {self.__balance:,.2f}'

  def deposit(self, amount):
    self.__balance += amount

  def withdraw(self, amount):
    if amount > self.__balance:
      print('Insufficient funds')
    else:
      self.__balance -= amount

# Create an instance of the BankAccount class
my_account = BankAccount("123456", 2000.5)

# Try to access the account number and balance directly
# print(my_account.__account_number) # This will raise an AttributeError
# print(my_account.__balance)  # This will raise an AttributeError

# Access the account number and balance using the public methods
print(my_account.get_account_number())  # Output: "123456"
print(my_account.get_balance()) # Output: 2000.5

# Make a deposit and a withdrawal using the public methods
my_account.deposit(500)
print(my_account.get_balance()) # Output: 2500.5

my_account.withdraw(2000)  # Output: "Insufficient funds"
print(my_account.get_balance())  # Output: 500.5

my_account.withdraw(600)
print(my_account.get_balance())  # Output: 500.5
