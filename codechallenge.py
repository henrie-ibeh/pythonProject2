"""
new = []
def count(arr):
    new = [1 for x in arr if x + 1 in arr]
    return sum(new)
count([1,3,2,3,5,0])
"""
# convert to int if int in list
import math

"""
g = ["5", "-2", "4", "C", "D", "9", "+", "+"]
new = [int(x) if x.lstrip('-').isnumeric() else x for x in g]
print(new)


inp = "ab-cd"
string = inp[::-1]
print(string)
"""
"""
a = [1, 2, 3, 4, 5]
b = [1, 2, 3J, 4, 5]
x = []


# Python3 program to find singles in a given binary tree

# A Binary Tree Node
class Node:

    # A constructor to create new tree node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Function to print all non-root nodes that don't have
# a sibling
def printSingles(root):
    # Base Case
    if root is None:
        return

    # If this is an internal node , recur for left
    # and right subtrees
    if root.left is not None and root.right is not None:
        printSingles(root.left)
        printSingles(root.right)

    # If left child is NULL, and right is not, print
    # right child and recur for right child
    elif root.right is not None:
        print(root.right.key),
        printSingles(root.right)

    # If right child is NULL and left is not, print
    # left child and recur for left child
    elif root.left is not None:
        print(root.left.key),
        printSingles(root.left)


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.left.left = Node(6)
printSingles(root)
"""

arr = [2,2,3,4]
def findl(arr):
    grow = []
    for x in arr:
        if arr.count(x) == x: grow.append(x)

    if len(grow) > 1:
        grow.sort()
        print(grow[-1])
        return grow[-1]
    elif len(grow) == 1:
        print(grow[0])
        return grow[0]
    else:
        print(-1)
        return -1

findl(arr)


def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)


# Function to left Rotate arr[] of size n by 1*/
def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


# utility function to print an array */
def printArray(arr, size):
    for i in range(size):
        print("% d" % arr[i], end=" ")


# Driver program to test above functions */
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)


a_b_c = [2445,133,12454,123]
print("\n",max(a_b_c))

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1

print(math.pow(3, 2))

x = 1;
while True:
    if x % 5 == 0:
        break
    print(x)
    x += 1
print(math.sqrt(9))
