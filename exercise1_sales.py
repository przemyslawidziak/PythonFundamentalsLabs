# Step 1- Create and run a Python File
print("****** Python Foundation Lab Started ******") # print function

# Step 2 - Create variables and data types
product = "Laptop" # string variable
quantity = 3 # integer variable
unit_price = 1200.4 # float variable
in_stock = True # boolean variable

print("****** Variables Created ******") # print function
print("Product:", product) # print string variable
print("Quantity:", quantity) # print integer variable
print("Unit Price:", unit_price) # print float variable
print("In Stock:", in_stock) # print boolean variable

print("****** Data Types of Variables ******") # print function
print(type(product)) # print data type of string variable
print(type(quantity)) # print data type of integer variable
print(type(unit_price)) # print data type of float variable
print(type(in_stock)) # print data type of boolean variable

#Step 3 - Perform a sales calculation
total_sales = quantity * unit_price # calculate total sales
print("****** Sales Calculation ******") # print function
print("Product:", product) # print product name
print("Quantity:", quantity) # print quantity
print("Unit Price:", unit_price) # print unit price
print("Total Sales:", total_sales) # print total sales

#Step 4 - Apply conditional statements
if total_sales >= 2000:
    print("Sales target achieved!") # print if sales target is achieved
else:
    print("Sales target not achieved! Keep trying!") # print if sales target is not achieved

    # Step 5 - Process Multiple Sales using loop
sales = [1200, 850, 2400, 1750, 3200] # list of sales amounts
print("****** Processing Multiple Sales ******")
for sale in sales:
    if sale >= 2000:
        print(f"Sale amount {sale} - Target achieved!")
    else:
        print(f"Sale amount {sale} - Target not achieved. Keep trying!")