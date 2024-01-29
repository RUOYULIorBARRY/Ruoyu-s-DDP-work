
# Functionality 1: create a Sales Tracking System which can
# ▪ Recording sales transactions, i.e., the number of product sales.
# ▪ Calculating total sales for each product.
# ▪ Identifying the best-selling product.

product_db = {}
# Create a function to add a new product


def add_product(product_id, name, price, initial_sales=0, initial_revenue=0.0):
    if product_id in product_db:
        print(f"Product ID {product_id} already exists.")
    else:
        product_db[product_id] = {
            "name": name,
            "price": price,
            "sales": initial_sales,
            "revenue": initial_revenue
        }

# Create a function to view the product database


def view_products():
    for product_id, details in product_db.items():
        print(
            f"ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Sales: {details['sales']}, Revenue: {details['revenue']}")


# This is a example to add products and create my database
add_product("001", "Eco-friendly Water Bottle", 12.99)
add_product("002", "Wireless Bluetooth Headphones", 59.99)
add_product("003", "Organic Cotton T-shirt", 24.99)
add_product("004", "Smartwatch Fitness Tracker", 45.99)
add_product("005", "Portable Charger 10000mAh", 29.99)

# view added products
for product_id, details in product_db.items():
    print(
        f"ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Sales: {details['sales']}, Revenue: {details['revenue']}")

# This is a function that can record the sales of a product
# In addition, Error Handling has been added so that if the user enters an incorrect product ID,
# he will be prompted to enter the correct product ID.


def record_sale(product_id, quantity_sold):
    try:
        if product_id not in product_db:
            print(
                f"Product ID {product_id} not found. Please enter the ritht product ID.")
            return
        quantity_sold = int(quantity_sold)
        product = product_db[product_id]
        product['sales'] += quantity_sold
        product['revenue'] += quantity_sold * product['price']
    except ValueError:
        print("Invalid quantity. Please enter a numeric value.")


# This is a function that can calculate the total sales for each product.

def calculate_total_sales():
    total_sales = {}
    for product_id, product in product_db.items():
        total_sales[product_id] = product['revenue']
    return total_sales

# This is a function that identifies the best-selling products.


def identify_best_selling_product():
    best_selling_product_id = max(
        product_db, key=lambda id: product_db[id]['sales'])
    return product_db[best_selling_product_id]


# This is an example of selling some products.
record_sale("001", 10)
record_sale("002", 5)
record_sale("003", 7)

# This allows the user to choose to view the sales of a specific product or to query the sales of an entire item,
# thus increasing the interactivity of the system.


def get_product_sales(product_id):
    if product_id in product_db:
        product = product_db[product_id]
        return f"{product['name']}: Sales - {product['sales']}, Revenue - {product['revenue']}"
    else:
        return "Product ID not found."


def interactive_sales_query():
    while True:
        user_input = input(
            "Enter product ID to view sales, type 'all' to view all products, or 'exit' to quit: ").strip()

        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'all':
            for pid in product_db:
                print(get_product_sales(pid))
        else:
            print(get_product_sales(user_input))


# Functionality2: create a Customer Management System which can
# ▪ Recording customer feedback or ratings for products.
# ▪ Displaying product average rating.

# This is a function to add a customer rating.
# In addition, Error Handling has been added so that if the user enters an incorrect product ID,
# he will be prompted to enter the correct product ID.

def record_customer_rating(product_id, rating):
    if product_id not in product_db:
        print("Product ID not found. Please enter the ritht product ID ")
        return

    try:
        rating = float(rating)
        if 1.0 <= rating <= 5.0:
            if 'ratings' not in product_db[product_id]:
                product_db[product_id]['ratings'] = []
            product_db[product_id]['ratings'].append(rating)
        else:
            print("Invalid rating. Please enter a rating between 1.0 and 5.0.")
    except ValueError:
        print("Invalid input. Rating must be a number.")

# This is a function to calculate and display the average rating of a product.


def display_product_average_rating(product_id):
    if product_id in product_db and 'ratings' in product_db[product_id]:
        ratings = product_db[product_id]['ratings']
        if ratings:
            average_rating = sum(ratings) / len(ratings)
            return f"Average Rating for {product_db[product_id]['name']}: {average_rating:.2f}"
        else:
            return "No ratings available for this product."
    else:
        return "Product ID not found."


def display_all_average_ratings():
    for product_id in product_db:
        print(display_product_average_rating(product_id))


# This is an example to record some product ratings.
record_customer_rating("001", 5)
record_customer_rating("001", 4)
record_customer_rating("002", 3)

# Shows the average rating for a specific product
print(display_product_average_rating("001"))  # product ID "001"
# product ID "003"，Assuming no ratings
print(display_product_average_rating("003"))


def sales_tracking_menu():
    while True:
        print("\n--- Sales Tracking ---")
        print("1. Record Sale")
        print("2. Calculate Total Sales")
        print("3. Identify Best Selling Product")
        print("4. Return to Main Menu")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity sold: "))
            record_sale(product_id, quantity)
        elif choice == '2':
            print(calculate_total_sales())
        elif choice == '3':
            best_selling = identify_best_selling_product()
            print(
                f"Best Selling Product: {best_selling['name']} - Sales: {best_selling['sales']}, Revenue: {best_selling['revenue']}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Users now have the option to view the average rating for a single product, as well as the average rating for all products.


def customer_management_menu():
    while True:
        print("\n--- Customer Feedback Management ---")
        print("1. Record Customer Rating")
        print("2. Display Product Average Rating")
        print("3. Display All Products Average Ratings")
        print("4. Return to Main Menu")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            rating = int(input("Enter rating (1-5): "))
            record_customer_rating(product_id, rating)
        elif choice == '2':
            product_id = input("Enter product ID to view average rating: ")
            print(display_product_average_rating(product_id))
        elif choice == '3':
            display_all_average_ratings()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# This is a function to implement the total sales input.

def report_total_sales_revenue():
    total_revenue = sum(product['revenue'] for product in product_db.values())
    print(f"Total Sales Revenue: ${total_revenue:.2f}")

# This is a function to define the best-selling product。


def identify_best_selling_product():
    best_selling_product_id = max(
        product_db, key=lambda id: product_db[id]['sales'])
    return product_db[best_selling_product_id]

# This is a function to create a Product Sales History.


def report_product_sales_history():
    for product_id, product in product_db.items():
        print(
            f"ID: {product_id}, Name: {product['name']}, Sales: {product['sales']}, Revenue: ${product['revenue']:.2f}")

#  Added a product sales reporting system to the system, creating a new feature set to generate insights about product sales, including total sales revenue, best-selling products, and product sales history.


def sales_report_menu():
    while True:
        print("\n--- Sales Report Menu ---")
        print("1. Total Sales Revenue")
        print("2. Best Selling Product")
        print("3. Product Sales History")
        print("4. Return to Main Menu")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            report_total_sales_revenue()
        elif choice == '2':
            best_selling = identify_best_selling_product()
            print(
                f"Best Selling Product: {best_selling['name']} - Sales: {best_selling['sales']}, Revenue: ${best_selling['revenue']:.2f}")
        elif choice == '3':
            report_product_sales_history()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# A general user menu interface is defined here, allowing users to access specific systems of their choice.


def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Sales Tracking")
        print("2. Customer Feedback Management")
        print("3. Sales Report")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            sales_tracking_menu()
        elif choice == '2':
            customer_management_menu()
        elif choice == '3':
            sales_report_menu()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


#
main_menu()
