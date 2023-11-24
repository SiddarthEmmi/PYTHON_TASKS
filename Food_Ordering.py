import sys

class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

class PizzaHut:
    def __init__(self):
        self.menu = {
            1: MenuItem(1, 'Veg Pizza', 150),
            2: MenuItem(2, 'Special Veg Pizza', 200),
            3: MenuItem(3, 'Mini Pizza', 100),
            4: MenuItem(4, 'Veg Burger', 100),
            5: MenuItem(5, 'Special Veg Burger', 130),
            6: MenuItem(6, 'Cheese Burger', 150),
            7: MenuItem(7, 'Veg Noodles', 100),
            8: MenuItem(8, 'Special Veg Noodles', 150),
            9: MenuItem(9, 'Cheese Noodles', 170),
        }
        self.order_items = []

    def display_menu(self):
        print("{:<10}{:<19}{:<10}".format("SL_NO", "FOODS", "PRICE"))
        for item_id, menu_item in self.menu.items():
            print("{:<10}{:<19}{:<10}".format(item_id, menu_item.name, menu_item.price))

    def take_order(self):
        self.display_menu()
        while True:
            choice = input("Enter your choice (0 to finish order): ")
            if choice == '0':
                break
            try:
                item_id = int(choice)
                if item_id not in self.menu:
                    print("Invalid choice. Please select a valid item.")
                    continue
                quantity = int(input("Enter quantity: "))
                order_item = OrderItem(self.menu[item_id], quantity)
                self.order_items.append(order_item)
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_order(self):
        print("{:<22}{:<22}{:<10}".format("FOODS", "QUANTITY", "PRICE"))
        for order_item in self.order_items:
            print("{:<22}{:<22}{:<10}".format(order_item.menu_item.name, order_item.quantity,
                                               order_item.menu_item.price * order_item.quantity))
        total_amount = sum(order_item.menu_item.price * order_item.quantity for order_item in self.order_items)
        print("Total amount:                              ", total_amount)

    def process_payment(self):
        if not self.order_items:
            print("You need to place an order first.")
            return

        self.display_order()

        pay = input("Want to pay? If YES click 'Y' else 'N': ")
        if pay.upper() == "Y":
            address = input("Enter Address: ")
            upi_number = input("Enter UPI Number: ")
            if address.isalpha() and upi_number.isdigit():
                print('THANK YOU!!..UR FOOD WILL BE DELIVERED SOON..')
                sys.exit(0)
            else:
                print("UR ADDRESS/UPI NUMBER WAS WRONG...PLS ENTER CORRECTLY")
                
        elif pay.upper() == "N":
            return
        else:
            print("Invalid choice")

if __name__ == "__main__":
    pizza_hut = PizzaHut()

    while True:
        print("1. ORDER")
        print("2. PAYMENT")
        print("3. EXIT")

        choice = input("Enter your choice: ")

        if choice == "1":
            pizza_hut.take_order()
        elif choice == "2":
            pizza_hut.process_payment()
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid choice.")
