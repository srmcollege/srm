import threading
import time
resource = 0
readers = 0
read_lock = threading.Semaphore(1)  
write_lock = threading.Semaphore(1)  

def reader():
    global readers
    read_lock.acquire()
    readers += 1
    if readers == 1:
        write_lock.acquire()  
    read_lock.release()
    
    print(f"{threading.current_thread().name} is reading resource: {resource} \n")
    time.sleep(3)

    read_lock.acquire()
    readers -= 1
    if readers == 0:
        write_lock.release()
    read_lock.release()

def writer():
    global resource
    write_lock.acquire()
    resource += 1
    print(threading.current_thread().name,"is writing resource: ",resource)
    time.sleep(3)
    write_lock.release()

def main():
    threads = []    

    for i in range(5):
        t = threading.Thread(target=reader, name=f"Reader-{i}")
        threads.append(t)
        t.start()

    for i in range(5):
        t = threading.Thread(target=writer, name=f"Writer-{i}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
