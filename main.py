from data_structures.heaps import MinHeap

def main():
    my_heap =MinHeap()
    
    my_heap.add(20)
    my_heap.add(17)
    my_heap.add(10)
    my_heap.add(25)
    my_heap.add(15)

    print(my_heap)


if __name__ == '__main__':
    main()