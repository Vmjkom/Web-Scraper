import unittest
from main.src.scraper import scrape_xml_yle

def test_htppRequest():
    artikkelit = scrape_xml_yle()
    #Varmista,että artikkeleja on imuroitu
    assert len(artikkelit) > 0
    

