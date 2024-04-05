class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        return self.valid_tic_tac_toe(board)

    def valid_tic_tac_toe(self, board: list[str]) -> bool:
        # Checking winning count of X and O: Win(O) and Win(X)
        # Counts of X and O: count(X), count(O)
        # If Win(X) >= 2 or Win(O)>= 2, return False
        # If Win(X) == 1 and Win(O) == 1, return False
        # If WIN(X) == 1 and WIN(O) == 0, check count(X) = count(O) + 1
        # If WIN(X) == 0 and WIN(O) == 1, check count(X) = count(O)
        # If WIN(X) == 0 and WIN(O) == 0, check count(X) = count(O) or count(O) + 1
        pass
