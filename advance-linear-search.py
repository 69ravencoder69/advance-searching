# Enhanced Linear Search
def linear_search(arr, target):

    indices = []
    
    def search_segment(segment, start_index):
        
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