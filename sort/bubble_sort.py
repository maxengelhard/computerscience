# Bubble sort compares pairs of adjacent values one at a time and swaps them if they are in the incorrect order. This continues until the list is sorted.
import sys

def bubble_sort():
    with open(sys.argv[1]) as f:
        lines = [int(x.rstrip("\n")) for x in f.readlines()]

    # do it until no more swaps
    for i in range(len(lines)):
        swapped = False
        for j in range(len(lines)-1):
            if lines[j+1] < lines[j]:
                swapped = True
                (lines[j], lines[j+1]) = (lines[j+1], lines[j])
        if not swapped:
            print(lines)
            return lines


if __name__ == "__main__":
    bubble_sort()