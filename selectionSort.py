#implement selection sort algorithm


def selection_sort(list):

    for i in range(0,len(list)-1):

        indexOfSmallestNum = i
        smallestNum = list[i]
        for j in range(i, len(list)):
            
            
            if(list[j] < smallestNum):
                smallestNum = list[j]
                indexOfSmallestNum = j

        helper = list[i]
        list[i] = list[indexOfSmallestNum]
        list[indexOfSmallestNum] = helper
        

    return list


numbers = [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
print(selection_sort(numbers))