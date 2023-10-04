#include <stdio.h>
#include <string.h>

// Define a product structure
typedef struct {
    char name[100];
    float price;
    int available;
} Product;

// Define a cart item structure
typedef struct {
    Product product;
    int quantity;
} CartItem;

// Function to display product details
void displayProduct(Product product) {
    printf("Name: %s\n", product.name);
    printf("Price: $%.2f\n", product.price);
    printf("Availability: %s\n", product.available ? "Available" : "Out of Stock");
    printf("\n");
}

// Function to display cart items
void displayCart(CartItem cart[], int itemCount) {
    printf("Cart Items:\n");
    float totalBill = 0.0;
    for (int i = 0; i < itemCount; i++) {
        printf("%d x %s\n", cart[i].quantity, cart[i].product.name);
        totalBill += cart[i].quantity * cart[i].product.price;
    }
    printf("Total Bill: $%.2f\n\n", totalBill);
}

int main() {
    // Sample products
    Product products[] = {
        {"Laptop", 1000.0, 1},
        {"Headphones", 50.0, 1},
        {"Mouse", 20.0, 0},
    };

    // Initialize the shopping cart
    CartItem cart[100];
    int itemCount = 0;

    int choice;
    do {
        printf("E-commerce App Menu:\n");
        printf("1. View Products\n");
        printf("2. Add to Cart\n");
        printf("3. View Cart\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Available Products:\n");
                for (int i = 0; i < sizeof(products) / sizeof(products[0]); i++) {
                    if (products[i].available) {
                        displayProduct(products[i]);
                    }
                }
                break;

            case 2:
                printf("Enter the product name to add to the cart: ");
                char productName[100];
                scanf("%s", productName);
                int quantity;
                printf("Enter the quantity: ");
                scanf("%d", &quantity);

                for (int i = 0; i < sizeof(products) / sizeof(products[0]); i++) {
                    if (strcmp(productName, products[i].name) == 0 && products[i].available) {
                        cart[itemCount].product = products[i];
                        cart[itemCount].quantity = quantity;
                        itemCount++;
                        printf("Added to cart: %s x %d\n", products[i].name, quantity);
                        break;
                    }
                }
                break;

            case 3:
                displayCart(cart, itemCount);
                break;

            case 4:
                printf("Thank you for shopping!\n");
                break;

            default:
                printf("Invalid choice. Please try again.\n");
                break;
        }
    } while (choice != 4);

    return 0;
}
