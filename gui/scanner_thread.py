import threading

threads = []

def split_processing(ports, num_splits, scan, range_low, range_high):
    split_size = (range_high-range_low) // num_splits
    
    start = range_low
    end = start + split_size
    for i in range(num_splits):
        
        if (i==num_splits-1):
            end = range_high
        
        threads.append(
            threading.Thread(target=scan, args=(ports, start, end)))
        threads[-1].start()  # start the thread we just 
        start += split_size
        end += split_size

    # wait for all threads to finish
    for t in threads:
        t.join()