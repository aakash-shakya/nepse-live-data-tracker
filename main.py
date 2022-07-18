from handleRequests import HandleRequests
from scrapper import Scrapper

class NepseScrapper:
    def __init__(self, url, body):
        self.url = url
        self.body = body
        self.handle_requests = HandleRequests(self.url, self.body)

    def get_text(self):
        return self.handle_requests.get_response_text()

    def scrape_data(self):
        scrapper = Scrapper(self.get_text())
        return scrapper.get_table_row_details_text()





if __name__ == "__main__":
    url = "http://www.nepalstock.com/floorsheet/"
    body = {
        "contract-no": "",
        "stock-symbol": "",
        "buyer": "",
        "seller": "",
        "_limit": 50
    }
    nepse_scrapper = NepseScrapper(url, body)
    nepse_scrapper.scrape_data()
    