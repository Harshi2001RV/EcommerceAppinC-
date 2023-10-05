class Product:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.availability >= quantity:
            self.cart.append((product, quantity))
            product.availability -= quantity
            print(f"{quantity} {product.name}(s) added to the cart.")
        else:
            print(f"Sorry, {product.name} is not available in the required quantity.")

    def update_quantity(self, product, new_quantity):
        for item in self.cart:
            if item[0] == product:
                old_quantity = item[1]
                if product.availability + old_quantity >= new_quantity:
                    item = (product, new_quantity)
                    product.availability += old_quantity - new_quantity
                    print(f"{product.name} quantity updated to {new_quantity}.")
                else:
                    print(f"Sorry, {product.name} does not have enough stock.")
                return
        print(f"{product.name} not found in the cart.")

    def remove_from_cart(self, product):
        for item in self.cart:
            if item[0] == product:
                self.cart.remove(item)
                product.availability += item[1]
                print(f"{product.name} removed from the cart.")
                return
        print(f"{product.name} not found in the cart.")

    def calculate_total(self):
        total = 0
        for item in self.cart:
            product, quantity = item
            total += product.price * quantity
        return total

    def view_cart(self):
        print("Shopping Cart:")
        for item in self.cart:
            product, quantity = item
            print(f"{product.name} - Quantity: {quantity}")

def main():
    # Creating some sample products
    product1 = Product("Laptop", 800, 5)
    product2 = Product("Phone", 300, 10)
    product3 = Product("Tablet", 200, 7)

    cart = ShoppingCart()

    # Display products
    print("Available Products:")
    print(f"1. {product1.name} - Price: ${product1.price} - Availability: {product1.availability}")
    print(f"2. {product2.name} - Price: ${product2.price} - Availability: {product2.availability}")
    print(f"3. {product3.name} - Price: ${product3.price} - Availability: {product3.availability}")

    while True:
        print("\nMenu:")
        print("1. Add to Cart")
        print("2. Update Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Calculate Total")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            product_id = int(input("Enter the product ID to add to cart: "))
            quantity = int(input("Enter the quantity: "))
            if product_id == 1:
                cart.add_to_cart(product1, quantity)
            elif product_id == 2:
                cart.add_to_cart(product2, quantity)
            elif product_id == 3:
                cart.add_to_cart(product3, quantity)
            else:
                print("Invalid product ID.")

        elif choice == 2:
            product_id = int(input("Enter the product ID to update in cart: "))
            quantity = int(input("Enter the new quantity: "))
            if product_id == 1:
                cart.update_quantity(product1, quantity)
            elif product_id == 2:
                cart.update_quantity(product2, quantity)
            elif product_id == 3:
                cart.update_quantity(product3, quantity)
            else:
                print("Invalid product ID.")

        elif choice == 3:
            product_id = int(input("Enter the product ID to remove from cart: "))
            if product_id == 1:
                cart.remove_from_cart(product1)
            elif product_id == 2:
                cart.remove_from_cart(product2)
            elif product_id == 3:
                cart.remove_from_cart(product3)
            else:
                print("Invalid product ID.")

        elif choice == 4:
            cart.view_cart()

        elif choice == 5:
            total = cart.calculate_total()
            print(f"Total: ${total}")

        elif choice == 6:
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
