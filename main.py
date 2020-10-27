"""
    Generate a random, ordered list of integers and benchmark with the
    recursive and iterative binary search functions.
"""
import random
from time import time


def iterative_binary_search(alist, item):
    start = time()
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time()
    return found, end - start


def recursive_binary_search(alist, item):
    start = time()
    if len(alist) == 0:
        end = time()
        return False, end - start
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            end = time()
            return True, end - start
        else:
            if item < alist[midpoint]:
                end = time()
                return recursive_binary_search(alist[:midpoint], item), end - start
            else:
                end = time()
                return recursive_binary_search(alist[midpoint + 1:], item), end - start


random_list = []
for i in range(0, 20):
    n = random.randint(1, 30)
    random_list.append(n)

if __name__ == '__main__':
    print(iterative_binary_search(random_list, 12))
    print(recursive_binary_search(random_list, 12))
