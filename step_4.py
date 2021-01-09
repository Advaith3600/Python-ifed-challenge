import time
import numpy as np


def standard(all_elements, subset_elements):
    """
    Standard way to find the intersection of two sets
    :param all_elements:
    :param subset_elements:
    :return:
    """
    start = time.time()
    verified_elements = []
    for element in subset_elements:
        if element in all_elements:
            verified_elements.append(element)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))


def numpy(all_elements, subset_elements):
    """
    Intersection of two sets using built-in functions of numpy
    :param all_elements:
    :param subset_elements:
    :return:
    """
    start = time.time()
    verified_elements = np.intersect1d(np.array(subset_elements), np.array(all_elements))

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))


def usingsets(all_elements, subset_elements):
    """
    Intersection of two sets using built-in set data structure of Python
    :param all_elements:
    :param subset_elements:
    :return:
    """
    start = time.time()
    verified_elements = set(subset_elements) & set(all_elements)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))


with open('subset_elements.txt') as f:
    subset_elements = f.read().split('\n')

with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')

print(standard.__doc__)
standard(all_elements, subset_elements)

print(numpy.__doc__)
numpy(all_elements, subset_elements)

print(usingsets.__doc__)
usingsets(all_elements, subset_elements)
