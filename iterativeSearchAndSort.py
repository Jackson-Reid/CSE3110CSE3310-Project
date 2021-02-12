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


rawArr, headers = getRawData('comicBookCharData_mixed.csv')


# rawArr is a 2D array holding all the Superhero data
# headers is a variable that holds the list of all the column headers.


def insertionSort(LIST):
    """
    Split the list into sorted and unsorted sections, then insert values into their correct location within the sorted list
    :param LIST: UNSORTED LIST
    :return: SORTED LIST
    """

    for i in range(1, len(LIST)):
        INDEX_VALUE = LIST[i]
        SORTED_INDEX = i - 1
        # Travels through the sorted part backwards

        while SORTED_INDEX >= 0 and INDEX_VALUE < LIST[SORTED_INDEX]:
            LIST[SORTED_INDEX + 1] = LIST[SORTED_INDEX]
            SORTED_INDEX = SORTED_INDEX - 1

        LIST[SORTED_INDEX + 1] = INDEX_VALUE
    return LIST



def linearSearch():
    """

    :return:
    """
    for row in SORTED_NUMBERS:
        if row[0] != INPUT_VALUE:
            pass
        else:
            for i in range(11):
                print(headers[i] + ": " + row[i])
                i = i + 1


# Test

if __name__ == "__main__":
    Running = True
    RETURN = False
    while Running:
        NUMBERS = rawArr
        SORTED_NUMBERS = (insertionSort(NUMBERS))
        INPUT_VALUE = input("What is the character ID?")
        for row in SORTED_NUMBERS:
            if row[0] != INPUT_VALUE:
                RETURN = False
            else:
                RETURN = True
                break

        linearSearch()
        if not RETURN:
            print("Error: Invalid entry")

        again = input("Do you want to search again?(y/N)")
        if again == "y":
            pass
        else:
            Running = False