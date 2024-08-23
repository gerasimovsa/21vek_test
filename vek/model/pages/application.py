from vek.model.components.catalog_tab import VekCatalogTab
from vek.model.components.footer import VekFooter
from vek.model.components.header import VekHeader
from vek.model.components.search_bar import VekSearchBar
from vek.model.pages.main_page import VekMainPage
from vek.model.pages.personal_data_page import VekPersonalDataPage


class Application:
    def __init__(self):
        # pages
        self.main_page = VekMainPage()
        self.personal_data_page = VekPersonalDataPage()
        # components
        self.catalog_tab = VekCatalogTab()
        self.header = VekHeader()
        self.footer = VekFooter()
        self.search_bar = VekSearchBar()


app = Application()
