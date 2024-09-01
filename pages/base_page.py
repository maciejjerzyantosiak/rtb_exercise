class BasePage:
    def __init__(self, page):
        self.page = page
        self.home_url = 'https://www.rtbhouse.com'
        self.cookies_allow_button = page.get_by_role("button", name="Allow all")

    def allow_cookies(self):
        self.cookies_allow_button.click()
