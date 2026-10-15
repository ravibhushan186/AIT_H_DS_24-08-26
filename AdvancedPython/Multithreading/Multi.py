from threading import Thread
from time import sleep

class A(Thread):
    def run(self):
        for i in range(5):
            print("Ravi")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("Bhushan")
            sleep(1)

t1 = A()
t2 = B()

t1.start()
t2.start()