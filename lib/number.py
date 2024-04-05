# https://en.wikiversity.org/wiki/Python/Prime_factorization
def factorize(n: int) -> dict[int, int]:
    """Get prime factorization of an integer

    Args:
        n (int): The positive number to factorize

    Returns:
        dict[int, int]: Keys are prime factors, values are their corresponding powers.
        None if n is 1 or less.
    """
    prime_factors: dict[int, int] = {}
    if n < 2:
        return None
    factor: int = 2
    while factor ** 2 <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
            prime_factors[factor] = prime_factors.get(factor, 0) + 1
    if n > 1:
        prime_factors[n] = prime_factors.get(n, 0) + 1
    return prime_factors

