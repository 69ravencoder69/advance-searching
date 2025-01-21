import multiprocessing

# Enhanced Linear Search
def linear_search(arr, target):
    """
    Searches for all occurrences of `target` in `arr`.
    Uses parallel processing if the array is large.
    """
    indices = []
    
    def search_segment(segment, start_index):
        """Helper function to search a segment in parallel."""
        return [start_index + i for i, value in enumerate(segment) if value == target]
    
    if len(arr) > 10000:  # Use multiprocessing for large datasets
        num_processes = multiprocessing.cpu_count()
        chunk_size = len(arr) // num_processes
        chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
        
        with multiprocessing.Pool(num_processes) as pool:
            results = pool.starmap(search_segment, [(chunk, i * chunk_size) for i, chunk in enumerate(chunks)])
        
        for result in results:
            indices.extend(result)
    else:
        indices = [i for i, value in enumerate(arr) if value == target]
    
    return indices if indices else -1


# Enhanced Binary Search (Iterative & Recursive)
def binary_search(arr, target, find_first=True):
    """
    Searches for `target` in a sorted list `arr`.
    Returns all occurrences of `target`.
    Uses Jump Search to quickly verify if `target` is within range.
    """
    left, right = 0, len(arr) - 1
    indices = []

    # Jump Search Pre-check (Enhancement)
    if arr[left] > target or arr[right] < target:
        return -1  # Target is out of range

    # Iterative Binary Search
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            indices.append(mid)
            # Search for duplicates on both sides
            l, r = mid - 1, mid + 1
            while l >= left and arr[l] == target:
                indices.append(l)
                l -= 1
            while r <= right and arr[r] == target:
                indices.append(r)
                r += 1
            return sorted(indices)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# Example Usage
if __name__ == "__main__":
    unsorted_list = [5, 3, 8, 2, 5, 10, 5, 1]
    sorted_list = [1, 2, 3, 5, 5, 5, 8, 10]

    target = 5

    print("Linear Search Results (Unsorted List):", linear_search(unsorted_list, target))
    print("Binary Search Results (Sorted List):", binary_search(sorted_list, target))
