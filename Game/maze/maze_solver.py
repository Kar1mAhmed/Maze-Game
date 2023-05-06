import queue
# W == left
# E == Right
# S == Down
# N == Up
class MazeSolverDFS:
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
        
        if current_point in self.goal:
            self.ans.append(self.stack.copy())
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
        
    
    
    class MazeSolverBFS:
        def __init__(self, maze) -> None:
            self.map = maze
            self.visited = set()
            self.queue = queue.Queue()
            self.goal = None
            self.visited = set()
            self.ans = []
        
        def get_path(self, goal, start = (1,1)):
            self.goal = goal
            self.queue.put(start)
            self._solve()
            return self.ans
            
        def _solve(self):
            current_point = self.stack[last_ele]
            self.visited.add(current_point)
            
            if current_point in self.goal:
                self.ans = self.stack.copy()
                return
            
            for key, value in self.map[current_point].items():
                if value == 1:
                    next_point = self._get_next_point(current_point, key)
                    self._remove_move(current_point, key)
                    
                    if next_point  in self.visited:
                        continue
                    
                    self.queue.put(next_point)
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

    solver = MazeSolverDFS(my_maze)
    print(solver.get_path(goal=(20,20)))