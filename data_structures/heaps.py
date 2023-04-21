import math
from typing import Union

class MinHeap(object):

    def __init__(self) -> None:
        self.size = 0
        self.items = []

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
        if(self.size==0):
            raise Exception(f'No element to peek, heap size = {self.size}')
        else:
            return self.items[0]
            
    def poll(self) -> Union[int, float]:
        if(self.size==0):
            raise Exception(f'No element to peek, heap size = {self.size}')
        
        root = self.items[0]
        self.size -= 1
        self.heapify_down()
        return root
    

    def add(self, item: Union[int, float]) -> None:
        self.size += 1
        self.items.append(item)
        self.heapify_up()


    def heapify_down(self) -> None:
        index = 0 #cero bacuse we start at the root

        """ we just check for left child becuse if there is not left
        child then theree is not a right child """
        while(self.has_left_child(index)):
            smaller_child_index = self.get_left_child_index()
            
            if( self.has_right_child(index) and self.get_right_child(index) < self.get_left_child(index) ):
                smaller_child_index = self.get_right_child_index(index)  

            if(self.items[index] and self.items[smaller_child_index]):
                break
            else:
                self.swap(index, smaller_child_index)
                index = smaller_child_index



    def heapify_up(self) -> None:
        index = self.size - 1
        
        while(self.has_parent(index) and self.get_parent(index) > self.items[index]):
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    
    def __str__(self) -> str:
        return f'MinHeap-items: {self.items}'