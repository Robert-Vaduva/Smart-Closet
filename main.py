import json
import random
import sys
from datetime import datetime, timedelta
import requests
from helpers.html.html_helper import generate_website
from helpers.sql.sqlalchemy_helper import init_db, add_instance, get_all, get_session
from models import Closet
from models import ClosetProduct


CONNECT_TIMEOUT = 5  # seconds
READ_TIMEOUT = 10  # seconds
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
    {"barcode": 40897677, "quantity": 1, "purchase_date": 0, "expiration_date": 0, "closet": 1},
    {"barcode": 20724696, "quantity": 2, "purchase_date": 0, "expiration_date": 0, "closet": 1},
    {"barcode": 4056489141877, "quantity": 1, "purchase_date": 0, "expiration_date": 0, "closet": 1},
    {"barcode": 4056489148739, "quantity": 1, "purchase_date": 0, "expiration_date": 0, "closet": 1},
    {"barcode": 20202392, "quantity": 1, "purchase_date": 0, "expiration_date": 0, "closet": 1},
    {"barcode": 4056489424918, "quantity": 2, "purchase_date": 0, "expiration_date": 0, "closet": 1},
    {"barcode": 4056489471264, "quantity": 2, "purchase_date": 0, "expiration_date": 0, "closet": 1},
    {"barcode": 20153229, "quantity": 2, "purchase_date": 0, "expiration_date": 0, "closet": 1},
    {"barcode": 20276515, "quantity": 1, "purchase_date": 0, "expiration_date": 0, "closet": 1},
    {"barcode": 4056489273264, "quantity": 1, "purchase_date": 0, "expiration_date": 0, "closet": 1},
    {"barcode": 20198107, "quantity": 1, "purchase_date": 0, "expiration_date": 0, "closet": 1},
    {"barcode": 4335896750712, "quantity": 1, "purchase_date": 0, "expiration_date": 0, "closet": 1},
]


def exit_fnc(products):
    """Exit the application with a goodbye message."""
    print("Bye!")
    sys.exit()


def list_products(products):
    print("List products")


def add_product(products):
    print("Add product")


def update_product(products):
    print("Update product")


def delete_product(products):
    print("Delete product")


def initiate_database(products):
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


def generate_web_site(products):
    print("Generate website")
    products = get_all(ClosetProduct)
    list_of_products = {}
    for product in products:
        quantity = filter_product_quantity(product.name)
        list_of_products[product.name] = {"image": product.img_url,
                                          "quantity": quantity}

    generate_website(list_of_products)


def format_product(barcode, quantity, _purchase_date, _expiration_date, _closet):
    purchase_date = datetime.now()
    expiration_date = purchase_date + timedelta(random.randint(1, 60))

    response = requests.get(f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json",
                            timeout=(CONNECT_TIMEOUT, READ_TIMEOUT))
    data = response.json()
    products = data.get("product", {})

    # pre-processing of the categories data
    if len(products.get("categories_hierarchy")) >= 7:
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


def filter_product_quantity(product_name):
    # Query for a specific product (e.g., by name or barcode)
    session = get_session()
    product = session.query(ClosetProduct.product_qty).filter(ClosetProduct.name == product_name).all()

    total = 0
    for elem in product:
        total += elem[0]
    if product:
        return total
    else:
        return None


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
                FUNCTIONS[user_input](True)  # rova add here list of products
            else:
                print("Invalid choice")
        except (TypeError, ValueError, KeyError) as error:
            print("Main function error:", error)


if __name__ == "__main__":
    main()
