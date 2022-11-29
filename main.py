# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")

def cmp(a,b):
    if a > b:
        return -1
    elif a == b
        return 0
    else
        return 1

def merge(arr, left, right, middle):
    x = middle - left + 1
    y = right - middle
    leftarr = [0] * (x)
    rightarr = [0] * (y)
 
    for i in range(0, x):
        leftarr[i] = arr[left + i]
 
    for j in range(0, y):
        rightarr[j] = arr[middle + 1 + j]
 
    i = 0 
    j = 0 
    k = left 
 
    while i < x and j < y:
        if leftarr[i] <= rightarr[j]:
            arr[k] = leftarr[i]
            i += 1
        else:
            arr[k] = rightarr[j]
            j += 1
        k += 1
 
    while i < x:
        arr[k] = leftarr[i]
        i += 1
        k += 1
 
    while j < y:
        arr[k] = R[j]
        j += 1
        k += 1
 
 
def merge_sort(arr,cmp(arr[0],arr[len(arr)-1])):
    left = 0
    right = len(arr)-1
    
    if left < right:

        middle = left + (right-l)//2
 
        mergeSort(arr, left, middle)
        mergeSort(arr, middle + 1, right)
        merge(arr, left, middle, right)
    pass

# must be in-place sort
def quick_sort(arr,cmp):
    pass
