import os

from browserservice import BrowserService
from parserservice import ParserService

MAIN_PAGE_URL = 'https://www.hapag-lloyd.com/en/home.html'
BL_PAGE_URL = 'https://www.hapag-lloyd.com/en/online-business/track/track-by-booking-solution.html?blno='
CONTAINER_PAGE_URL = 'https://www.hapag-lloyd.com/en/online-business/track/track-by-booking-solution.html?view=S8510&container='


class HapagLloydHandle:
    def __init__(self, folder_to_save):
        self.folder_to_save = None
        self.bl = None
        self.folder_name = folder_to_save
        self.browser = BrowserService()
        self.browser.go_to_page(MAIN_PAGE_URL)
        self.browser.close_cookie_options()

    def handle(self, bl):
        self.bl = bl
        self.folder_to_save = self.make_dir(bl)
        self.browser.get(BL_PAGE_URL + self.bl)
        page = self.browser.get_html()
        containers = ParserService().get_containers(page)
        self.save_html_content(page, 'bl_' + self.bl)

        for container in containers:
            self.container_handle(container)

    def container_handle(self, container):
        self.browser.get(CONTAINER_PAGE_URL + container)
        container_html = self.browser.get_html()
        self.save_html_content(container_html, container)
        print(container + ' saved')

    def save_html_content(self, content, name):
        file = open(self.folder_to_save + name + '.html', 'w')
        file.write(content)
        file.close()

    def make_dir(self, document_name):
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

        if not os.path.exists(self.folder_name + document_name):
            os.makedirs(self.folder_name + document_name)

        return self.folder_name + document_name + '/'
