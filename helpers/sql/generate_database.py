from helpers.sql.setup_database import Base, engine, session
from models import Category, Store, Closet, ClosetProduct
from datetime import datetime, timedelta


# Define your ORM models here
Base.metadata.create_all(engine)


NOW = datetime.now()
produce_list = [
  {
    "closet_product_id": 1,
    "product_id": 101,
    "product_name": "Organic Bananas",
    "category_id": 1,
    "product_img_url": "https://example.com/images/banana.jpg",
    "product_nutrition_info": "Calories: 52 per 100g, Carbs: 14g, Sugar: 10g",
    "product_price": 3.99,
    "product_qty": 6,
    "purchase_date": f"{str(NOW)}",
    "expiration_date": f"{str(NOW + timedelta(days=5))}",
    "product_active": 1,
    "store_id": 1,
    "closet_id": 2
  },
  {
    "closet_product_id": 2,
    "product_id": 102,
    "product_name": "Whole Wheat Bread",
    "category_id": 2,
    "product_img_url": "https://example.com/images/bread.jpg",
    "product_nutrition_info": "Calories: 247 per 100g, Protein: 13g, Fiber: 7g",
    "product_price": 2.50,
    "product_qty": 2,
    "purchase_date": f"{str(NOW)}",
    "expiration_date": f"{str(NOW + timedelta(days=3))}",
    "product_active": 1,
    "store_id": 1,
    "closet_id": 1
  },
  {
    "closet_product_id": 3,
    "product_id": 103,
    "product_name": "Frozen Pizza",
    "category_id": 3,
    "product_img_url": "https://example.com/images/pizza.jpg",
    "product_nutrition_info": "Calories: 280 per slice, Fat: 11g, Protein: 12g",
    "product_price": 6.75,
    "product_qty": 1,
    "purchase_date": f"{str(NOW)}",
    "expiration_date": f"{str(NOW + timedelta(weeks=12))}",
    "product_active": 1,
    "store_id": 1,
    "closet_id": 3
  },
  {
    "closet_product_id": 4,
    "product_id": 104,
    "product_name": "Greek Yogurt",
    "category_id": 4,
    "product_img_url": "https://example.com/images/yogurt.jpg",
    "product_nutrition_info": "Calories: 59 per 100g, Protein: 10g, Carbs: 3.6g",
    "product_price": 1.20,
    "product_qty": 6,
    "purchase_date": f"{str(NOW)}",
    "expiration_date": f"{str(NOW + timedelta(days=3))}",
    "product_active": 1,
    "store_id": 1,
    "closet_id": 2
  },
  {
    "closet_product_id": 5,
    "product_id": 105,
    "product_name": "Almond Milk",
    "category_id": 5,
    "product_img_url": "https://example.com/images/almond_milk.jpg",
    "product_nutrition_info": "Calories: 30 per cup, Fat: 2.5g, Carbs: 1g",
    "product_price": 3.49,
    "product_qty": 1,
    "purchase_date": f"{str(NOW)}",
    "expiration_date": f"{str(NOW + timedelta(days=3))}",
    "product_active": 1,
    "store_id": 1,
    "closet_id": 2
  },
  {
    "closet_product_id": 6,
    "product_id": 106,
    "product_name": "Orange Juice, 100% Pure",
    "category_id": 5,
    "product_img_url": "https://example.com/images/orange_juice.jpg",
    "product_nutrition_info": "Calories: 45 per 100ml, Sugar: 9g",
    "product_price": 2.99,
    "product_qty": 1,
    "purchase_date": f"{str(NOW)}",
    "expiration_date": f"{str(NOW + timedelta(days=3))}",
    "product_active": 1,
    "store_id": 1,
    "closet_id": 2
  },
  {
    "closet_product_id": 7,
    "product_id": 107,
    "product_name": "Free-Range Eggs, 12 Pack",
    "category_id": 4,
    "product_img_url": "https://example.com/images/eggs.jpg",
    "product_nutrition_info": "Calories: 155 per 100g, Protein: 13g, Fat: 11g",
    "product_price": 3.19,
    "product_qty": 12,
    "purchase_date": f"{str(NOW)}",
    "expiration_date": f"{str(NOW + timedelta(days=14))}",
    "product_active": 1,
    "store_id": 1,
    "closet_id": 2
  },
  {
    "closet_product_id": 8,
    "product_id": 108,
    "product_name": "Cheddar Cheese, Sliced",
    "category_id": 4,
    "product_img_url": "https://example.com/images/cheddar.jpg",
    "product_nutrition_info": "Calories: 402 per 100g, Fat: 33g, Protein: 25g",
    "product_price": 2.49,
    "product_qty": 1,
    "purchase_date": f"{str(NOW)}",
    "expiration_date": f"{str(NOW + timedelta(days=14))}",
    "product_active": 1,
    "store_id": 1,
    "closet_id": 2
  },
  {
    "closet_product_id": 9,
    "product_id": 109,
    "product_name": "Tomatoes, Cherry",
    "category_id": 1,
    "product_img_url": "https://example.com/images/cherry_tomatoes.jpg",
    "product_nutrition_info": "Calories: 18 per 100g, Carbs: 3.9g, Sugar: 2.6g",
    "product_price": 2.29,
    "product_qty": 500,
    "purchase_date": f"{str(NOW)}",
    "expiration_date": f"{str(NOW + timedelta(days=3))}",
    "product_active": 1,
    "store_id": 1,
    "closet_id": 1
  },
  {
    "closet_product_id": 10,
    "product_id": 110,
    "product_name": "Carrots, Organic",
    "category_id": 1,
    "product_img_url": "https://example.com/images/carrots.jpg",
    "product_nutrition_info": "Calories: 41 per 100g, Carbs: 10g, Fiber: 2.8g",
    "product_price": 1.99,
    "product_qty": 1,
    "purchase_date": f"{str(NOW)}",
    "expiration_date": f"{str(NOW + timedelta(days=7))}",
    "product_active": 1,
    "store_id": 1,
    "closet_id": 1
  }
]
categories = [
    "Dairy",
    "Meat & Poultry",
    "Fish & Seafood",
    "Fruits",
    "Vegetables",
    "Grains & Cereals",
    "Legumes (beans, lentils, peas)",
    "Nuts & Seeds",
    "Oils & Fats",
    "Beverages",
    "Snacks & Sweets",
    "Spices & Herbs",
    "Canned & Preserved",
    "Frozen Foods",
    "Condiments & Sauces",
    "Bakery & Bread",
    "Prepared Meals"
]
german_stores = [
    ["Edeka", "https://www.edeka.de/"],
    ["REWE", "https://www.rewe.de/"],
    ["Aldi Süd", "https://www.aldi-sued.de/"],
    ["Aldi Nord", "https://www.aldi-nord.de/"],
    ["Lidl", "https://www.lidl.de/"],
    ["Kaufland", "https://www.kaufland.de/"],
    ["Penny Markt", "https://www.penny.de/"],
    ["Netto Marken-Discount", "https://www.netto-online.de/"],
    ["Norma", "https://www.norma-online.de/"],
    ["Real", "https://www.real.de/"],
    ["Metro Cash & Carry", "https://www.metro.de/"],
    ["Globus", "https://www.globus.de/"],
    ["famila", "https://www.famila.de/"],
    ["Combi", "https://www.combi.de/"],
    ["Marktkauf", "https://www.marktkauf.de/"],
    ["Alnatura", "https://www.alnatura.de/"],
    ["Bio Company", "https://www.biocompany.de/"],
    ["denk’s Biomarkt", "https://www.denks.de/"],
    ["Lekkerland", "https://www.lekkerland.de/"],
    ["Selgros", "https://www.selgros.de/"],
    ["SPAR Express", "https://www.spar.de/"],
    ["Nah & frisch", "https://www.nah-und-frisch.at/"],
    ["Tegut", "https://www.tegut.com/"]
]

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

def main():
    """
    for element in categories:
        session.add(Category(category_name=element))
    for element in german_stores:
        session.add(Store(store_name=element[0], store_url=element[1]))
    for element in closet_locations:
        session.add(Closet(closet_location=element[0], comments=element[1]))
    """
    products = []
    for item in produce_list:
        product = ClosetProduct(
            product_id=item["product_id"],
            product_name=item["product_name"],
            category_id=item["category_id"],
            product_img_url=item["product_img_url"],
            product_nutrition_info=item["product_nutrition_info"],
            product_price=item["product_price"],
            product_qty=item["product_qty"],
            purchase_date=datetime.fromisoformat(item["purchase_date"]) if item["purchase_date"] else None,
            expiration_date=datetime.fromisoformat(item["expiration_date"]) if item["expiration_date"] else None,
            product_active=bool(item["product_active"]),
            store_id=item["store_id"],
            closet_id=item["closet_id"],
        )
        products.append(product)
    session.add_all(products)
    session.commit()


if __name__ == "__main__":
    main()
