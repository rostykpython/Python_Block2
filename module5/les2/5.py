import multiprocessing


def print_records(records):
    for record in records:
        print(f'Name {record[0]}, score: {record[1]}\n')


def insert_record(records, record):
    records.append(record)
    print('New record has been added\n')


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        records = manager.list([('mike', 10), ('jack', 8)])
        new_record = ('jeff', 7)

        p1 = multiprocessing.Process(target=insert_record, args=(records, new_record))
        p2 = multiprocessing.Process(target=print_records, args=(records,))

        p1.start()
        p1.join()

        p2.start()
        p2.join()
