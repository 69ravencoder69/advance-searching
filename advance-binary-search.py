# Enhanced Binary Search (Iterative & Recursive)
def binary_search(arr, target, find_first=True):
   
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
