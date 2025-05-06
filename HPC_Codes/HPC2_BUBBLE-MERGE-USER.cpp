#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <omp.h>

using namespace std;
using namespace std::chrono;

// Function to generate a random array (for user input case, remove the random generation part)
void generateArray(vector<int>& arr, int size) {
    for (int i = 0; i < size; i++) {
        cin >> arr[i]; // User input instead of random generation
    }
}

// Sequential Bubble Sort
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Parallel Bubble Sort using OpenMP
void parallelBubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        #pragma omp parallel for
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Merge function for Merge Sort
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int i = 0; i < n2; i++) R[i] = arr[mid + 1 + i];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }

    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

// Sequential Merge Sort
void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// Parallel Merge Sort using OpenMP
void parallelMergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        #pragma omp parallel sections
        {
            #pragma omp section
            parallelMergeSort(arr, left, mid);

            #pragma omp section
            parallelMergeSort(arr, mid + 1, right);
        }
        
        merge(arr, left, mid, right);
    }
}

// Function to measure execution time in nanoseconds
template <typename Func>
double measureTime(Func func, vector<int>& arr) {
    auto start = high_resolution_clock::now();
    func(arr);
    auto stop = high_resolution_clock::now();
    return duration<double, std::nano>(stop - start).count(); // Measure in nanoseconds
}

int main() {
    int size;
    cout << "Enter the number of elements: ";
    cin >> size;

    vector<int> arr(size);
    cout << "Enter the elements:\n";
    generateArray(arr, size);

    // Bubble Sort Comparison
    vector<int> arrCopy = arr;
    cout << "Sequential Bubble Sort Time: " 
         << measureTime(bubbleSort, arrCopy) << " ns\n";

    arrCopy = arr;
    cout << "Parallel Bubble Sort Time: " 
         << measureTime(parallelBubbleSort, arrCopy) << " ns\n";

    // Merge Sort Comparison
    arrCopy = arr;
    cout << "Sequential Merge Sort Time: " 
         << measureTime([&](vector<int>& a){ mergeSort(a, 0, size - 1); }, arrCopy) 
         << " ns\n";

    arrCopy = arr;
    cout << "Parallel Merge Sort Time: " 
         << measureTime([&](vector<int>& a){ parallelMergeSort(a, 0, size - 1); }, arrCopy) 
         << " ns\n";

    return 0;
}
