
import data
from cashier import Cashier

class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = data.resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if self.machine_resources["bread"] >= ingredients["bread"] and self.machine_resources["ham"] >= ingredients["ham"] and self.machine_resources["cheese"] >= ingredients["cheese"]:
            return True
        else:
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        order_ingredients["bread"] -= sandwich_size["bread"]
        order_ingredients["ham"] -= sandwich_size["ham"]
        order_ingredients["cheese"] -= sandwich_size["cheese"]
        return print(f"sandwich is ready. Bon appetit!")