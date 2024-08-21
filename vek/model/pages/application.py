from vek.model.pages.catalog_page import VekCatalogPage
from vek.model.pages.main_page import VekMainPage
from vek.model.pages.personal_data_page import VekPersonalDataPage


class Application:
    def __init__(self):
        self.main_page = VekMainPage()
        self.personal_data_page = VekPersonalDataPage()
        self.catalog_page = VekCatalogPage()


app = Application()
