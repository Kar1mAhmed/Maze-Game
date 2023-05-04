import random
# W == left
# E == Right
# S == Down
# N == Up

class MazeSolverDFSV0:
    def __init__(self, maze) -> None:
        self.maze = maze
        self.current_point = (1,1)
        self.path = []
        self.last_action = None
    
    def solve(self, goal):
        self.path = []
        self.path.append((1,1))
        while self.current_point != goal:
            self._move(self.current_point)
        
        return self.path
        
    
    def _move(self, point):
        direction = self._pick_move()
        
        if direction == 'E':
            self.current_point = (point[0], point[1] + 1)
        elif direction == 'W':
            self.current_point = (point[0], point[1] - 1)
        elif direction == 'N':
            self.current_point = (point[0] - 1, point[1])
        elif direction == 'S':
            self.current_point = (point[0] + 1, point[1])
        else:
            print(f"Wrong direction Given {direction}")
            return
        
        self.last_action = direction
        self.path.append(self.current_point)
                
    
    def _pick_move(self):
        available_moves = []
        for key, val in self.maze[self.current_point].items():
            if val != 0 :
                available_moves.append(key)
        
        action_reverse = self.reverse_direction(self.last_action)
        
        print(self.current_point, available_moves)
        if action_reverse is not None and len(available_moves) > 1:
            try:
                available_moves.remove(action_reverse)
            except:
                move_index = 0
        
        move_index =random.randint(0, len(available_moves) - 1)
        
        direction = available_moves[move_index]
        
        # Remove this move from future available moves
        self.maze[self.current_point][direction] = 0

        return direction
        
    
    def reverse_direction(self, direction):
        if direction == 'E':
            return 'W'
        elif direction == 'W':
            return 'E'
        elif direction == 'N':
            return 'S'
        elif direction == 'S':
            return 'N'




class MazeSolverDFS_V1:
    def __init__(self, maze) -> None:
        self.maze = maze
        self.current_point = (1,1)
        self.to_visit = set()
        self.visited = set()
        self.path = []
        self.last_action = None
    
    def solve(self, goal):
        self.to_visit.add((1,1))
        while self.current_point != goal and bool(self.to_visit):
            self._move(self.to_visit.pop())
        
        return self.path
        
    # add points that can be visited from current point
    def _discover(self, point):
        
        available_moves = []
        for key, val in self.maze[self.current_point].items():
            if val != 0 :
                available_moves.append(key)
        
        for direction in available_moves:
            if direction == 'E':
                destination = (point[0], point[1] + 1)
                if destination not in self.visited:
                    self.to_visit.add(destination)
                    
            elif direction == 'W':
                destination = (point[0], point[1] - 1)
                if destination not in self.visited:
                    self.to_visit.add(destination)
                    
            elif direction == 'N':
                destination = (point[0] - 1, point[1])
                if destination not in self.visited:
                    self.to_visit.add(destination)
                    
            elif direction == 'S':
                destination = (point[0] + 1, point[1])
                if destination not in self.visited:
                    self.to_visit.add(destination)
                    
            else:
                print(f"Wrong direction Given {direction}")
                return
        
        
        self.visited.add(point)
        
        if len(available_moves) > 0:
            self.path.append(self.current_point)
                
    
    def _move(self, point):
        self.current_point = point
        self._discover(point)
        
        

class MazeSolverDFS_V2:
    def __init__(self, maze) -> None:
        self.map = maze
        self.visited = set()
        self.stack = []
        self.goal = None
        self.visited = set()
        self.ans = []
    
    def get_path(self, goal, start = (1,1)):
        self.goal = goal
        self.stack.append(start)
        self._solve()
        return self.ans
        
    def _solve(self):
        last_ele = len(self.stack) - 1
        current_point = self.stack[last_ele]
        self.visited.add(current_point)
        
        if current_point == self.goal:
            self.ans = self.stack.copy()
            return
        
        for key, value in self.map[current_point].items():
            if value == 1:
                next_point = self._get_next_point(current_point, key)
                self._remove_move(current_point, key)
                
                if next_point  in self.visited:
                    continue
                
                self.stack.append(next_point)
                self._solve()
        
        self.stack.pop()
        return 
        
        
    def _get_next_point(self, current_point, direction):
        if direction == 'E':
            return (current_point[0], current_point[1] + 1)
        elif direction == 'W':
            return (current_point[0], current_point[1] - 1)
        elif direction == 'N':
            return (current_point[0] - 1, current_point[1])
        elif direction == 'S':
            return (current_point[0] + 1, current_point[1])
        else:
            print(f"Wrong direction Given {direction}")
            return
        
    def _remove_move(self, point, direction):
        self.map[point][direction] = 0
        

if __name__ == "__main__":
    
    from maze_creator import maze
    
    my_maze = maze(20, 20)
    my_maze.CreateMaze(pattern='h', loopPercent=10)
    my_maze = my_maze.maze_map        

    solver = MazeSolverDFS_V2(my_maze)
    print(solver.get_path(goal=(20,20)))