class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {"item":item, "price":price, "quantity":quantity}
        self.cart.append(product)

    def remove_item(self, item):
        for i in self.cart:
            if i["item"] == item:
                self.cart.remove(i)
                break
        else:
            print("Item not found in cart")
                

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item["price"] * item["quantity"]
        print(f"total price: {total}")
        if amount < total:
            print(f"Please prodive {total-amount} more")
        else:
            extra = amount - total
            print(f"Here is your items and extra money: {extra}")


vuban = Shopping("Vuban")
vuban.add_to_cart("alu", 50, 6)
vuban.add_to_cart("dim", 12, 24)
vuban.add_to_cart("rice", 50, 5)

print(vuban.cart)
vuban.remove_item("alu")
print(vuban.cart)
vuban.checkout(600)

# print(vuban.cart[0])