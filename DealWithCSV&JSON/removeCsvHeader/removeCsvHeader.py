#! usr/bin/env python3
# removeCsvHeader.py  - Remove the header from all CSV files in the current working direcrtory

import os, csv

os.makedirs('headerRemoved', exist_ok=True)

# 循环遍历每一个CSV文件
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue                            # skip non-csv files
    print('Removing header from ' + csvFilename + '...')

    # 读入CSV文件
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue                        # skip first row
        csvRows.append(row)
    csvFileObj.close()

    # 写入CSV文件，没有第一行
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
    