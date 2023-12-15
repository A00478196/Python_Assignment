# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:59:33 2023

@author: dell
"""

'List to be manipulated'
our_list = [1,2,3,4]


'Function stack which follows the LIFO - last in first out'
def stack(our_list, operation, new_element=None):
    if operation=="add":
        print("Adding new element to the stack ")
        our_list.append(new_element)
        print(our_list)
    elif operation=="remove":
        print("Adding remove an element from the stack ")
        our_list.pop()
        print(our_list)

    else:
        our_list


'Function stac'
def queue(our_list, operation, new_element=None):
    if operation=="add":
        print("Adding new element to the queue ")
        our_list.append(new_element)
        print(our_list)
    elif operation=="remove":
        print("Adding remove an element from the queue ")
        our_list.pop(0)
        print(our_list)

    else:
        our_list
    
def main():
    stack(our_list, "add", 0)
    stack(our_list, "remove")
    queue(our_list, "add", 5)
    queue(our_list, "remove")
    


if __name__ == "__main__":
    main()



    
