#implement the bubble sort algorithm

def bubble_sort(list):

    for i in range(0 , len(list) - 1):
        
        for j in range(0,len(list) -1 -i):
        
            if(list[j] > list[j+1]):
                helper = list[j]
                list[j] = list[j+1]
                list[j+1] = helper

    return list


numbers = [3,7,1,4,2,8,5,9]
print(bubble_sort(numbers))