import unittest
from main.src.scraper import scrape_xml_yle

def test_ylescrapet():
    artikkelit = scrape_xml_yle()
    #Varmista,että artikkeleja on imuroitu
    assert len(artikkelit) > 0
    #Varmista, että palautettu tyyppi on lista, jotta jsoniksi muuttaminen onnistuu
    assert type(artikkelit) == list
    #Katso, että kaikkiin on tallentunut kaikki tiedot: Otsikko, julkaisupvm, teksti
    for art in artikkelit:
        assert len(art) == 3

