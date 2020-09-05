class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start_positions = []
        for i, row, in enumerate(board):
            for j, letter in enumerate(row):
                if letter == word[0]:
                    start_positions.append((i, j))

        m, n = len(board), len(board[0])

        def can_make_word(word, used, position):
            if not word:
                return True
            used.append(position)
            i, j = position
            possible_next = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            next_positions = [(i, j) for i, j in possible_next
                              if 0 <= i < m and 0 <= j < n
                              and (i, j) not in used
                              and board[i][j] == word[0]]
            if not next_positions:
                return False
            return any(can_make_word(word[1:], list(used), position)
                       for position in next_positions)

        return any(can_make_word(word[1:], [], position) for position in start_positions)
