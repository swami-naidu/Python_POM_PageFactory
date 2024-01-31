import time

from Base.conftext import *


def test_best_sellers_data(amazon_setup):
    Objects.object["home"].goto_amazon_home_page()
    Objects.object["home"].click_best_sellers_button()
    Objects.object["best_sellers"].print_departments()  # PRINT
    # Objects.object["best_sellers"].print_best_sellers_in_bags_wallets_luggage()
    # Objects.object["best_sellers"].print_best_sellers_in_video_games()
    # Objects.object["best_sellers"].print_best_sellers_in_music()
    # Objects.object["best_sellers"].print_best_sellers_in_amazon_renewed()
    # Objects.object["best_sellers"].print_best_sellers_in_office_products()
    # Objects.object["best_sellers"].print_best_sellers_in_industrial_and_scientific()
    time.sleep(3)


def test_new_releases_data():
    Objects.object["home"].goto_amazon_home_page()
    Objects.object["home"].click_new_releases_button()
    Objects.object["new_releases"].print_departments()  # PRINT
    Objects.object["new_releases"].click_department_amazon_renewed()
    Objects.object["new_releases_renewed"].print_renewed_items()  # PRINT
    Objects.object["new_releases_renewed"].click_any_department_button()
    Objects.object["new_releases"].click_department_baby_products()
    Objects.object["new_releases_baby_products"].print_baby_product_items()  # PRINT
    Objects.object["new_releases_baby_products"].click_any_department_button()
    time.sleep(3)


def test_movers_and_shakers_data():
    Objects.object["home"].goto_amazon_home_page()
    Objects.object["home"].click_movers_and_shakers_button()
    Objects.object["movers_and_shakers"].print_departments()  # PRINT
    Objects.object["movers_and_shakers"].print_some_movers_and_shakers()  # PRINT
    time.sleep(3)


def test_all_mobile_phones_data():
    Objects.object["home"].goto_amazon_home_page()
    Objects.object["home"].click_all_mobile_phones_button()
    Objects.object["all_mobile_phones"].print_data()  # PRINT
    Objects.object["all_mobile_phones"].print_brand_data()  # PRINT
