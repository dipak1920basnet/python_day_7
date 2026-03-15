# Partial Guidance Exercise

# Goal: represent a product inventory.
def main():
    product = {
        "name":"Laptop",
        "price":1200,
        "stock":10,
        "category":"Electronics"
    }


    product_details(product)

    if not low_stock(product):
        update_stock_quantity(product, 3)
    print()
    print()
    product_details(product)
    


"""
1️⃣ print all product details
2️⃣ decrease stock after a sale
"""
# print all product details 
def product_details(product):
    """
    print all product details 
    """
    for key in product:
        print(key, ":", product[key])

def update_stock_quantity(product, sold_stock):
    if product["stock"] < sold_stock:
        print("Not enough stock")
        return 
    product["stock"] -= sold_stock

def low_stock(product):
    if product["stock"] < 5:
        return True
    return False

if __name__ == "__main__":
    main()