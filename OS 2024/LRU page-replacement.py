def LRU(pages, capacity):
    cache = []
    page_faults = 0

    for page in pages:
        if page in cache:
            cache.remove(page)
            cache.append(page)
        else:
            page_faults += 1
            if len(cache) >= capacity:
                cache.pop(0)
            cache.append(page)

        print(f"Cache: {cache}")
    return page_faults

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4

page_faults = LRU(pages, capacity)
print(f"Total page faults: {page_faults}")

