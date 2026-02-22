from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_checkout_happy_path(page, login):
    """Verify a user can successfully complete checkout for a single product."""
    login()  # authenticate user using reusable login fixture

    item_slug = "sauce-labs-backpack"  # stable product identifier used by SauceDemo

    inventory = InventoryPage(page)  # inventory page object creation
    inventory.assert_loaded()  # confirm inventory page is displayed
    inventory.add_item_to_cart(item_slug)  # add selected product to cart
    inventory.open_cart()  # navigate to cart page

    cart = CartPage(page)  # cart page object creation
    cart.assert_loaded()  # confirm cart page opened
    cart.start_checkout()  # begin checkout process

    step_one = CheckoutStepOnePage(page)  # checkout step one page object creation
    step_one.assert_loaded()  # verify step one page is displayed
    step_one.fill_customer_info("John", "Doe", "12345")  # provide customer details
    step_one.continue_to_overview()  # proceed to order overview

    step_two = CheckoutStepTwoPage(page)  # checkout step two page object creation
    step_two.assert_loaded()  # confirm overview page opened
    step_two.finish()  # finalize purchase

    complete = CheckoutCompletePage(page)  # checkout complete page object creation
    complete.assert_loaded()  # verify confirmation page opened
    complete.assert_success_message()  # confirm successful order message