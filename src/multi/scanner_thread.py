import threading


def split_processing(ports, num_splits, scan, range_low, range_high):
    split_size = (range_high-range_low) // num_splits
    threads = []
    start  = 0
    before = split_size * num_splits
    for end in range(split_size, before, split_size):
        # determine the indices of the list this thread will handle
        # We can just use this for loop
#         start = i * split_size
        # special case on the last chunk to account for uneven splits
    # No point of comparing each time if looking for end
    # We can create end
#         end = range_high if i+1 == num_splits else (i+1) * split_size
        # create the thread
        threads.append(
            threading.Thread(target=scan, args=(ports, start, end)))
        start = end
        threads[-1].start()  # start the thread we just created
    # The range - end will be helpful for remaining
    threads.append(
        threading.Thread(target=scan, args=(ports, end, range_end)))
    threads[-1].start()

    # wait for all threads to finish
    for t in threads:
        t.join()
