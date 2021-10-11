import multiprocessing


def sender(conn, msgs):
    for msg in msgs:
        conn.send(msg)
        print(f'Send message: {msg}')

    conn.close()


def receiver(conn):
    while True:
        msg = conn.recv()
        if msg == 'end':
            break
        print(f'Recieved the message: {msg}')


if __name__ == '__main__':

    msgs = ['hello', 'how are you?', 'im ok', 'end']
    parent_con, child_con = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=sender, args=(parent_con, msgs))
    p2 = multiprocessing.Process(target=receiver, args=(child_con,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()
