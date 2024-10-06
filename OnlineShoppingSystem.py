class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        #product details
        self.product_name = product_name  
        self.price = price  
        self.quantity_in_stock = quantity_in_stock  

    def display_product_info(self):
        #the product information
        print(f"Product: {self.product_name}, Price: ${self.price:.2f}, Quantity: {self.quantity_in_stock}")


class ShoppingCart:
    # Total number of shopping carts
    total_carts = 0  

    def __init__(self):
        # Creation of a new shopping cart
        self.items = []  
        ShoppingCart.total_carts += 1  

    def add_to_cart(self, product, quantity):
        # Add a product to the cart
        if quantity > product.quantity_in_stock:
            print(f"Cannot add {quantity}. Only {product.quantity_in_stock} in stock.")
        else:
            # Add product and quantity
            self.items.append((product, quantity))  
            # Reduce stock
            product.quantity_in_stock -= quantity  
            print(f"Added {quantity} of {product.product_name}.")

    def remove_from_cart(self, product):
        # Removal of a product from the cart
        for item in self.items:
            if item[0] == product:
                # Remove item
                self.items.remove(item) 
                # Restore stock
                product.quantity_in_stock += item[1]  
                print(f"Removed {product.product_name}.")
                return
        print(f"{product.product_name} not found.")

    def display_cart(self):
        # Show all items in the cart
        if not self.items:
            print("Cart is empty.")
            return
        
        print("Shopping Cart Items:")
        for product, quantity in self.items:
            print(f"- {product.product_name}: {quantity} units")

    def calculate_total(self):
        # Total price
        total = sum(product.price * quantity for product, quantity in self.items)
        return total


# Create Product objects
ProductA = Product("food flask", 31000, 100)
ProductB = Product("sponge", 3000, 50)
ProductC = Product("movit shower gel", 55000, 500)

# Create ShoppingCart instances
Cart01 = ShoppingCart()
Cart02 = ShoppingCart()

# Add items to Cart01
Cart01.add_to_cart(ProductA, 2)  
Cart01.add_to_cart(ProductB, 5)  

# Add items to Cart02
Cart02.add_to_cart(ProductB, 1)  
Cart02.add_to_cart(ProductC, 10)  

# Display of cart contents
Cart01.display_cart() 
Cart02.display_cart()  

# Calculate total for each cart
total_Cart01 = Cart01.calculate_total()
total_Cart02 = Cart02.calculate_total()

print(f"Total for Cart 01: UGX{total_Cart01:.2f}")  
print(f"Total for Cart 02: UGX{total_Cart02:.2f}")  

# Remove an item from Cart01
Cart01.remove_from_cart(ProductB)  

# Display Cart01 after removal
Cart01.display_cart()  
