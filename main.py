import time ##so we can time our program
from customSort import * ## This lets you use the sorting functions

def main():
	#import values.txt
	try:
		file = open("values.txt", 'r')
	except IOError:
		print "File not Found", "values.txt"
	##put values in array
	values = []
	values2 = []
	values3 = []
	values4 = []
	for line in file:
		#lines = file.read().split('\n')
		values.append(line)			
	#return values
	values2 = values
	values3 = values
	values4 = values
	##sort & time
	BubbleTime = time.time()
	bubbleSort(values)
	BubbleTime = time.time() - BubbleTime
	
	#Selection sort
	SelectionTime = time.time()
	selectionSort(values2)
	SelectionTime = time.time() - SelectionTime
	
	#Insertion Sort
	InsertionTime = time.time()
	insertionSort(values3)
	InsertionTime = time.time() - InsertionTime
	
	#Python Sort
	PythonTime = time.time()
	values4.sort()
	PythonTime = time.time() - PythonTime
	
	##print results
	print("Time to sort with Bubble sort: ", BubbleTime)
	print("Time to sort with Selection sort: ", SelectionTime)
	print("Time to sort with Insertion sort: ", InsertionTime)
	print("Time to sort with Python's sort: ", PythonTime)


main()

    
