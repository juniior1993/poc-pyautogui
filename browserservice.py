import time
import webbrowser
import pyautogui
import pyperclip

IMAGE_PATH = '/home/darcijunior/PycharmProjects/poc-pyautogui/images'


class BrowserService:
    def __init__(self):
        self.browser = webbrowser.get('firefox')

    def go_to_page(self, url):
        self.browser.open(url)
        self.close_other_tabs()
        self.waiting_for_page_load()

    def close_cookie_options(self):
        position = pyautogui.locateOnScreen(f'{IMAGE_PATH}/button_confirm_cookies.png', confidence=0.7)
        if position is not None:
            pyautogui.click(position)

    def waiting_for_page_load(self, image='ready_loaded_browser.png'):
        close_time = time.time() + 20
        while True:
            if time.time() > close_time:
                break

            position = pyautogui.locateOnScreen(f'{IMAGE_PATH}/{image}', confidence=0.7)
            if position is not None:
                break

    def get(self, url):
        self.browser.open_new_tab(url)
        self.close_other_tabs()
        # pyautogui.hotkey('ctrl', 'l')
        # pyautogui.typewrite(url, interval=0.01)
        # pyautogui.press('enter')
        self.waiting_for_page_load('ready_loaded_broser_tracing.png')

    def get_html(self):
        pyautogui.press('f8')
        return pyperclip.paste()

    def close_other_tabs(self):
        pyautogui.hotkey('alt', 'w')
