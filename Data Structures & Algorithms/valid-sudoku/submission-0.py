from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        board_sets = defaultdict(set)

        i, j = 0, 0

        while i < 9:
            j = 0

            while j < 9:
                current = board[i][j]

                if "." != current:
                    # check against row
                    if current in board_sets[("r", i)]:
                        print(board_sets)
                        return False

                    else:
                        board_sets[("r", i)].add(current)

                    # check against col
                    if current in board_sets[("c", j)]:
                        print(board_sets)
                        return False

                    else:
                        board_sets[("c", j)].add(current)

                    # check against box
                    if current in board_sets[("b", i // 3, j // 3)]:
                        print(board_sets)
                        return False

                    else:
                        board_sets[("b", i // 3, j // 3)].add(current)

                j += 1
            i += 1

        return True
