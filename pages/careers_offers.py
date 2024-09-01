from pages.base_page import BasePage


class CareersOffersPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.job_mode_dropdown = self.page.get_by_placeholder("On-site/remote/hybrid")
        self.see_more_button = self.page.get_by_role("button", name="See more")
        self.position_counter = self.page.locator('h1[class="sc-eca978c5-2 hdjZOx"]')
        self.job_offers = self.page.locator('div[class="sc-acbd9527-0 jxxKIe"]')
        self.job_links = self.job_offers.locator('a[class="sc-1781beb0-2 fSFUhE"]')
        self.job_names_locations = self.job_offers.locator('span')
        self.job_work_mode = self.job_offers.locator('p[class="sc-5cd84594-0 diUEBQ"]')

    def navigate(self):
        self.page.goto(f'{self.home_url}/careers-offers')

    def filer_by_job_mode(self, job_mode):
        self.job_mode_dropdown.click()
        self.page.locator('ul[id=":R3ifm:-listbox"]').get_by_text(job_mode).click()

    def see_more(self, see_all=False):
        while self.see_more_button.count() > 0:
            self.see_more_button.click()
            if not see_all:
                break

    def get_job_info(self):
        offer_urls, job_data = [], []
        if self.job_offers.count() > 0:
            for row in self.job_links.all():
                offer_urls.append(row.get_attribute('href'))
            role_names_locations = self.job_names_locations.all_text_contents()
            role_names_locations = list(filter('Details'.__ne__, role_names_locations))
            role_names = role_names_locations[::2]
            locations = role_names_locations[1::2]
            work_modes = self.job_work_mode.all_text_contents()

            for role_name, work_mode, location, offer_url in list(zip(role_names, work_modes, locations, offer_urls)):
                job_data_dict = {
                    'role_name': role_name,
                    'work_mode': work_mode,
                    'location': location,
                    'offer_url': self.home_url + offer_url
                }
                job_data.append(job_data_dict)

        return job_data
