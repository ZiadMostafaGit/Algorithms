def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively call merge_sort on each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    # Compare elements from both lists and append the smaller one to the merged list
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # Append the remaining elements from left list
    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx += 1

    # Append the remaining elements from right list
    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx += 1

    return merged

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
print("Unsorted array:", arr)

sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)


'''

Sure! Let's walk through the merge sort algorithm step by step with the provided code:

Consider the unsorted array: [38, 27, 43, 3, 9, 82, 10].
Step 1: Initial Call to merge_sort

We start with the initial call to the merge_sort function with the unsorted array.

python

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)

Step 2: Initial Call to merge_sort Function

The merge_sort function is called with the unsorted array [38, 27, 43, 3, 9, 82, 10].
Step 3: Divide the Array

The array is divided into two halves: [38, 27, 43, 3] and [9, 82, 10].
Step 4: Recursive Calls
Recursive Call 1: [38, 27, 43, 3]

The merge_sort function is called recursively with the array [38, 27, 43, 3].
Divide [38, 27, 43, 3]

The array is divided into two halves: [38, 27] and [43, 3].
Recursive Calls 2 and 3: [38, 27] and [43, 3]

The merge_sort function is recursively called for the subarrays [38, 27] and [43, 3].
Divide [38, 27]

Since the subarray has only two elements, no further division is needed.
Merge [38, 27]

The two elements are sorted and merged into [27, 38].
Divide [43, 3]

The subarray [43, 3] is divided into [43] and [3].
Merge [43, 3]

The two elements are sorted and merged into [3, 43].
Merge [27, 38] and [3, 43]

The sorted subarrays [27, 38] and [3, 43] are merged into [3, 27, 38, 43].
Recursive Call 4: [9, 82, 10]

The merge_sort function is called recursively with the array [9, 82, 10].
Divide [9, 82, 10]

The array is divided into two halves: [9] and [82, 10].
Recursive Call 5: [82, 10]

The merge_sort function is recursively called with the subarray [82, 10].
Divide [82, 10]

The array is divided into [82] and [10].
Merge [82] and [10]

The two elements are sorted and merged into [10, 82].
Merge [9] and [10, 82]

The sorted subarrays [9] and [10, 82] are merged into [9, 10, 82].
Merge [3, 27, 38, 43] and [9, 10, 82]

The sorted subarrays [3, 27, 38, 43] and [9, 10, 82] are merged into the final sorted array [3, 9, 10, 27, 38, 43, 82].
Final Sorted Array

The final sorted array is [3, 9, 10, 27, 38, 43, 82].

This is how the merge sort algorithm sorts the given array using the provided code. Let me know if you need further explanation!







'''