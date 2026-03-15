class SadikBank:
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self._routing_number = routing_number
    
    #def deposit(self):


    def withdrawl(self, withdrawl_ammount):
        if self.current_balance < self.minimum_balance:
            print("Can not withdrawl funds!")
        else:
            self.current_balance -= withdrawl_ammount
            print("Balance after withdrawl: $", int(self.current_balance))

    def deposit(self, deposit_ammount):
        self.current_balance += deposit_ammount
        print("Balance after deposit: $", int(self.current_balance))
    def print_customer_information(self):
        print("Name: " + self.customer_name)
        print("Balance: $", int(self.current_balance))
        print("Routing Number: ", str(self._routing_number))
        print("Account Number: ", str(self._account_number)) 