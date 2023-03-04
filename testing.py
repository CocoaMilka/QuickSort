from quickSort import *

a = [1, 5, 7, 6, 3, 5, 1, 3, 4]

b = QuickSortAlgorithm(a)

b.printArray()

b.QuickSort(0, len(b.array) - 1)

print("After sorting: ")

b.printArray()
