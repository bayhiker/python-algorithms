class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        return self.decode_cipher_text_directly_assign(encodedText, rows)

    def decode_cipher_text_directly_assign(self, encoded_text: str, rows: int) -> str:
        cols = len(encoded_text) // rows
        input: list[str] = []
        for i in range(cols):
            for j in range(i, len(encoded_text), cols + 1):
                input.append(encoded_text[j])
        while input and input[-1] == " ":
            input.pop()
        return "".join(input)

    def decode_cipher_text_count_input(self, encoded_text: str, rows: int) -> str:
        n = len(encoded_text)
        if n == 0:
            return ""
        if n % rows > 0:
            raise ValueError("Length of encoded_text is not multiple of rows")
        cols = n // rows  # Number of characters per row
        input_length = 0
        if cols < rows:
            # Only (i, i) in original matrix is valid characters
            input_length = cols
        else:
            # Calculate upper right corner empty spaces
            for i in range(rows - 1, -1, -1):
                if encoded_text[cols * i + cols - 1] == " ":
                    break
            upper_right_spaces = i * (i + 1) // 2
            for j in range(i + 1):
                if encoded_text[cols * (i - j) + cols - 1 - j] == " ":
                    upper_right_spaces += 1
            # There are (rows-1)**2 empty spaces added on lower left corner
            lower_left_spaces = rows * (rows - 1) // 2
            input_length = n - lower_left_spaces - upper_right_spaces
        input = ""
        for x in range(input_length):
            input += encoded_text[cols * (x % rows) + (x // rows + x % rows)]

        return input
