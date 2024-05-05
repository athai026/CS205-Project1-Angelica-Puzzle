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

    