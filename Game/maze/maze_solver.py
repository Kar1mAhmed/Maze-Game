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
        self.goals = None
        self.visited = set()
        self.ans = []
    
    def get_path(self, goals, start):
        self.goals = goals
        self.stack.append(start)
        self._solve()
        return self.ans
    
    def reset(self, maze):
        self.map = maze
        self.visited = set()
        self.stack = []
        self.goals = []
        self.visited = set()
        self.ans = []
        
    def _solve(self):
        
        #base case
        if len(self.goals) == 0:
            return
        
        last_ele = len(self.stack) - 1
        current_point = self.stack[last_ele]
        self.visited.add(current_point)
        
        if current_point in self.goals:
            self.ans.append(self.stack.copy())
            self.goals.remove(current_point)
            return
        
        for key, value in self.map[current_point].items():
            
            if len(self.goals) == 0:
                return
            
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
    Map = maze(3,3)
    Map.CreateMaze(pattern='h', loopPercent=10)
    
    Map = Map.maze_map
    print(type(Map))
    solver = MazeSolverDFS(Map.copy())

    # print(solver.get_path([(2,2)], (1,1)))
    # solver.reset(Map.copy())
    # print(solver.get_path([(3,3)], (2,2)))