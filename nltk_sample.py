from nltk.sentiment.vader import SentimentIntensityAnalyzer
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

workbook = xlrd.open_workbook('twitter_Data.xls')
rb = open_workbook("twitter_Data.xls")
wb = copy(rb)
s = wb.get_sheet(0)

worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows - 1
curr_row = 0
column=0
sid = SentimentIntensityAnalyzer()
while curr_row < num_rows:
        curr_row += 1

        value = worksheet.cell(curr_row, column)
        print (str(value))
        sentence = str(value)
        ss = sid.polarity_scores(sentence)
        print(ss)
        str1 = str(ss)
        s.write(curr_row, 2, str1)
wb.save('twitter_Data.xls')