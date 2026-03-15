import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = resources 
cashier_instance = recipes




def main():
    while True:
        action = input("What would you like? (small/ medium/ large/ off/ report): ")
        sand_type = {action: SandwichMaker(action)}
        if action == "off":
            print("The machine has been turned off!")
            break
        elif action == "report":
            print(resources)
        else:
            sand_type[action] = SandwichMaker(sand_type[action])
            if sand_type[action].check_resources(recipes[action]["ingredients"]):
                money = sand_type[action].process_coins()
                if money < 0:
                    break
                sand_type[action].transaction_result(money, recipes[action]["cost"])
                sand_type[action].make_sandwich(recipes[action]["ingredients"], resources)
            else:
                print("There are not enough resources.")

if __name__=="__main__":
    main()


