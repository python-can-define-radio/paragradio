from multiprocessing.connection import Connection
import time

from typeguard import typechecked


class Pretend_Spec_An:
    def do_thing_1(self, sec: float):
        time.sleep(sec)


@typechecked
def receive_cmds(child_conn: Connection):
    while True:
        rc = child_conn.recv_bytes()
        if rc == b"quit":
            child_conn.close()
            break
        else:
            print("Child: received", rc)
            child_conn.send_bytes(b"ack")