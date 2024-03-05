def insertion_sort(array):
    count = 0
    for i in range(1, len(array)):
        print(array)
        last_sorted_position = array[i-1]  
        count += 1
        if array[i] < last_sorted_position:
            temp = array[i] 
            for j in range(i-1,-1,-1):  
                count += 1
                if temp < array[j]: 
                    if j == 0: 
                        array[j+1] = array[j]
                        array[j] = temp
                    else: 
                        array[j+1] = array[j]
                else: 
                    array[j+1] = temp 
                    break 
    return (f'{array} \nNumber of comparisons = {count}')

array = [5,9,3,10,45,2,0]
print(insertion_sort(array))


sorted_array = [5,6,7,8,9]
print(insertion_sort(sorted_array))

reverse_sorted_array = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
print(insertion_sort(reverse_sorted_array))
