from PO.Amazon import Cart, LandingPage, Product, Search, SelectProduct


def landing_page(setup, url):
    LandingPage.LandingPage(setup).open_home_page(url)


def search_product(setup,search_term):
    Search.SearchPage(setup).search_product(search_term)


def select_product(setup):
    SelectProduct.SelectProduct(setup).select_product()


def view_product_images(setup):
    Product.Product(setup).view_product_images()


def check_product_rating_reviews_qa(setup):
    Product.Product(setup).check_product_rating_reviews_qa()


def select_product_quantity(setup,quantity):
    Product.Product(setup).select_product_quantity(quantity)


def add_product_to_cart(setup):
    Product.Product(setup).add_product_to_cart()


def proceed_to_checkout(setup):
    Cart.Cart(setup).proceed_to_checkout()


def verify_cart(setup):
    Cart.Cart(setup).verify_cart()