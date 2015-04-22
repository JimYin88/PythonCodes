def merge_sort(seq):
    """Accepts a mutable sequence. Utilizes merge_sort to sort in place, return
    a sorted sequence"""
    if len(seq) == 1:
        return seq
    else:
        #recursion: break sequence down into chunks of 1
        mid = len(seq)/2
        left = merge_sort(seq[:mid])
        right = merge_sort(seq[mid:])

        i, j, k = 0, 0, 0 #i= left counter, j= right counter, k= master counter

        #run until left or right is out
        while i < len(left) and j < len(right):
            #if current left val is < current right val; assign to master list
            if left[i] < right[j]:
                seq[k] = left[i]
                i += 1; k += 1
            #else assign right to master
            else:
                seq[k] = right[j]
                j += 1; k += 1

        #handle remaining items in remaining list
        remaining = left if i < j else right
        r = i if remaining == left else j

        while r < len(remaining):
            seq[k] = remaining[r]
            r += 1; k += 1

        return seq
        
        
from heapq import merge

def merge_sort2(m):
    if len(m) <= 1:
        return m

    middle = len(m) / 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort2(left)
    right = merge_sort2(right)
    return list(merge(left, right))
