from web_scraper import __version__
from web_scraper.web_scarper import *


def test_version():
    assert __version__ == '0.1.0'


def test_get_citations_needed_count():
    actual= get_citations_needed_count()
    # print(actual)
    excepted='Number of citation 5'
    assert actual==excepted


# test_get_citations_needed_count()