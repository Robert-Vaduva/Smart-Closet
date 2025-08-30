import json
import random
import sys
from datetime import datetime, timedelta
import requests
from helpers.html.html_helper import generate_website
from helpers.api.api_helper import get_product_info
from helpers.sql.sqlalchemy_helper import init_db, add_instance, get_all, get_session, get_quantity_by_name, get_unique, delete_instance
from models import Closet
from models import ClosetProduct


CONNECT_TIMEOUT = 5  # seconds
READ_TIMEOUT = 10  # seconds
TIMEDELTA_DAYS_MAX = 60
PURCHASE_DATE = datetime.now()
EXPIRATION_DATE = PURCHASE_DATE + timedelta(random.randint(1, TIMEDELTA_DAYS_MAX))
closet_locations = [
    ["Pantry", "Dry goods like pasta, rice, canned foods"],
    ["Refrigerator", "Dairy, fruits, vegetables, drinks"],
    ["Freezer", "Frozen meals, meat, ice cream"],
    ["Cupboard", "Snacks, cereals, baking ingredients"],
    ["Kitchen Shelf", "Snacks, cereals, baking ingredients"],
    ["Basement", "Bulk items, extra canned goods"],
    ["Garage", "Bulk items, extra canned goods"],
    ["Wine Cellar", "Wine, specialty beverages"]
]
shopping_list_lidl = [
    {"barcode": 40897677, "quantity": 1, "purchase_date": PURCHASE_DATE, "expiration_date": EXPIRATION_DATE, "closet": 1},
    {"barcode": 20724696, "quantity": 2, "purchase_date": PURCHASE_DATE, "expiration_date": EXPIRATION_DATE, "closet": 1},
    {"barcode": 4056489141877, "quantity": 1, "purchase_date": PURCHASE_DATE, "expiration_date": EXPIRATION_DATE, "closet": 1},
    {"barcode": 4056489148739, "quantity": 1, "purchase_date": PURCHASE_DATE, "expiration_date": EXPIRATION_DATE, "closet": 1},
    {"barcode": 20202392, "quantity": 1, "purchase_date": PURCHASE_DATE, "expiration_date": EXPIRATION_DATE, "closet": 1},
    {"barcode": 4056489424918, "quantity": 2, "purchase_date": PURCHASE_DATE, "expiration_date": EXPIRATION_DATE, "closet": 1},
    {"barcode": 4056489471264, "quantity": 2, "purchase_date": PURCHASE_DATE, "expiration_date": EXPIRATION_DATE, "closet": 1},
    {"barcode": 20153229, "quantity": 2, "purchase_date": PURCHASE_DATE, "expiration_date": EXPIRATION_DATE, "closet": 1},
    {"barcode": 20276515, "quantity": 1, "purchase_date": PURCHASE_DATE, "expiration_date": EXPIRATION_DATE, "closet": 1},
    {"barcode": 4056489273264, "quantity": 1, "purchase_date": PURCHASE_DATE, "expiration_date": EXPIRATION_DATE, "closet": 1},
    {"barcode": 20198107, "quantity": 1, "purchase_date": PURCHASE_DATE, "expiration_date": EXPIRATION_DATE, "closet": 1},
    {"barcode": 4335896750712, "quantity": 1, "purchase_date": PURCHASE_DATE, "expiration_date": EXPIRATION_DATE, "closet": 1},
]


def exit_fnc():
    """Exit the application with a goodbye message."""
    print("Bye!")
    sys.exit()


def list_products():
    print("Here is a list of the current products")
    products = get_all(ClosetProduct)
    for product in products:
        print(product.closet_product_id, product.name)
    return products


def add_product():
    print("Add product")
    barcode = int(input("Enter barcode: "))
    quantity = int(input("Enter quantity: "))
    print("Here are the possible storage locations: ")
    for index, location in enumerate(closet_locations):
        print(f"{index}. {location[0]}")
    closet = int(input("Select storage: "))
    add_instance(format_product(barcode, quantity, PURCHASE_DATE, EXPIRATION_DATE, closet))
    generate_web_site()


def update_product():
    print("Update product")


def delete_product():
    print("Delete product")
    products = list_products()
    index = int(input("Enter the number of the product to be removed: "))
    for product in products:
        if product.closet_product_id == index:
            delete_instance(product)
    list_products()
    generate_web_site()


def initiate_database():
    print("Initiate database")
    # Initialize DB (create tables if not existing)
    init_db()
    for element in closet_locations:
        add_instance(Closet(closet_location=element[0], comments=element[1]))
    for element in shopping_list_lidl:
        add_instance(format_product(element["barcode"],
                                    element["quantity"],
                                    element["purchase_date"],
                                    element["expiration_date"],
                                    element["closet"]))
    print("The database has been successfully generated")


def generate_web_site():
    print("Generate website")
    products = get_all(ClosetProduct)
    list_of_products = {}
    for product in products:
        quantity = get_quantity_by_name(ClosetProduct, product.name)
        list_of_products[product.name] = {"image": product.img_url,
                                          "quantity": quantity}

    generate_website(list_of_products)


def format_product(barcode, quantity, purchase_date, expiration_date, _closet):
    data = get_product_info(barcode)
    products = data.get("product", {})

    # pre-processing of the categories data
    if len(products.get("categories_hierarchy")) > 7:
        category = products.get("categories_hierarchy")[7]
    else:
        category = products.get("categories_hierarchy")[0]

    # pre-processing of the nutritional data
    nutriments = products.get("nutriments")
    keys_to_include = ['energy-kcal_100g', 'fat', 'saturated-fat', 'carbohydrates', 'sugars',
                       'fiber', 'proteins', 'salt', 'fruits-vegetables-nuts-estimate-from-ingredients_100g']
    smaller_dict = {}
    for key in keys_to_include:
        if key in nutriments.keys():
            smaller_dict[key] = nutriments[key]

    product = ClosetProduct(
        barcode=barcode,
        name=products.get("product_name"),
        category=category,
        img_url=products.get("image_front_small_url"),
        nutrition_info=json.dumps(smaller_dict),
        product_price=0,
        product_qty=quantity,
        purchase_date=purchase_date,
        expiration_date=expiration_date,
        product_active=True,
        store=products.get("stores"),
        closet_id=random.randint(1, len(closet_locations))
    )
    return product


FUNCTIONS = {0: exit_fnc, 1: list_products, 2: add_product, 3: update_product,
             4: delete_product, 5: initiate_database, 6: generate_web_site}


def main():
    """Main function that runs the CLI menu and handles user input."""
    print("********** My Storage Database **********")
    while True:
        try:
            print("\nMenu:")
            print("0. Exit")
            print("1. List products")
            print("2. Add product")
            print("3. Update product")
            print("4. Delete product")
            print("5. Initiate database")
            print("6. Generate website")
            user_input = int(input(f"\nEnter choice (0-{len(FUNCTIONS) - 1}): "))
            if 0 <= user_input < len(FUNCTIONS):
                FUNCTIONS[user_input]()
            else:
                print("Invalid choice")
        except (TypeError, ValueError, KeyError) as error:
            print("Main function error:", error)


if __name__ == "__main__":
    main()
