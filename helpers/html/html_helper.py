import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
TEMPLATE_PATH = os.path.join(BASE_DIR, "static", "index_template.html")
TARGET_PATH = os.path.join(BASE_DIR, "static", "index.html")
TITLE_KEYWORD = "__TEMPLATE_TITLE__"
PRODUCT_GRID_KEYWORD = "__TEMPLATE_PRODUCT_GRID__"
WEB_PAGE_TITLE = "Welcome to Robert's Storage App"
ENCODING = "utf-8"


def get_html_template(path):
    """Read and return the HTML template content from a file."""
    try:
        with open(path, "r", encoding=ENCODING) as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
    except OSError as error:
        print(f"File error: {error}")
    return None


def format_data_for_html(products):
    output = ""
    if isinstance(products, dict):
        for name, value in products.items():
            product_name = name
            product_image = value['image']
            product_quantity = value['quantity']
            output += "\n"
            output += "\t\t<li>\n"
            output += "\t\t\t<div class=\"product\">\n"
            output += f"\t\t\t\t<img class=\"product-image\" src=\"{product_image}\" title=\"\"/>\n"
            output += f"\t\t\t\t<div class=\"product-name\">Product name: <br><b>{product_name}</b></div>\n"
            output += f"\t\t\t\t<div class=\"product-quantity\">Quantity: <b>{product_quantity}</b></div>\n"
            output += "\t\t\t</div>\n"
            output += "\t\t</li>\n"
    else:
        print("In order to format the html file, a list of dictionaries is expected")
    return output


def generate_website(products):
    """Generate the product website by injecting data into the HTML template."""
    template = get_html_template(TEMPLATE_PATH)
    if not template:
        print("The website was not generated, problem with the html template")
    else:
        formated_grid = format_data_for_html(products)
        index = template.replace(TITLE_KEYWORD, WEB_PAGE_TITLE)
        index = index.replace(PRODUCT_GRID_KEYWORD, formated_grid)
        try:
            with open(TARGET_PATH, "w", encoding=ENCODING) as file:
                file.write(index)
                print("Website was generated successfully.")
        except FileExistsError as error:
            print(f"File already exists: {TARGET_PATH}", error)
        except OSError as error:
            print(f"File error: {error}")
