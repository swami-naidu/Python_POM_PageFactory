from Base.BaseClass import BaseClass
from Pages.AmazonAllMobilePhonesPage import AllMobilePhones
from Pages.AmazonBestSellersPage import AmazonBestSellers
from Pages.AmazonHomePage import AmazonHome
from Pages.AmazonMoversShakersPage import MoversAndShakers
from Pages.AmazonNewReleasesPage import AmazonNewReleases
from Pages.AmazonNewReleases_BabyProductsPage import BabyProducts
from Pages.AmszonNewReleases_RenewedPage import Renewed


class Objects:
    driver = None
    wait = None
    object = {}
    base = BaseClass()

    def initialise_objects(self, driver, wait):
        Objects.object.update({"home": AmazonHome(driver, wait)})
        Objects.object.update({"best_sellers": AmazonBestSellers(driver, wait)})
        Objects.object.update({"new_releases": AmazonNewReleases(driver, wait)})
        Objects.object.update({"new_releases_renewed": Renewed(driver, wait)})
        Objects.object.update({"new_releases_baby_products": BabyProducts(driver, wait)})
        Objects.object.update({"movers_and_shakers": MoversAndShakers(driver, wait)})
        Objects.object.update({"all_mobile_phones": AllMobilePhones(driver, wait)})


