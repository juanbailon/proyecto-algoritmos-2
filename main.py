from data_structures.heaps import MinHeap, MaxHeap

def main():
    my_heap =MaxHeap()
    
    my_heap.add(20)
    my_heap.add(17)
    my_heap.add(10)
    my_heap.add(25)
    my_heap.add(15)
    my_heap.add(21)

    print(my_heap)


if __name__ == '__main__':
    main()