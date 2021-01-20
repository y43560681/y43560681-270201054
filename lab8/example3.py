import random


def get_rand_list():
    store = []
    for i in range(5):
        store.append(random.randint(0, 10))
    return store


def get_overlap():
    intersection = []
    list1 = get_rand_list()
    list2 = get_rand_list()
    for i in list1:
        if i in list2:
            intersection.append(i)
    print(intersection)


get_overlap()