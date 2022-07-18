
from bs4 import BeautifulSoup
from filewriter import generate_excel_file


class Scrapper:
    def __init__(self, response_text):
        self.response_text = response_text

    def get_soup(self):
        soup = BeautifulSoup(self.response_text, 'html.parser')
        return soup

    def find_table(self):
        soup = self.get_soup()
        table = soup.find('table', {'class': 'table my-table'})
        return table

    def find_table_row(self, row_class):
        try:
            table = self.find_table()
            table_row = table.find('tr', {'align': row_class})
            return table_row
        except Exception as e:
            print(e)

    def decompose_unwanted_table_row(self, row_class):
        table_row = self.find_table_row(row_class)
        table_row.decompose()

    def find_all_table_row(self):
        table = self.find_table()
        table_rows = table.find_all('tr')
        return table_rows


    '''
        arr = [
            [
                0,1,2
            ],
            [
                4,5,6
            ]
        ]
    
    '''

    def get_table_row_details_text(self):
        table_row_details = self.find_all_table_row()
        
        arr = []
        for i in range(1, len(table_row_details)):
            arr.append(table_row_details[i].find_all('td'))
        
        generate_excel_file('nepse_floorsheet', arr)

