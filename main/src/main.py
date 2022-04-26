from scraper import scrape_xml

def main():
    
    for a in scrape_xml().keys():
        print(a)


if __name__ == "__main__":
    main()