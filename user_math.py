"""
Shanti Kandel
Data Analytics Module 2 Project 2
Jan 22, 2023

This project aims to write functions through Math module to perform common mathmatical calculations.

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    It could result ValueError if the input value are not numbers or negetive or is 0.

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)

def defect_product(*args):
    """
    returns counts of defected product produced in an hour
    """
    defect_count = 0
    for number in args:
        if isinstance(number, int) and number >= 0:
            defect_count += number
        else:
            raise ValueError("All inputs must be non-negative integers.")
    return defect_count

#---------------------------------------------------------------

def sales_of_product(medium, large, small, operating_expenses):
    """
    Returns total number of products sold based on their size
    """
    try:
        total_sales = medium + large + small
        revenue = operating_expenses - total_sales
        return revenue
    except Exception as e:
        print(f'An error occurred: {e}')


    #-------------------------------------------------------------

def revenue_after_discount(unit_price, units_sold, discount_percentage):
    """
    Calculates the revenue after discount for a product
    """
    total_price = unit_price * units_sold
    discount_amount = (discount_percentage/100) * total_price
    revenue_after_discount = total_price - discount_amount
    return revenue_after_discount


#------------------------------------------------------------------------




# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print(f"get_area_of_lot(6, 2) = {get_area_of_lot(6, 2)}")
    print()
    print(f"number of defect product produced per hour ={defect_product(4, 8, 12)}")
    print()
    print(f"sales of products based on product size ={sales_of_product(12, 30, 32,200)}")
    print()
    print(f"revenue after deducting discount= {revenue_after_discount(22, 24, 26)}")
    print()