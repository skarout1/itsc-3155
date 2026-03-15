from bankAccount import SadikBank

class Checking(SadikBank):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self._routing_number = routing_number

    def transfer(self, transfer_ammount, transfer_to_number):
        transfer_limit = 2500
        print("Transfer limit is: $", transfer_limit)
        if(transfer_ammount > transfer_limit):
            print("Transfer ammount is too much")
        else:
            self.current_balance -= transfer_ammount
            print(transfer_ammount, " transfered from account ", self._account_number, " to account ", transfer_to_number)
