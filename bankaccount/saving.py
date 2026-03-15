from bankAccount import SadikBank

class Saving(SadikBank):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self._routing_number = routing_number

    def intrest(self):
        intrest_ammount = self.current_balance * 1.05
        print("Savings account intrest ammount is: .5%. current balance is: $", self.current_balance, ". After intrest: $", intrest_ammount)