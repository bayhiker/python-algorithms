def test_0731() -> None:
    from .lc_0731 import MyCalendarTwo

    my_calendar_two = MyCalendarTwo()
    assert my_calendar_two.book(10, 20) is True
    assert my_calendar_two.book(50, 60) is True
    assert my_calendar_two.book(10, 40) is True
    assert my_calendar_two.book(5, 15) is False
    assert my_calendar_two.book(5, 10) is True
    assert my_calendar_two.book(25, 55) is True
    c = MyCalendarTwo()
    assert c.book(47, 50) is True
    assert c.book(1, 10) is True
    assert c.book(27, 36) is True
    assert c.book(40, 47) is True
    assert c.book(20, 27) is True
    assert c.book(15, 23) is True
    assert c.book(10, 18) is True
    assert c.book(27, 36) is True
    assert c.book(17, 25) is False
    assert c.book(8, 17) is False
    assert c.book(24, 33) is False
    assert c.book(23, 28) is False
    assert c.book(21, 27) is False
    assert c.book(47, 50) is True
    assert c.book(14, 21) is False
    assert c.book(26, 32) is False
    assert c.book(16, 21) is False
    assert c.book(2, 7) is True
    assert c.book(24, 33) is False
    assert c.book(6, 13) is False
    assert c.book(44, 50) is False
    assert c.book(33, 39) is False
    assert c.book(30, 36) is False
    assert c.book(6, 15) is False
    assert c.book(21, 27) is False
    assert c.book(49, 50) is False
    assert c.book(38, 45) is True
    assert c.book(4, 12) is False
    assert c.book(46, 50) is False
    assert c.book(13, 21) is False


def test_0736() -> None:
    from .lc_0736 import Solution

    solution = Solution()
    assert solution.evaluate("(let x 3 x 2 x)") == 2
    assert solution.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))") == 14
    assert solution.evaluate("(let x 1 y 2 x (add x y) (add x y))") == 5
    assert solution.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))") == 6
    assert solution.evaluate("(let a1 3 b2 (add a1 1) b2)") == 4
    assert solution.evaluate("(let x 7 -12)") == -12
    assert solution.evaluate("(let x -2 y x y)") == -2
    assert (
        solution.evaluate("(let a (add 1 2) b (mult a 3) c 4 d (add a b) (mult d d))")
        == 144
    )


def test_0780() -> None:
    from .lc_0780 import Solution

    solution = Solution()
    assert solution.reachingPoints(1, 1, 3, 5) is True
    assert solution.reachingPoints(1, 1, 2, 2) is False
    assert solution.reachingPoints(1, 1, 1, 1) is True
    assert solution.reachingPoints(1, 1, 1000000000, 1)
    assert solution.reachingPoints(9, 5, 12, 8) is False


def test_0789() -> None:
    from .lc_0789 import Solution

    solution = Solution()
    assert solution.escapeGhosts(ghosts=[[1, 0]], target=[2, 0]) is False
    assert solution.escapeGhosts(ghosts=[[1, 0], [0, 3]], target=[0, 1]) is True
    assert solution.escapeGhosts(ghosts=[[2, 0]], target=[1, 0]) is False
