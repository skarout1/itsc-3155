class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        large = float(input("Please enter coins.\nHow many large dollars?: "))
        half = float(input("How many half dollars?: "))
        quarters = float(input("How many quarters?: "))
        nickles =  float(input("How many nickles?: "))
        total = ((large * 100) + (half * 50) + (quarters * 25) + (nickles * 5))/100
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        change = coins - cost
        if change > 0:
            return print(f"Here is ${change:.2f}")
        else:
            return print("You do not have enough coins")