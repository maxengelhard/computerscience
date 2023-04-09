# Merge sort recursively divides the list into two repeatedly and then merges the smaller lists back into a larger one in the correct order.
import sys

def merge_sort():
    with open(sys.argv[1]) as f:
        lines = [int(x.rstrip("\n")) for x in f.readlines()]

    result = msort(lines)
    print(result)
    return result

def msort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) //2
    # want to do it to the right half and left half recursivley
    left_arr = msort(arr[:mid])
    right_arr = msort(arr[mid:])
    result = []
    i = 0
    j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i+=1
        else:
            result.append(right_arr[j])
            j+=1

    result += left_arr[i:]
    result += right_arr[j:]
    return result


if __name__ == "__main__":
    merge_sort()