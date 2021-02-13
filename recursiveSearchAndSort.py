"""
Title: Recursive Superhero Search and Sort
Author: Jackson Reid
Date-Created: 2021-02-11
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


def quickSort(LIST, FIRST_INDEX, LAST_INDEX):
    """
    Uses a pivot value to recursively sort through the list.
    :param LIST: UNSORTED LIST
    :param FIRST_INDEX: Left-most index value
    :param LAST_INDEX: Right-most index value
    :return:
    """

    if FIRST_INDEX < LAST_INDEX:

        PIVOT_VALUE = LIST[FIRST_INDEX]
        LEFT_INDEX = FIRST_INDEX + 1
        RIGHT_INDEX = LAST_INDEX

        DONE = False

        while not DONE:
            while LEFT_INDEX <= RIGHT_INDEX and LIST[LEFT_INDEX] <= PIVOT_VALUE:
                LEFT_INDEX = LEFT_INDEX + 1
            while RIGHT_INDEX >= LEFT_INDEX and LIST[RIGHT_INDEX] >= PIVOT_VALUE:
                RIGHT_INDEX = RIGHT_INDEX - 1
            if RIGHT_INDEX < LEFT_INDEX:
                DONE = True
            else:
                TEMP = LIST[LEFT_INDEX]
                LIST[LEFT_INDEX] = LIST[RIGHT_INDEX]
                LIST[RIGHT_INDEX] = TEMP

        TEMP = LIST[FIRST_INDEX]  # PIVOT VALUE
        LIST[FIRST_INDEX] = LIST[RIGHT_INDEX]
        LIST[RIGHT_INDEX] = TEMP

        # Recursive part
        quickSort(LIST, FIRST_INDEX, RIGHT_INDEX - 1)  # Continues down left branch
        quickSort(LIST, RIGHT_INDEX + 1, LAST_INDEX)  # Continues down right branch


def recursiveBinarySearch(LIST, VALUE):
    MIDPOINT = len(LIST) // 2
    for row in NUMBERS:
        if row[0] == VALUE:
            # BASE CASE
            for i in range(11):
                print(headers[i] + ": " + row[i])
                i = i + 1
            return MIDPOINT
    else:
        if VALUE < LIST[MIDPOINT]:
            return recursiveBinarySearch(LIST[:MIDPOINT], VALUE)
        else:
            return recursiveBinarySearch(LIST[MIDPOINT + 1:], VALUE)


# Main program code
if __name__ == "__main__":
    Running = True
    while Running:
        NUMBERS = rawArr
        quickSort(NUMBERS, 0, len(NUMBERS) - 1)
        INPUT_VALUE = input("What is the character ID?")
        for row in NUMBERS:
            if row[0] != INPUT_VALUE:
                RETURN = False
            else:
                RETURN = True
                break
        if not RETURN:
            print("Error: Invalid entry")
        else:
            recursiveBinarySearch(NUMBERS, INPUT_VALUE)

            again = input("Do you want to search again?(y/N)")
            if again == "y":
                pass
            else:
                Running = False
