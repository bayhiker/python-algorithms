class Solution:
    def numberToWords(self, num: int) -> str:
        """Convert a non-negative integer num to its English words representation.

        Args:
            num (int): 0 <= num <= 2**31 - 1

        Returns:
            str: English word representation of num
        """
        return self.number_to_words(num)

    def number_to_words(self, num: int) -> str:
        # Dictionaries:
        # - digits: 0-9
        # - teens: 10-19
        # - tens: 20-30-...-90
        # Return
        # - 0-9 lookup digits, 10-19: lookup teens
        # - 20-99: tens + digits (except 0).
        # - 1xx-9xx: hundreds + two digits above, Note that AND not needed based on the samples
        # - 1xxx-9xxx: thousands + 3 digits above
        # - 1,xxx,xxx - 9,xxx,xxx: x million xxx thousands xxx
        # - 1,xxx,xxx,xxx - 9,xxx,xxx,xxx: x billion xxx million xxx thousands xxx
        pass
