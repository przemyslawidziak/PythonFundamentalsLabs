#Step 1 - Create a function
def calculate_sales(quantity, unit_price):
    return quantity * unit_price

result = calculate_sales(3, 1200.4) # call the function with arguments
print("****** Sales Calculation using Function ******") # print function
print("Total Sales:", result) # print total sales calculated by the function

#Step 2 - Reuse the function with different values
print("****** Reusing the Function with Different Values ******") # print function
print("Total Sales for 5 units at $1500.5 each:", calculate_sales(5, 1500.5)) # call the function with different arguments  
print("Total Sales for 2 units at $800.75 each:", calculate_sales(2, 800.75)) # call the function with different arguments
print("Total Sales for 10 units at $250.99 each:", calculate_sales(10, 250.99)) # call the function with different arguments

#Step 3 - Check and convert data types
print("")
print("****** Data Type Check and Conversion ******") # print function
quantity = "5.51" # string variable
print("Original Quantity (string):", quantity) # print original string variable
quantity_int = int(quantity) # convert string to integer
print("Converted Quantity (integer):", quantity_int) # print converted integer variable
print("Total Sales for converted quantity at $1500.5 each:", calculate_sales(quantity_int, 500)) # call the function with converted integer variable