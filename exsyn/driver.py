import multiprocessing as mp
from para_gnurad import receive_cmds


parent_conn, child_conn = mp.Pipe()
p = mp.Process(target=lambda: receive_cmds(child_conn))
p.start()

parent_conn.send_bytes(b"foo")
if parent_conn.poll(0.5):
    rc = parent_conn.recv_bytes()
    print("Parent: heard back", rc)
    parent_conn.send_bytes(b"quit")
    if parent_conn.poll(0.5):
        rc = parent_conn.recv_bytes()
        print("Parent heard back", rc)
    else:
        print("no response 2")
else:
    print("no response 1")