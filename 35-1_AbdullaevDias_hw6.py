def bubble_sort(list):
    for i in range(0, len(list) - 1):
        for j in range(len(list) - 1):
            if (list[j] > list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


list = [2, 10, 8, 6, 4, 9, 1, 3, 5, 7]
print("Несортированный лист ", list)
print("Сортированный лист: ", bubble_sort(list))


def binarySearch(list1, N):
    first = 0
    last = len(list1) - 1
    resultOk = False

    while first <= last and not resultOk:
        middle = (first + last) // 2
        val = list1[middle]
        if val == N:
            resultOk = True
        if val > N:
            last = middle - 1
        else:
            first = middle + 1
    return resultOk


list1 = [1, 3, 5, 8, 10, 11, 14, 15, 20, 60, 90]
value = 100
result = binarySearch(list1, value)
if result:
    print('элемент найден')
else:
    print('элемент не найден')
