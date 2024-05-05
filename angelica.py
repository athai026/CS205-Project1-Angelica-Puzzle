from queue import PriorityQueue
import copy
import time

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

    def __lt__(self, rhs):
        return self.f < rhs.f

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

    def expand(self, pq, choice):
        curr = pq.get()[1]

        if curr.check_right():
            right = copy.deepcopy(curr)
            right.move_right(choice)
            pq.put((right.f, right))
            # print(f'f: {right.f}, g: {right.g}, h: {right.h}')
            # right.print_puzzle()
            # print('added right')

        if curr.check_left():
            left = copy.deepcopy(curr)
            left.move_left(choice)
            pq.put((left.f, left))
            # print(f'f: {left.f}, g: {left.g}, h: {left.h}')
            # left.print_puzzle()
            # print('added left')

        if curr.check_up():
            up = copy.deepcopy(curr)
            up.move_up(choice)
            pq.put((up.f, up))
            # print(f'f: {up.f}, g: {up.g}, h: {up.h}')
            # up.print_puzzle()
            # print('added up')

        if curr.check_down():
            down = copy.deepcopy(curr)
            down.move_down(choice)
            pq.put((down.f, down))
            # print(f'f: {down.f}, g: {down.g}, h: {down.h}')
            # down.print_puzzle()
            # print('added down')

    def misplaced(self):
        numMisplaced = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] != '.':
                    if self.puzzle[i][j] != self.goal[i][j]:
                        numMisplaced += 1

        return numMisplaced
    
    def manhattan(self):
        heuristic = 0

        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] != '.':
                    if self.puzzle[i][j] != self.goal[i][j]:
                        if self.puzzle[i][j] == 'A':
                            A1 = (0,0)
                            A2 = (2,1)
                            A1dist = abs(i - A1[0]) + abs(j - A1[1])
                            A2dist = abs(i - A2[0]) + abs(j - A2[1])
                            heuristic += min(A1dist, A2dist)
                        else:
                            goal_position = self.find_goal(self.puzzle[i][j])
                            heuristic += abs(i - goal_position[0]) + abs(j - goal_position[1])

        return heuristic
    
    def find_goal(self, letter):
        if letter == 'N':
            return (0,1)
        if letter == 'G':
            return (0,2)
        if letter == 'E':
            return (1,0)
        if letter == 'L':
            return (1,1)
        if letter == 'I':
            return (1,2)
        if letter == 'C':
            return (2,0)
        
    def search(self, pq, choice, visited):
        maxQueueSize = 1

        while not pq.empty():
            curr = pq.queue[0][1]
            print(f'The best state to expand with g(n) = {curr.g} and h(n) = {curr.h} is:')
            curr.print_puzzle()

            found = False
            if curr.puzzle != curr.goal:
                curr.expand(pq, choice)
                
                for i in range(len(visited)):
                    if curr.puzzle == visited[i]:
                        if curr.f < visited[i].f:
                            curr, visited[i] = visited[i], curr
                        found = True
                        break
                
                if not found:
                    visited.append(curr)

                if pq.qsize() > maxQueueSize:
                    print(pq.qsize())
                    maxQueueSize = pq.qsize()
                    print(maxQueueSize)

            else:
                print('You\'ve reached your goal!')
                curr.print_puzzle()
                print(f'Depth of solution: {curr.g}')
                break

        return maxQueueSize

def main():

    puzzleTemp = []
    for i in range(3):
        puzzle_row = input(f'Input characters for row {i+1} separated by spaces: ')
        puzzle_row = puzzle_row.split(' ')
        puzzleTemp.append(puzzle_row)

    print('1. Uniform Cost Search')
    print('2. A* with Misplaced Tile Heuristic')
    print('3. A* with Manhattan Distance Heuristic')
    choice = int(input('Which search algorithm would you like to use? (input number choice): '))

    start = time.perf_counter()

    puzzle = Angelica(puzzleTemp)
    if choice == 2:
        puzzle.h = puzzle.misplaced()
        puzzle.f = puzzle.g + puzzle.h
    elif choice == 3:
        puzzle.h = puzzle.manhattan()
        puzzle.f = puzzle.g + puzzle.h

    pq = PriorityQueue()
    pq.put((puzzle.f, puzzle))
    visited = []
    maxQueueSize = puzzle.search(pq, choice, visited)

    end = time.perf_counter()
    
    print(f'Elapsed time: {end - start :0.5f} seconds')
    print(f'Maximum queue size: {maxQueueSize}')
    print(f'Number of nodes expanded {len(visited)}')



if __name__ == '__main__':
    main()