"""
Title: Superhero Database
Author: Jackson Reid
Date-Created - 2021-02-09
"""


def getRawData(fileName):
    import csv
    tempLi = []
    fil = open(fileName)
    text = csv.reader(fil)
    for line in text:
        tempLi.append(line)
    var = tempLi.pop(0)
    return tempLi, var

rawArr, headers =
getRawData('comicBookCharData_mixed.csv')

# rawArr is a 2D array holding all the Superhero data
# headers is a variable that holds the list of all the column headers.

print(rawArr[0])
