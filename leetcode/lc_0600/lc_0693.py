class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return self.has_alternating_bits(n)

    def has_alternating_bits(self, n: int) -> bool:
        last_digit = n % 2
        n //= 2
        while n > 0:
            curr_digit = n % 2
            if curr_digit == last_digit:
                return False
            last_digit = curr_digit
            n //= 2
        return True
