from helpers.sql.setup_database import Base, engine, session
from models import Category, Store, Closet, ClosetProduct


# Define your ORM models here
Base.metadata.create_all(engine)


def main():
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
        "Edeka",
        "REWE",
        "Aldi Süd",
        "Aldi Nord",
        "Lidl",
        "Kaufland",
        "Penny Markt",
        "Netto Marken-Discount",
        "Norma",
        "Real",
        "Metro Cash & Carry",
        "Globus",
        "famila",
        "Combi",
        "Marktkauf",
        "Alnatura",
        "Bio Company",
        "denk’s Biomarkt",
        "Lekkerland",
        "Selgros",
        "SPAR Express",
        "Nah & frisch",
        "Tegut",
    ]
    closet_types = [
        "Pantry",
        "Refrigerator",
        "Freezer",
        "Cupboard",
        "Kitchen Shelf",
        "Basement Storage",
        "Garage Storage",
        "Garage Storage",
        "Wine Cellar"
    ]

    for elements in categories:
        session.add(Category(category_name=elements))
    session.commit()
    for elements in german_stores:
        session.add(Store(store_name=elements))
    session.commit()


if __name__ == "__main__":
    main()
