import math
from typing import Union

class MinHeap(object):
    """ 
    This is a minimum heap implementation, it was design whit the purpose
    of being a heap of numbers, either int or float.

    warning:
        this is not a complete/full heap implentation, since it lacks of heap
        operations such as remove 
    """

    def __init__(self) -> None:
        self.size = 0
        self.items = []

    def get_item(self, index: int) -> Union[int, float]:
        return self.items[index]

    def get_left_child_index(self, parent_index: int) -> int:
        return 2*parent_index + 1
    
    def get_right_child_index(self, parent_index: int) -> int:
        return 2*parent_index + 2
    
    def get_parent_index(self, child_index: int) -> int:
        if(child_index==0):
            return 0
        else:
            return (child_index-1)//2
    
    def has_left_child(self, index: int) -> bool:
        return self.get_left_child_index(index) < self.size
    
    def has_right_child(self, index: int) -> bool:
        return self.get_right_child_index(index) < self.size
    
    def has_parent(self, index: int) -> bool:
        return self.get_parent_index(index) >= 0
    
    def get_left_child(self, index: int) -> Union[int, float]:
        return self.items[ self.get_left_child_index(index) ]
    
    def get_right_child(self, index: int) -> Union[int, float]:
        return self.items[ self.get_right_child_index(index) ]
    
    def get_parent(self, index: int) -> Union[int, float]:
        return self.items[ self.get_parent_index(index) ]
    

    def swap(self, indexA: int, indexB: int) -> None:
        temp = self.items[indexA]
        self.items[indexA] = self.items[indexB]
        self.items[indexB] = temp

    def peek(self) -> Union[int, float]:
        """ Returns the values of the first element of the heap whitout removing it """
        if(self.size==0):
            raise Exception(f'No element to peek, heap size = {self.size}')
        else:
            return self.items[0]
            
    def poll(self) -> Union[int, float]:
        """ Removes the first elments of the heap """
        if(self.size==0):
            raise Exception(f'No element to peek, heap size = {self.size}')
        
        root = self.items[0]
        self.size -= 1
        self.heapify_down()
        return root
    

    def add(self, item: Union[int, float]) -> None:
        """ Adds a new item to the heap """
        self.size += 1
        self.items.append(item)
        self.heapify_up()


    def heapify_down(self) -> None:
        """ Takes the firts element of the heap  and heapify this elements down the heap """
        index = 0 #cero bacuse we start at the root

        """ we just check for left child becuse if there is not left
        child then theree is not a right child """
        while(self.has_left_child(index)):
            smaller_child_index = self.get_left_child_index()
            
            if( self.has_right_child(index) and self.get_right_child(index) < self.get_left_child(index) ):
                smaller_child_index = self.get_right_child_index(index)  

            if(self.items[index] < self.items[smaller_child_index]):
                break
            else:
                self.swap(index, smaller_child_index)
                index = smaller_child_index



    def heapify_up(self) -> None:
        """ Takes the last element of the heap  and heapify this elements up the heap """
        index = self.size - 1

        while(self.has_parent(index) and (self.get_parent(index) > self.items[index]) ):
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    
    def __str__(self) -> str:        
        return f'MinHeap-items: {self.items}'
    



class MaxHeap(MinHeap):

    def heapify_up(self) -> None:
        """ Same as the one from MinHeap, except for the conditional in the while loop """
        index = self.size - 1

        while(self.has_parent(index) and (self.get_parent(index) < self.items[index]) ):
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)
    

    def heapify_down(self) -> None:
        """ Same as the one from MinHeap, except for the conditionals in the if staments """        
        index = 0

        while(self.has_left_child(index)):
            bigger_child_index = self.get_left_child_index()
            
            if( self.has_right_child(index) and self.get_right_child(index) > self.get_left_child(index) ):
                bigger_child_index = self.get_right_child_index(index)  

            if(self.items[index] > self.items[bigger_child_index]):
                break
            else:
                self.swap(index, bigger_child_index)
                index = bigger_child_index
    
    
    def __str__(self) -> str:        
        return f'MaxHeap-items: {self.items}'