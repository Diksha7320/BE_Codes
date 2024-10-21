import random
import time

# Function to partition the array for deterministic quicksort
def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    comparisons, swaps = 0, 0
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1
    return i + 1, comparisons, swaps

# Deterministic QuickSort
def deterministic_quicksort(arr, low, high):
    comparisons, swaps = 0, 0
    if low < high:
        pi, part_comps, part_swaps = deterministic_partition(arr, low, high)
        comparisons += part_comps
        swaps += part_swaps
        left_comps, left_swaps = deterministic_quicksort(arr, low, pi - 1)
        right_comps, right_swaps = deterministic_quicksort(arr, pi + 1, high)
        comparisons += left_comps + right_comps
        swaps += left_swaps + right_swaps
    return comparisons, swaps

# Function to partition the array for randomized quicksort
def randomized_partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]
    return deterministic_partition(arr, low, high)

# Randomized QuickSort
def randomized_quicksort(arr, low, high):
    comparisons, swaps = 0, 0
    if low < high:
        pi, part_comps, part_swaps = randomized_partition(arr, low, high)
        comparisons += part_comps
        swaps += part_swaps
        left_comps, left_swaps = randomized_quicksort(arr, low, pi - 1)
        right_comps, right_swaps = randomized_quicksort(arr, pi + 1, high)
        comparisons += left_comps + right_comps
        swaps += left_swaps + right_swaps
    return comparisons, swaps

# Helper function to time and analyze the sorting algorithms
def analyze_sort(arr, sort_func, name):
    start_time = time.time()
    comparisons, swaps = sort_func(arr, 0, len(arr) - 1)
    end_time = time.time()
    
    print(f"\n{name}:")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print("Sorted Array:")
    print(arr)

# Main function to run the analysis
def main():
    arr_size = 10
    arr = [random.randint(1, 100) for _ in range(arr_size)]

    print("Original Array:")
    print(arr)

    # Deterministic Quick Sort
    arr_copy = arr.copy()
    analyze_sort(arr_copy, deterministic_quicksort, "Deterministic Quick Sort")

    # Randomized Quick Sort
    arr_copy = arr.copy()
    analyze_sort(arr_copy, randomized_quicksort, "Randomized Quick Sort")

if __name__ == "__main__":
    main()
