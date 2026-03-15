import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker
cashier_instance = Cashier




def main():
    while True:
        action = input("What would you like? (small/ medium/ large/ off/ report): ")
        sandwich_maker_instance = {action: SandwichMaker(action)}
        cashier_instance = {action: Cashier()}
        if action == "off":
            print("The machine has been turned off!")
            break
        elif action == "report":
            print(resources)
        else:
            sandwich_maker_instance[action] = SandwichMaker(sandwich_maker_instance[action])
            if sandwich_maker_instance[action].check_resources(recipes[action]["ingredients"]):
                money = cashier_instance[action].process_coins()
                if money >= data.recipes[action]["cost"]:
                    cashier_instance[action].transaction_result(money, recipes[action]["cost"])
                    sandwich_maker_instance[action].make_sandwich(recipes[action]["ingredients"], resources)
                else:
                    cashier_instance[action].transaction_result(money, recipes[action]["cost"])
                    
            else:
                print("There are not enough resources.")

if __name__=="__main__":
    main()

