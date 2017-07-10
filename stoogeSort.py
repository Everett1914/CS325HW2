#Everett Williams
#08JUL17 as of 09JUL17
#HW2 Problem 5
#Stooge Sort program

#Stooge sort sorts as follows:
#	If the value at the end is smaller than the value at the start, swap them.
#	If there are 3 or more elements in the list, then:
#		1. Stooge sort the initial 2/3 of the list
#		2. Stooge sort the final 2/3 of the list
#		3. Stooge sort the initial 2/3 of the list again
#	else: exit the procedure
#   The followng website assisted in the formatting of the arrays in the
#   recursive calls and the idea to calculate 1/3 instead of 2/3 then use the
#   array structures to calculate 2/3.
#   https://en.wikipedia.org/wiki/Talk%3AStooge_sort

import math

def stoogeSort(arr):
    if len(arr) == 2 and arr[1] < arr[0]:
        arr[0], arr[1] = arr[1], arr[0]

    if len(arr) > 2:
        x = int(len(arr)/3)  #calculates 1/3 of the length of the array
        m = math.ceil(x)
        arr[:-m] = stoogeSort(arr[:-m])  #stooge sort initial two thirds
        arr[m:] = stoogeSort(arr[m:])  #stooge sort final two thirds
        arr[:-m] = stoogeSort(arr[:-m])  #stooge sort initial two thirds for corrections
    return arr

#read data from data.txt and store data as integers into the list dataArray and
#return unsorted array
def readArray():
    with open('data.txt') as data:
        dataArray = []
        for line in data:
            line = line.split() # to deal with blank
            if line:            # lines (ie skip them)
                for value in line:
                    num = int(value)
                    dataArray.append(num)
    return dataArray

#write sorted array to stooge.out
def outPutArray(array):
    with open('stooge.out', 'w') as outPutFile:
        for val in array:
            num = str(val)
            outPutFile.write(num + " ")

#Main program
unsortedArray = readArray()
if unsortedArray[0] != 0:
    del unsortedArray[0]
    sortedArray = stoogeSort(unsortedArray)
    print(sortedArray)
    outPutArray(sortedArray)
