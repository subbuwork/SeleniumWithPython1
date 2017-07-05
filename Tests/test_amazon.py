from selenium import webdriver
import pytest
from Utils import Browser
from Resources import Amazon


@pytest.fixture(scope="module")
def setup():
    browser = Browser.Browser().open_browser("gc")
    yield browser
    browser.quit()


def test_landing_page(setup):
    Amazon.landing_page(setup,"https://www.amazon.com")


def test_search_product(setup):
    Amazon.landing_page(setup,"https://www.amazon.com")
    Amazon.search_product(setup, "Ferrari 458")
    assert "Ferrari 458" in setup.page_source


def test_select_product(setup):
    Amazon.landing_page(setup, "https://www.amazon.com")
    Amazon.search_product(setup, "Ferrari 458")
    assert "Ferrari 458" in setup.page_source
    Amazon.select_product(setup)
    assert "Back to search results for 'Ferrari 458'" in setup.page_source


def test_verify_product_features(setup):
    Amazon.landing_page(setup, "https://www.amazon.com")
    Amazon.search_product(setup, "Ferrari 458")
    assert "Ferrari 458" in setup.page_source
    Amazon.select_product(setup)
    assert "Product information" in setup.page_source
    Amazon.view_product_images(setup)
    Amazon.check_product_rating_reviews_qa(setup)


def test_add_product_to_cart(setup):
    Amazon.landing_page(setup, "https://www.amazon.com")
    Amazon.search_product(setup, "Ferrari 458")
    assert "Ferrari 458" in setup.page_source
    Amazon.select_product(setup)
    assert "Product information" in setup.page_source
    Amazon.view_product_images(setup)
    setup.implicitly_wait(3)
    Amazon.check_product_rating_reviews_qa(setup)
    setup.implicitly_wait(3)
    Amazon.select_product_quantity(setup, "2")
    Amazon.add_product_to_cart(setup)
    Amazon.verify_cart(setup)



