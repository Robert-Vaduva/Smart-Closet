from helpers.sql.setup_database import Base, engine, session
from models import Closet, ClosetProduct
from datetime import datetime, timedelta
from helpers.html.html_helper import generate_website
import requests
import random
import json
import os


# Define your ORM models here
Base.metadata.create_all(engine)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
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
]


def format_product(barcode, quantity, _purchase_date, _expiration_date, _closet):
    purchase_date = datetime.now()
    expiration_date = purchase_date + timedelta(random.randint(1, 60))

    response = requests.get(f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json")
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


def create_database():
    for element in closet_locations:
        session.add(Closet(closet_location=element[0], comments=element[1]))
    for element in shopping_list_lidl:
        session.add(format_product(element["barcode"],
                                   element["quantity"],
                                   element["purchase_date"],
                                   element["expiration_date"],
                                   element["closet"]))
    session.commit()
    print("The database has been successfully generated")


def filter_product_quantity(product_name):
    # Query for a specific product (e.g., by name or barcode)
    product = session.query(ClosetProduct.product_qty).filter(ClosetProduct.name == product_name).all()

    total = 0
    for elem in product:
        total += elem[0]
    if product:
        return total
    else:
        return None


def main():
    create_database()

    products = session.query(ClosetProduct).all()
    list_of_products = {}
    for product in products:
        quantity = filter_product_quantity(product.name)
        list_of_products[product.name] = {"image": product.img_url,
                                          "quantity": quantity}

    generate_website(list_of_products)
    session.close()


if __name__ == "__main__":
    main()
