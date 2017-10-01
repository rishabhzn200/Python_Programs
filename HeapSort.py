#   This program creates takes an array as an input and sort it using Heapsort method.
#   It creates MAX heap from the given input array and recursively calls MAX Heapify routine to maintain the order in the tree such that
#   each node greater than its children.
#   At the end of each iteration, max element occupies the root of the tree.

def MaxHeapify(i, hS):
    left = 2*i
    right = 2*i + 1
    largest = -1
    if left <= hS and A[left] > A[i]:
        largest = left
    else:
        largest = i

    if right <= hS and A[right] > A[largest]:
        largest = right

    if largest != i:
        #exchange largest and i and call max_heapify
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        MaxHeapify(largest, hS)



def CreateMaxHeap(hS):
    #heapSize = A.__len__()
    for i in range(hS/2, -1, -1): # run from heapsize/2 down to 0
        MaxHeapify(i, hS)
    #print("List A = " + str(A))


def HeapSort():
    global heapsize
    global A
    B = []
    CreateMaxHeap(heapsize)
    count = 0
    for i in range(heapsize, 0, -1):  # len to 2
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        count = count + 1 #num sorted elements
        MaxHeapify(0, heapsize - count) # leave the last element


def main():
    B = HeapSort()



#Sample Input
if __name__ == "__main__":
    A = [5, 13, 25, 17, 7, 20, 8, 2,  4]
    heapsize = A.__len__() - 1
    main()
    print("Sorted Array is--->\n" + str(A))