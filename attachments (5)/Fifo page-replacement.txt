def fifo_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1

        print(f"Memory: {memory}")

    return page_faults


pages = [0, 2, 1, 6, 4, 0, 1, 0, 3, 1, 2, 1]
capacity = 3
faults = fifo_page_replacement(pages, capacity)
print(f"Total Page Faults: {faults}")


