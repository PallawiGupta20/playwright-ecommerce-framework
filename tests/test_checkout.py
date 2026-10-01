def test_full_purchase_flow(inventory_page, cart_page, checkout_page):
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()

    cart_page.proceed_to_checkout()

    checkout_page.fill_checkout_info("Pallawi", "Gupta", "121001")
    checkout_page.finish_order()

    assert checkout_page.get_confirmation_text() == "Thank you for your order!"
