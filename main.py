### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if resources["bread"] >= ingredients["bread"] and resources["ham"] >= ingredients["ham"] and resources["cheese"] >= ingredients["cheese"]:
            return True
        else:
            return False

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
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        order_ingredients["bread"] -= sandwich_size["bread"]
        order_ingredients["ham"] -= sandwich_size["ham"]
        order_ingredients["cheese"] -= sandwich_size["cheese"]
        return print(f"{action} sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###

while True:
    action = input("What would you like? (small/ medium/ large/ off/ report): ")
    sand_type = {action: SandwichMachine(action)}
    if action == "off":
        print("The machine has been turned off!")
        break
    elif action == "report":
        print(resources)
    else:
        sand_type[action] = SandwichMachine(sand_type[action])
        if sand_type[action].check_resources(recipes[action]["ingredients"]):
            money = sand_type[action].process_coins()
            if money < 0:
                break
            sand_type[action].transaction_result(money, recipes[action]["cost"])
            sand_type[action].make_sandwich(recipes[action]["ingredients"], resources)
        else:
            print("There are not enough resources.")




