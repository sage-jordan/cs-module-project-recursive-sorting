# TO-DO: complete the helper function below to merge 2 sorted arrs
def merge(left, right):
    left_index = 0
    right_index = 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
     # Your code here

    if len(arr) <= 1:  # base case
        return arr

    # divide arr in half and merge sort recursively
    half = int(len(arr) / 2)
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge(left, right)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1

    # Checks if already sorted
    if(arr[mid] <= arr[start2]):
        return
    
    # while start < mid and 2nd < end 
    while (start <= mid and start2 <= end):
        # if first counter is smaller, move to next index
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            # else, save larger value/index
            value = arr[start2]
            index = start2

            # and while that index isn't the starting point, 
            while (index != start):
                # completely stuck. 


def merge_sort_in_place(arr, l, r):
    if l < r:
        mid = ( l + r ) / 2
        left = arr[l:]
        right = arr[:r]

        merge_sort_in_place(left, l, mid)
        merge_sort_in_place(right, mid, r)
    

    return merge_in_place(arr, l, mid, r)
     
    



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr





#### This code works for merge_sort, but it uses only one funciton
    # result = []
    # if( len(arr) <= 1):
    #     return arr
    # half = int(len(arr) / 2)
    # lower = merge_sort(arr[:half])
    # upper = merge_sort(arr[half:])
    # lower_len = len(lower)
    # upper_len = len(upper)
    # i = 0
    # j = 0
    # while i != lower_len or j != upper_len:
    #     # if we haven't reached the end of lower iteration
    #     # and either are true:
    #     # upper is done iterating 
    #     # or lower[i] is smaller than upper[i] (j for code)
    #     if( i != lower_len and (j == upper_len or lower[i] < upper[j] )):
    #         # append the lower number
    #         result.append(lower[i])
    #         i += 1
    #     else:
    #         # append the upper number
    #         result.append(upper[j])
    #         j += 1
    # return result