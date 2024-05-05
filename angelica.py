class NPuzzle:
    def __init__(self):
        self.size = 0
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.blank = (0, 0)
        self.goal = [['','',''], ['','',''], ['','','']]

    def __init__(self, puzzle, puzzle_size):
        self.puzzle = puzzle
        self.size = puzzle_size
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.blank = self.find_blank()
        self.goal = [['A','N','G'], ['E','L','I'], ['C','A','.']]

    def __init__(self, p1):
        self.puzzle = p1.puzzle
        self.size = p1.size
        self.g = p1.g
        self.h = p1.h
        self.f = p1.f
        self.blank = p1.blank
        self.goal = p1.goal

    def go_right(self, choice):
        i, j = self.blank
        self.puzzle[i][j], self.puzzle[i][j + 1] = self.puzzle[i][j + 1], self.puzzle[i][j]
        self.blank = (i, j + 1)
        self.g += 1

        if choice == 2:
            self.h = self.find_misplaced()
        elif choice == 3:
            self.h = self.manhattan_distance()

        self.f = self.g + self.h

    def go_left(self, choice):
        i, j = self.blank
        self.puzzle[i][j], self.puzzle[i][j - 1] = self.puzzle[i][j - 1], self.puzzle[i][j]
        self.blank = (i, j - 1)
        self.g += 1

        if choice == 2:
            self.h = self.find_misplaced()
        elif choice == 3:
            self.h = self.manhattan_distance()

        self.f = self.g + self.h

    def go_up(self, choice):
        i, j = self.blank
        self.puzzle[i][j], self.puzzle[i - 1][j] = self.puzzle[i - 1][j], self.puzzle[i][j]
        self.blank = (i - 1, j)
        self.g += 1

        if choice == 2:
            self.h = self.find_misplaced()
        elif choice == 3:
            self.h = self.manhattan_distance()

        self.f = self.g + self.h

    def go_down(self, choice):
        i, j = self.blank
        self.puzzle[i][j], self.puzzle[i + 1][j] = self.puzzle[i + 1][j], self.puzzle[i][j]
        self.blank = (i + 1, j)
        self.g += 1

        if choice == 2:
            self.h = self.find_misplaced()
        elif choice == 3:
            self.h = self.manhattan_distance()

        self.f = self.g + self.h

    def check_right(self):
        i, j = self.blank
        return j != self.size - 1

    def check_left(self):
        i, j = self.blank
        return j != 0

    def check_up(self):
        i, j = self.blank
        return i != 0
    
    def check_down(self):
        i, j = self.blank
        return i != self.size - 1

    