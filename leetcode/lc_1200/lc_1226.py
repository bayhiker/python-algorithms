from collections.abc import Callable
from threading import RLock


class DiningPhilosophers:
    def __init__(self) -> None:
        self.forks = [RLock() for i in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: "Callable[[], None]",
        pickRightFork: "Callable[[], None]",
        eat: "Callable[[], None]",
        putLeftFork: "Callable[[], None]",
        putRightFork: "Callable[[], None]",
    ) -> None:
        left_fork = self.forks[philosopher]
        right_fork = self.forks[(philosopher + 1) % 5]
        if philosopher % 2 == 0:
            with left_fork:
                with right_fork:
                    pickLeftFork()
                    pickRightFork()
                    eat()
                    putRightFork()
                    putLeftFork()
        else:
            with right_fork:
                with left_fork:
                    pickRightFork()
                    pickLeftFork()
                    eat()
                    putLeftFork()
                    putFork()
