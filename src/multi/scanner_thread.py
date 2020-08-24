import threading


def split_processing(ports, num_splits, scan, range_low, range_high):
    split_size = (range_high-range_low) // num_splits
    threads = []
    for i in range(num_splits):
        # determine the indices of the list this thread will handle
        start = i * split_size
        # special case on the last chunk to account for uneven splits
        end = range_high if i+1 == num_splits else (i+1) * split_size
        # create the thread
        threads.append(
            threading.Thread(target=scan, args=(ports, start, end)))
        threads[-1].start()  # start the thread we just created

    # wait for all threads to finish
    for t in threads:
        t.join()