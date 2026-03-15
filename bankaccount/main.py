from saving import Saving
from checking import Checking


#customer_name, current_balance, minimum_balance, account_number, routing_number


p2 = Saving("Andrew", 50000, 100, 1234, 4321)
p2.print_customer_information()
p2.withdrawl(3000)
p2.print_customer_information()
p2.deposit(2000)
p2.print_customer_information()
p2.intrest()

print("\n")

p3 = Checking("Sadik", 60000, 110, 2233, 3322)
p3.print_customer_information()
p3.withdrawl(4000)
p3.print_customer_information()
p3.deposit(2000)
p3.print_customer_information()
p3.transfer(2000, 4332)

print("\n")

p4 = Saving("John", 70000, 120, 9999, 8888)
p4.print_customer_information()
p4.withdrawl(3000)
p4.print_customer_information()
p4.deposit(2000)
p4.print_customer_information()
p4.intrest()

print("\n")

p5 = Checking("Marry", 80000, 130, 1111, 2222)
p5.print_customer_information()
p5.withdrawl(4000)
p5.print_customer_information()
p5.deposit(2000)
p5.print_customer_information()
p5.transfer(3000, 7647)