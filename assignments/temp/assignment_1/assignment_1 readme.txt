Product Information System Using Different Data Types and Formatting Methods
Objective
Create a Python program that takes user input for product details and displays the information using different Python data types and string formatting methods:
- Comma Separation (sep=',')
- Percentage Formatting (% operator)
- f-strings (f"")
- .format() method

Task 1: Input Product Details
The program collects the following details:
- Product ID (int)
- Product Name (str)
- Price (float)
- Categories (list of strings, comma-separated)
- Stock Details (tuple – Available stock, Sold items)
- Discount Percentage (float)
- Product Features (set, comma-separated)
- Supplier Details (dict with name, contact number, and location)

Task 2: Display Product Details with Online Product Example
Python Code:

# Task 1: Take Product Details
product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
categories = input("Enter Categories (comma-separated): ").split(',')
available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
discount = float(input("Enter Discount Percentage: "))
features = set(input("Enter Product Features (comma-separated): ").split(','))
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")

stock_details = (available_stock, sold_stock)
supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

# Task 2: Display Output Using Different Formatting Methods

# 1. Comma Separation
print("\n1. Using Comma Separation (sep=',')")
print("Product ID, Name, Price:", product_id, product_name, price, sep=',')

# 2. Percentage Formatting
print("\n2. Using Percentage Formatting (% operator)")
print("Product Discount: %.2f%%" % discount)

# 3. f-strings
print("\n3. Using f-strings (f"")")
print(f"Product Name: {product_name}")
print(f"Price: ₹{price}")
print(f"Discount: {discount}%")
print(f"Stock Available: {stock_details[0]} units")

# 4. .format() method
print("\n4. Using .format() method")
print("Supplier Details: Name - {}, Contact - {}, Location - {}".format(
    supplier_details["name"], supplier_details["contact"], supplier_details["location"]
))

# 5. Online Product Example (Canon Pixma TS3370s Printer)
online_product = {
    "name": "Canon Pixma TS3370s Wireless All-in-One Printer",
    "price": 4159.0,
    "source": "Zepto/Online"
}

print("\n5. Online Product from Amazon:")
print(f"Name: {online_product['name']}")
print(f"Price: ₹{online_product['price']}")
print(f"Source: {online_product['source']}")


Sample Input:
Enter Product ID: 202  
Enter Product Name: Canon Pixma TS3370s Wireless Printer  
Enter Price: 4159.0  
Enter Categories (comma-separated): Electronics, Printer, Wireless  
Enter Available Stock: 30  
Enter Sold Stock: 10  
Enter Discount Percentage: 12.5  
Enter Product Features (comma-separated): Wireless, All-in-One, Color Print, Mobile Print  
Enter Supplier Name: Canon Distributors  
Enter Supplier Contact Number: 9876543210  
Enter Supplier Location: Mumbai
Expected Output:

1. Using Comma Separation (sep=',')
Product ID, Name, Price:202,Canon Pixma TS3370s Wireless Printer,4159.0

2. Using Percentage Formatting (% operator)
Product Discount: 12.50%

3. Using f-strings (f"")
Product Name: Canon Pixma TS3370s Wireless Printer
Price: ₹4159.0
Discount: 12.5%
Stock Available: 30 units

4. Using .format() method
Supplier Details: Name - Canon Distributors, Contact - 9876543210, Location - Mumbai

5. Online Product from Amazon:
Name: Canon Pixma TS3370s Wireless All-in-One Printer
Price: ₹4159.0
