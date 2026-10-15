from time import sleep
class A:
    def run(self): # run is a pre-defined function
        for i in range(5):
            print("Ravi")
            sleep(1)

class B:
    def run(self):
        for i in range(5):
            print("Bhushan")
            sleep(1)

t1 = A()
t2 = B()

t1.run()
t2.run()