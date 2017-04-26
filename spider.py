# !-*- utf-8 -*-
# !/bin/python
import multiprocessing
import urllib.request
import os
# import csv
# import json

from multiprocessing import Process


class etf_spider(Process):

    def __init__(self, dta):
        self.dta = dta
        Process.__init__(self)

    def get_data(self, stock_name):
        fields = ["Date", "Open", "High", "Low",
                  "Close", "Volume", "Adj Close"]
        # today = datetime.date.today()
        # stock_data = {}
        # stock_data['name'] = stock_name
        # etf = Share(stock_name)
        # stock_data['historicals'] = etf.get_historical(
        #     '2006-02-01', str(today))
        url = "http://ichart.finance.yahoo.com/table.csv?g=d&f=2017&e=12&c=1950&b=10&a=7&d=7&s=%s" % (
            stock_name)
        data = urllib.request.urlopen(url)
        csvfileName = stock_name + '.csv'
        filename_with_path = os.path.join(os.path.join(
            os.path.dirname(__file__), os.pardir, 'data', csvfileName))
        csv_file = open(filename_with_path, 'wb')
        csv_file.write(data.read())
        csv_file.close()
        # jsonfileName = stock_name + '.json'
        # jsonfile = open(jsonfileName, 'w')
        # reader = csv.DictReader(data.read().decode('utf-8'), fields)
        # for row in reader:
        #     print(row)
        #     json.dump(row, jsonfile)
        #     jsonfile.write('\n')

    def run(self):
        try:
            self.get_data(self.dta)
        except Exception as e:
            print("============= some_warning =================")
            print(self.dta)
            print(str(e))
            print("============= end_warning =================")


if __name__ == '__main__':
    etf_list = open('etf_list.txt', 'r', encoding='UTF-8')
    for line in etf_list:
        stock_name = (line.replace(' ', '').replace('\n', ''))
        p = etf_spider(stock_name)
        p.start()
