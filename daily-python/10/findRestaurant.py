'''
Date: 2022-10-16 15:20:28
LastEditors: r7000p
LastEditTime: 2022-10-16 20:08:32
FilePath: \Daily\daily-python\10\findRestaurant.py
'''

def findRestaurant(list1, list2):
    res, Restaurant = [], []
    hashmap = dict()
    # list1 的餐馆优先级
    for i in range(len(list1)):
        hashmap[list1[i]] = i
    # list1 和 list2 的餐馆优先级
    for i in range(len(list2)):
        if list2[i] in hashmap:
            hashmap[list2[i]] += i
            Restaurant += [(list2[i], hashmap[list2[i]])]
    Restaurant = sorted(Restaurant, key=lambda x : x[1])
    num = Restaurant[0][1]
    for i in Restaurant:
        if i[1] == num:
            res += [i[0]]
    return res

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
print(findRestaurant(list1, list2))