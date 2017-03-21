import threading
import queue
import time


class Job(object):

    def __init__(self, name: str):
        self.name = name


class SimulatedDevice(threading.Thread):

    def __init__(self):
        super(SimulatedDevice, self).__init__()
        self.run_flag = True
        self.message_queue = queue.Queue()
        self.task_thread = None
        self.task_lock = threading.Lock()

    def stop_task_on_thread(self):
        if self.task_thread:
            with self.task_lock:
                if self.task_thread:
                    print("Stop task on thread ..")
                    self.run_flag = False
                    if self.task_thread.is_alive():
                        self.task_thread.join()
                    self.run_flag = True

    def launch_task_on_thread(self, task):
        self.stop_task_on_thread()
        self.task_thread = threading.Thread(target=task)
        self.task_thread.start()

    def task_move(self):
        print("Start move ..")
        i = 0
        while i < 10 and self.run_flag:
            i += 1
            print(".. iteration %d" % i)
            time.sleep(0.25)
        print("Stop move ..")

    def run(self):
        print("Start SimulatedDevice ..")

        while True:
            if not self.message_queue.empty():
                print("Get job from message queue ..")
                job = self.message_queue.get()
                if job.name == "move":
                    self.launch_task_on_thread(self.task_move)
                elif job.name == "stop":
                    self.stop_task_on_thread()
                self.message_queue.task_done()


if __name__ == "__main__":
    s = SimulatedDevice()
    s.start()
    s.message_queue.put(Job("move"))
    s.message_queue.put(Job("move"))
    time.sleep(0.4)
    s.message_queue.put(Job("stop"))
