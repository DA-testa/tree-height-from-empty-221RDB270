# python3

import sys
import threading
import numpy


def compute_height(n, parent):
    # Write this function
    max_height = 0
    
    tree[ [] for i in range(n) ]
        for i in range(n): 
            if parent[i] == -1:
                root = i  
            else: 
                tree[parent[i]].append(i)
        
    place = [root] 
    while place:
        next = []
        for node in place:
            next += tree[node]
        place = next
        max_height += 1
             
               
              
    # Your code here 
    return max_height 
 
  
def main():
    # implement input form keyboard and from files
    file = input()
    
    if file[0] == "I":
        file = input()
        
    if file and 'a' not in file:
        try:
            with open(file, 'r') as file_1:
                b = int(file_1.readline())
                parent = list(map(int,flie_1.readline().split()))
    else:
        b = int(input())
        parent = list(map(int, input().split()))
        
        if b[0] == "I":
            b = input()
            
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    max_height = compute_height(n, parent)
    print(max_height)
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

# print(numpy.array([1,2,3]))
