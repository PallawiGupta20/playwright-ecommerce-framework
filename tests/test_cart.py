from pages.cart_page import CartPage

def test_add_single_product_to_cart(inventory_page):
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == "1"


def test_add_multiple_products_to_cart(inventory_page):
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.add_product_to_cart("sauce-labs-bike-light")
    assert inventory_page.get_cart_count() == "2"


def test_cart_shows_added_items(inventory_page):
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == "1"
    
    inventory_page.go_to_cart()
    
    # 1. Initialize CartPage manually on the same browser tab session
    cart_page = CartPage(inventory_page.page)
    
    # 2. ENFORCE A WAITING CUSHION: Wait for the item list row element to appear in the DOM
    inventory_page.page.wait_for_selector(".cart_item", state="visible", timeout=5000)
    
    # 3. Assert the item count
    assert cart_page.get_item_count() == 1
