import pytest
from pages.careers_offers import CareersOffersPage
from playwright.sync_api import expect, Page
from utilities.utilities import *

config = get_config()


@pytest.fixture
def load_page(page: Page):
    _page = CareersOffersPage(page)
    _page.home_url = config['url']
    _page.navigate()
    _page.allow_cookies()
    yield _page


def test_check_careers_offers_counter(load_page):
    _page = load_page
    _page.filer_by_job_mode('Remote')
    _page.see_more(see_all=True)
    expect(_page.position_counter).to_have_text(f'{str(_page.job_offers.count())} positions in all locations')
    offers = _page.get_job_info()
    save_dict_to_json(offers, config["careers_file_name"])

