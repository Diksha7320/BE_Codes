import random

def simple_partition(arr, low, high):
    pivot = arr[low]  # Choosing the first element as the pivot
    i = low + 1  # Pointer for the greater element
    comparisons = 0

    for j in range(low + 1, high + 1):
        comparisons += 1
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than the pivot
            i += 1

    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Place pivot in correct position
    return i - 1, comparisons

def simple_deterministic_quicksort(arr, low, high):
    comparisons = 0
    if low < high:
        pi, part_comps = simple_partition(arr, low, high)
        comparisons += part_comps

        comparisons += simple_deterministic_quicksort(arr, low, pi - 1)
        comparisons += simple_deterministic_quicksort(arr, pi + 1, high)

    return comparisons

def simple_randomized_partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[low], arr[rand_pivot] = arr[rand_pivot], arr[low]  # Swap random pivot with the first element
    return simple_partition(arr, low, high)

def simple_randomized_quicksort(arr, low, high):
    comparisons = 0
    if low < high:
        pi, part_comps = simple_randomized_partition(arr, low, high)
        comparisons += part_comps

        comparisons += simple_randomized_quicksort(arr, low, pi - 1)
        comparisons += simple_randomized_quicksort(arr, pi + 1, high)

    return comparisons

def main():
    # Manual input of array elements
    arr = list(map(int, input("Enter the elements of the array, separated by spaces: ").split()))
    print("Original Array:", arr)

    arr_copy = arr.copy()
    det_comparisons = simple_deterministic_quicksort(arr_copy, 0, len(arr_copy) - 1)
    print("Deterministic Quick Sort - Comparisons:", det_comparisons)
    print("Sorted Array:", arr_copy)

    arr_copy = arr.copy()
    rand_comparisons = simple_randomized_quicksort(arr_copy, 0, len(arr_copy) - 1)
    print("Randomized Quick Sort - Comparisons:", rand_comparisons)
    print("Sorted Array:", arr_copy)

if __name__ == "__main__":
    main()
