def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
print("Unsorted array:", arr)

sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)








'''
Let's walk through the example using the same unsorted array: [38, 27, 43, 3, 9, 82, 10].
Step 1: Initial Call to quick_sort

We start with the initial call to the quick_sort function with the unsorted array.

python

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)

Step 2: Initial Call to quick_sort Function

The quick_sort function is called with the unsorted array [38, 27, 43, 3, 9, 82, 10].
Step 3: Select Pivot and Partition the Array

The pivot is selected as the middle element, which is 9.

The array is partitioned into three subarrays:

    left: [3]
    middle: [9]
    right: [38, 27, 43, 82, 10]

Step 4: Recursive Calls

The quick_sort function is recursively called on the left and right subarrays.
Recursive Call 1: [3]

Since the subarray has only one element, it is returned as is.
Recursive Call 2: [38, 27, 43, 82, 10]

The quick_sort function is called recursively with the subarray [38, 27, 43, 82, 10].
Step 5: Select Pivot and Partition the Array

The pivot is selected as the middle element, which is 43.

The array is partitioned into three subarrays:

    left: [27, 10]
    middle: [43]
    right: [38, 82]

Step 6: Recursive Calls
Recursive Call 3: [27, 10]

The quick_sort function is called recursively with the subarray [27, 10].
Recursive Call 4: [38, 82]

The quick_sort function is called recursively with the subarray [38, 82].
Step 7: Merge Sorted Subarrays

After all recursive calls are made, the sorted subarrays are concatenated to form the final sorted array:

css

[3] + [9] + [27, 10] + [38] + [43] + [82]

Final Sorted Array

The final sorted array is [3, 9, 10, 27, 38, 43, 82].

This is how the quicksort algorithm sorts the given array using the provided code. Let me know if you need further explanation!

'''