import queue
import random
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
        
        # To make Dfs fully random
        items = list(self.map[current_point].items())
        random.shuffle(items)
        shuffled_items = dict(items)
        
        for key, value in shuffled_items.items():
            
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
            self.goals = None
            self.visited = set()
            self.ans = []
        
        def get_path(self, goals, start = (1,1)):
            self.goals = goals
            self.queue.put([start])
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
            
            current_path = self.queue.get()
            current_point = current_path[-1]
            
            self.visited.add(current_point)
            
            if current_point in self.goals:
                self.ans.append(current_path.copy())
                self.goals.remove(current_point)
                return
            
            for key, value in self.map[current_point].items():
                if value == 1:
                    next_point = self._get_next_point(current_point, key)
                    self._remove_move(current_point, key)
                    
                    if next_point in self.visited:
                        continue
                    
                    new_path = current_path + [next_point]
                    self.queue.put(new_path)
                    
            self._solve()
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
    Map = maze(5,5)
    Map.CreateMaze(pattern='h', loopPercent=10)
    
    Map = Map.maze_map
    solver = MazeSolverBFS(Map.copy())

    print(solver.get_path([(5,5)], (1,1)))