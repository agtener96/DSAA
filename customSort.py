def bubbleSort(seq):
	for passnum in range(len(seq)-1,0,-1):
		for i in range(passnum):
			if seq[i]>seq[i+1]:
				temp = seq[i]
				seq[i] = seq[i+1]
				seq[i+1] = temp

def selectionSort(seq):
	for fillslot in range(len(seq)-1,0,-1):
		positionOfMax=0
		for location in range(1,fillslot+1):
			if seq[location]>seq[positionOfMax]:
				positionOfMax = location

		temp = seq[fillslot]
		seq[fillslot] = seq[positionOfMax]
		seq[positionOfMax] = temp

def insertionSort(seq):
	for index in range(1,len(seq)):
		currentvalue = seq[index]
		position = index

	while position>0 and seq[position-1]>currentvalue:
		seq[position]=seq[position-1]
		position = position-1
	seq[position]=currentvalue
