import multiprocessing

num = -1


def producer(data, queue):

    print("getting data and puting it to the queue")
    for item in data:
        queue.put(item)


def consumer(queue, number):
    # while True:
    #     data = queue.get()
    #     print(f'Data found: {data}')
    #     if data is num:
    #         break
    #     processed = data**2
    #     print(processed)
    for i in range(number):
        data = queue.get()
        print(f'Data found: {data}')
        processed = data ** 2
        print(processed)


if __name__ == '__main__':
    q = multiprocessing.Queue()
    data = [5, 10, 13, -1]

    p1 = multiprocessing.Process(target=producer, args=(data, q))
    p2 = multiprocessing.Process(target=consumer, args=(q, len(data)))
    p3 = multiprocessing.Process(target=consumer, args=(q, len(data)))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Ended")
