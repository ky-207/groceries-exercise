# groceries.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#
# PRODUCTS (PART 1)
#
# --------------
# THERE ARE 20 PRODUCTS:
# --------------
#  + All-Seasons Salt ($4.99)
#  + Chocolate Fudge Layer Cake ($18.50)
#  + Chocolate Sandwich Cookies ($3.50)
#  + Cut Russet Potatoes Steam N' Mash ($4.25)
#  + Dry Nose Oil ($21.99)
#  + Fresh Scent Dishwasher Cleaner ($4.99)
#  + Gluten Free Quinoa Three Cheese & Mushroom Blend ($3.99)
#  + Green Chile Anytime Sauce ($7.99)
#  + Light Strawberry Blueberry Yogurt ($6.50)
#  + Mint Chocolate Flavored Syrup ($4.50)
#  + Overnight Diapers Size 6 ($25.50)
#  + Peach Mango Juice ($1.99)
#  + Pizza For One Suprema Frozen Pizza ($12.50)
#  + Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
#  + Pure Coconut Water With Orange ($3.50)
#  + Rendered Duck Fat ($9.99)
#  + Robust Golden Unsweetened Oolong Tea ($2.49)
#  + Saline Nasal Mist ($16.00)
#  + Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
#  + Sparkling Orange Juice & Prickly Pear Beverage ($2.99)


print("--------------")
# print("THERE ARE ", len(products), " PRODUCTS:")
# print("THERE ARE " + str(len(products)) + " PRODUCTS:")
print(f"THERE ARE {len(products)} PRODUCTS:")
print("--------------")


def sort_by_name(product):
    return product["name"]

sorted_products = sorted(products, key=sort_by_name)



for product in sorted_products:
    price_usd = " (${0:.2f})".format(product["price"])
    print(" ... " + product["name"] + price_usd)


#
# DEPARTMENTS (PART 2)
#
# --------------
# THERE ARE 10 DEPARTMENTS:
# --------------
#  + Babies (1 product)
#  + Beverages (5 products)
#  + Dairy Eggs (1 product)
#  + Dry Goods Pasta (1 product)
#  + Frozen (4 products)
#  + Household (1 product)
#  + Meat Seafood (1 product)
#  + Pantry (2 products)
#  + Personal Care (2 products)
#  + Snacks (2 products)

departments = []
for product in products:
    # print(product["department"])
    #if product["department"] not in departments:
    #     departments.append(product["department"])
    departments.append(product["department"])

unique_departments = list(set(departments))

print("--------------")
print(f"THERE ARE {len(unique_departments)} DEPARTMENTS:")
print("--------------")

unique_departments.sort()

for d in unique_departments:
    matching_products = [product for product in products if product["department"] == d]
    matching_products_count = len(matching_products)
    if matching_products_count > 1:
        label = "products"
    else:  
        label = "product"
    print(" + " + d.title() + " (" + str(matching_products_count) + " " + label + ")")