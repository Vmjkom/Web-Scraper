from scraper import scrape_il, scrape_xml_yle, to_json
import sys

def main():
    ehto = True
    while(ehto):
        sivusto = str(input('Syötä yle tai iltalehti: ').lower())
        if sivusto == 'yle':
            yle_artikkelit = scrape_xml_yle()
            nimi = input('Anna nimi tiedostolle johon json data tallenetaan: ')
            try:
                with open(nimi+'.json', 'xb') as f:
                    f.write(to_json(yle_artikkelit))
                    ehto = False
                    break
            except FileExistsError:
                print("Nimi on jo käytössä")
        if sivusto == 'iltalehti':
            il_artikkelit = scrape_il()
            nimi = input('Anna nimi tiedostolle johon json data tallenetaan: ')
            try:
                with open(nimi+'.json', 'xb') as f:
                    f.write(to_json(il_artikkelit))
                    ehto = False
                    break
            except FileExistsError:
                print("Nimi on jo käytössä")
            
        else:
            print("Väärä syöte")

    
        
if __name__ == "__main__":
    main()