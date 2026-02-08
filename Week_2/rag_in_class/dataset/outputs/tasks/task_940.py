def heap_sort(arr):
    """Sorts the input array in-place using heap sort algorithm.

    Args:
        arr: List of elements to be sorted.

    Returns:
        The sorted list (same as input list after in-place sorting).
    """
    heapify(arr)
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        shift_down(arr, 0, end - 1)
        end -= 1
    return arr

def heapify(arr):
    """Converts the input array into a max-heap in-place.

    Args:
        arr: List to be converted into a max-heap.
    """
    start = len(arr) // 2
    while start >= 0:
        shift_down(arr, start, len(arr) - 1)
        start -= 1

def shift_down(arr, start, end):
    """Shifts down the element at 'start' index to maintain heap property.

    Args:
        arr: The heap array.
        start: Index of the element to shift down.
        end: Last valid index in the heap.
    """
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        # Compare with right child if it exists and is larger
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        # Swap if root is smaller than the larger child
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return
