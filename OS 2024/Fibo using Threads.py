import threading

def fibonacci(n, result_list, index):
    if n == 0:
        result_list[index] = 0
    elif n == 1:
        result_list[index] = 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        result_list[index] = b

def main():
    n = int(input("Enter the number of terms in the Fibonacci series: "))
    result_list = [0] * n
    threads = []
    for i in range(n):
        thread = threading.Thread(target=fibonacci, args=(i, result_list, i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("Fibonacci sequence:")
    print(result_list)

if __name__ == "__main__":
    main()
