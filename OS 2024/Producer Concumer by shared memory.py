buffer = []
buffer_size = 5

def producer():
    for i in range(buffer_size):
        if len(buffer) == 0:
            print("Buffer is empty")
        while len(buffer) == buffer_size:
            print("Buffer is full, waiting to consume...")
            return
        item = input(f"Enter item {i+1}: ")
        buffer.append(item)
        print(f"Produced: {item}")
    if len(buffer) == buffer_size:
        print("Buffer is full")
        print("Current buffer:", buffer)

def consumer():
    print("Buffer before consuming:", buffer)
    while len(buffer) > 0:
        item = buffer.pop(0)
        print(f"Consumed: {item}")
    if len(buffer) == 0:
        print("Buffer is empty")

if __name__ == "__main__":
    producer()
    consumer()
