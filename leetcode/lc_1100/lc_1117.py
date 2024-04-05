from typing import Callable
from threading import Semaphore


class H2O:
    def __init__(self):
        self.hydrogen_count = 0
        self.h = Semaphore(2)
        self.o = Semaphore(0)

    def hydrogen(self, releaseHydrogen: "Callable[[], None]") -> None:
        self.h.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.hydrogen_count += 1
        if self.hydrogen_count == 2:
            self.o.release()
            self.hydrogen_count = 0

    def oxygen(self, releaseOxygen: "Callable[[], None]") -> None:
        self.o.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.h.release()
        self.h.release()
