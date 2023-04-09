# Selection sort iterates through the unsorted portions of a list, selecting the smallest element each time and moving it to its correct location.
import sys

def selection_sort():
    with open(sys.argv[1]) as f:
        lines = [int(x.rstrip("\n")) for x in f.readlines()]
        

    ## iterate through all indexes
    for i in range(len(lines)):
        # select a number to account for
        min_idx = i

        ## iterate through the rest for that index +1
        for j in range(i+1,len(lines)):
            if lines[j] < lines[min_idx]:
                min_idx = j

        # we got the min idx now swap them
        lines[i] , lines[min_idx] = lines[min_idx] , lines[i]


    print(lines)
        
        




if __name__ == "__main__":
    selection_sort()
