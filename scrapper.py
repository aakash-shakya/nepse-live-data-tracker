

from datetime import datetime
from bs4 import BeautifulSoup
# from matplotlib.pyplot import table
from filewriter import write_to_csv


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
        # self.decompose_unwanted_table_row('right')
        return table_rows


    # def get_table_row_details(self):
    #     table_row = self.find_all_table_row()
    #     # table_row_details = [ row.find('td') for row in table_row]
    #     # return table_row_details

    #     for i in range(1, len(table_row)):
    #         print(table_row[i].find('td').text)
    

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
        # print(table_row_details)
        
        arr = []
        for i in range(1, len(table_row_details)):
            # print(table_row_details[i].find_all('td'))
            arr.append(table_row_details[i].find_all('td'))
        
        final_arr = []

        with open ('filename' + str(datetime.now()) +'.xlsx', 'w') as f:
            for i in arr:
                for j in i:
                    print(j.text)
                    f.write(j.text)
                    f.write('\t')
                f.write('\n')
                print('------------------------')
        f.close()
        # print(final_arr)
        # write_to_csv()
        
