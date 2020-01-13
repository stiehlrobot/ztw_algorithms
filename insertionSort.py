#implement insertion sort

def insertion_sort(list):

    for i in range(1, len(list)):

        currentIndex = i
        currentValue = list[i]

        while currentIndex > 0 and list[currentIndex - 1] > currentValue:
            list[currentIndex] = list[currentIndex-1]
            currentIndex -= 1

        list[currentIndex] = currentValue
            

    return list

            

                


numbers = [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
print(insertionSort(numbers))
print(insertion_sort(numbers))
