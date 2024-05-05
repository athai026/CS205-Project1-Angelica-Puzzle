from queue import PriorityQueue

class Angelica:
    def __init__(self):
        self.size = 3
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.blank = (0,0)
        self.goal = [['','',''], ['','',''], ['','','']]

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = 3
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.blank = self.find_blank()
        self.goal = [['A','N','G'], ['E','L','I'], ['C','A','.']]

    def move_right(self, choice):
        i, j = self.blank
        self.puzzle[i][j], self.puzzle[i][j + 1] = self.puzzle[i][j + 1], self.puzzle[i][j]
        self.blank = (i, j + 1)
        self.g += 1

        if choice == 2:
            self.h = self.misplaced()
        elif choice == 3:
            self.h = self.manhattan()

        self.f = self.g + self.h

    def move_left(self, choice):
        i, j = self.blank
        self.puzzle[i][j], self.puzzle[i][j - 1] = self.puzzle[i][j - 1], self.puzzle[i][j]
        self.blank = (i, j - 1)
        self.g += 1

        if choice == 2:
            self.h = self.misplaced()
        elif choice == 3:
            self.h = self.manhattan()

        self.f = self.g + self.h

    def move_up(self, choice):
        i, j = self.blank
        self.puzzle[i][j], self.puzzle[i - 1][j] = self.puzzle[i - 1][j], self.puzzle[i][j]
        self.blank = (i - 1, j)
        self.g += 1

        if choice == 2:
            self.h = self.misplaced()
        elif choice == 3:
            self.h = self.manhattan()

        self.f = self.g + self.h

    def move_down(self, choice):
        i, j = self.blank
        self.puzzle[i][j], self.puzzle[i + 1][j] = self.puzzle[i + 1][j], self.puzzle[i][j]
        self.blank = (i + 1, j)
        self.g += 1

        if choice == 2:
            self.h = self.misplaced()
        elif choice == 3:
            self.h = self.manhattan()

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
    
    def find_blank(self):
        for i in range(3):
            for j in range(self.size):
                if self.puzzle[i][j] == '.':
                    return (i, j)
                
    def print_puzzle(self):
        for i in range(self.size):
            print("[", end="")
            for j in range(self.size):
                print(self.puzzle[i][j], end="")
                if j != self.size - 1:
                    print(",", end="")
            print("]")

    def expand(pq, choice):
        curr = pq.get()

        if curr.check_right():
            right = curr
            right.move_right(choice)
            pq.put((right.f, right))

        if curr.check_left():
            left = curr
            left.move_left(choice)
            pq.put((left.f, left))

        if curr.check_up():
            up = curr
            up.move_up(choice)
            pq.put((up.f, up))

        if curr.check_down():
            down = curr
            left.move_down(choice)
            pq.put((down.f, down))

        

def main():

    puzzleTemp = []
    for i in range(3):
        puzzle_row = input(f'Input characters for row {i+1} separated by spaces: ')
        puzzle_row = puzzle_row.split(' ')
        puzzleTemp.append(puzzle_row)

    print('1. Uniform Cost Search')
    print('2. A* with Misplaced Tile Heuristic')
    print('3. A* with Manhattan Distance Heuristic')
    choice = input('Which search algorithm would you like to use? (input number choice): ')

    puzzle = Angelica(puzzleTemp)
    pq = PriorityQueue()
    pq.put((puzzle.f, puzzle))



if __name__ == '__main__':
    main()