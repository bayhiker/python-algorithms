def fib_recursion(n):
    if n < 0:
        raise ValueError(f"n must be non-negative, found {n}")
    return n if n < 2 else fib_recursion(n-1) + fib_recursion(n-2)

def fib_dp_bottom_up(n):
    if n < 0:
        raise ValueError(f"n must be non-negative, found {n}")
    if n < 2:
        return n
    fib = 1
    prev = 0
    for counter in range(2, n):
        fib = fib + prev
        prev = fib - prev
    return fib+prev

def fib_dp_top_down(n):
    if n < 0:
        raise ValueError(f"n must be non-negative, found {n}")
    fib = {0:0, 1:1}
    def get_fib(k):
        if k in fib:
            return fib[k]
        fib[k] = get_fib(k-1) + get_fib(k-2)
        return fib[k]
    return get_fib(n)
    

class FibDpTopDown:
    
    def __init__(self) -> None:
        self.fib = {0: 0, 1: 1}

    def get_fib(self, n):
        if n < 0:
            raise ValueError(f"n must be non-negative, found {n}")
        if n in self.fib:
            return self.fib[n]
        else:
            self.fib[n] = self.get_fib(n-1) + self.get_fib(n-2)
            return self.fib[n]
    
    