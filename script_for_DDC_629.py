#python script for DDC 629
#given an array and an integer "k" split the array into "k" divisions so that 
#the sum of each of the arrays is minimized. Return arrays and the maximum sum

def create_list_of_arrays(k):
    array_list = []
    for i in range(k):
        array_list.append([])
    return array_list

def split_lists(list_of_nums, k):
    partitions = create_list_of_arrays(k)
    list_of_nums.sort(reverse=True)
    # print(list_of_nums)
    while len(list_of_nums > 0):

    counter = 1
    for i in range(len(list_of_nums) / len(partitions)):
        if counter % 2 == 1:
            list_nums.sort(reverse=True)
        else:
            list_of_nums.sort()
        for j in range(len(partitions)):
            partitions[i + partions*j]
k = 3
test_array = [2, 3, 1, 4, 31, 9, 4, 1, 7]
print(create_list_of_arrays(k))
split_lists(test_array, k)