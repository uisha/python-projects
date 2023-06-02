# https://www.geeksforgeeks.org/how-to-check-the-execution-time-of-python-script/
import functions
import time
from insertionSort import insertion_sort as iSort
from mergeSort import merge_sort as mSort

str = input("Enter String: \n")
size = len(str)

strList = []

functions.divideString(str, strList, len(str))

# functions.printList(strList)

# # Sorting
start = time.time()
# iSort(strList)
mSort(strList)
end = time.time()

print("\n\n\nSorted:")
functions.printList(strList)

print("\n\nThe time of execution of above program is :",
      (end-start) * 10**3, "ms")