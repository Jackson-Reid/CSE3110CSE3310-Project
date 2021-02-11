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


def quickSort(list, firstIndex, lastIndex):
    """
    Uses a pivot value to recursively sort the list provided
    :param list: Unsorted list
    :param firstIndex: Left-most index value
    :param lastIndex: Right most index value
    :return: Sorted List
    """

    if firstIndex < lastIndex:
        pivotValue = list[firstIndex]
        leftIndex = firstIndex + 1
        rightIndex = lastIndex

        done = False

        while not done:
            while leftIndex <= rightIndex and list[leftIndex] <= pivotValue:
                leftIndex = leftIndex + 1
            while rightIndex >= leftIndex and list[rightIndex] >= pivotValue:
                rightIndex = rightIndex - 1
            if rightIndex < leftIndex:
                done = True
            else:
                temp = list[leftIndex]
                list[leftIndex] = list[rightIndex]
                list[rightIndex] = temp
        temp = list[firstIndex]  # Pivot value
        list[firstIndex] = list[rightIndex]
        list[rightIndex] = temp

        # Recursive part below
        quickSort(list, firstIndex, rightIndex - 1)  # Traverses through left branch
        quickSort(list, rightIndex + 1, lastIndex)  # Traverses through right branch


# Main program code
if __name__ == "__main__":
    numbers = rawArr
    print(numbers)
    print(quickSort(numbers, 0, len(numbers) - 1))
