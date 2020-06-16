# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [None] * elements

    # Your code here
    while None in merged_arr:
        if not arrA:
            popped = arrB.pop(0)
            first_instance = merged_arr.index(None)
            merged_arr[first_instance] = popped
        elif not arrB:
            popped = arrA.pop(0)
            first_instance = merged_arr.index(None)
            merged_arr[first_instance] = popped
        elif arrA[0] < arrB[0]:
            popped = arrA.pop(0)
            first_instance = merged_arr.index(None)
            merged_arr[first_instance] = popped
        elif arrB[0] < arrA[0]:
            popped = arrB.pop(0)
            first_instance = merged_arr.index(None)
            merged_arr[first_instance] = popped
        else:
            continue

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # base case
    if len(arr) == 0 or len(arr) == 1:
        return arr 
    # recursive case
    elif len(arr) == 2:
        return merge([arr[0]], [arr[1]])
    else:    
        middle = (len(arr) - 1) // 2
        left = arr[:middle]
        right = arr[middle:]
        
        return merge(merge_sort(left), merge_sort(right))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
