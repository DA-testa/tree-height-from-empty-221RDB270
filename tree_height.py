# python3

import sys
import threading
import numpy


def compute_height(n, parent):
    tree = [[] for i in range(n)]
    # Write this function
    max_height = 0
    
    
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
    
    if "I" in file:
        n = int(input())
        parent = list(map(int, input().split()))
    if "F" in file:
        path = "./test/"
        filen = input()
        filep = os.path.join(path, filen)
        
        
    if 'a' not in filen:
        try:
            with open(filep) as files:
                n = int(files.readline())
                parent = list(map(int, files.readline().split()))
        except FileNotFoundError:
            sys.exit()
            
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
