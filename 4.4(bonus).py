import sys
sys.setrecursionlimit(10**5)
        
class Graph: 
  
    def __init__(self,num_of_vs): 
        self.num_of_vertices = num_of_vs 
        self.graph = {}
  
    def add_edge(self,u,v): 
        self.graph.setdefault(u,[]).append((v,0)) 
        self.graph.setdefault(v,[]).append((u,1)) 
   
    def DfsUntil(self, visited, former_edge_directions, length, num_of_root, numbers, v) :
        visited[v] = 1
        numbers[v] = (length, former_edge_directions)
        for i, _type in self.graph[v] :
            if visited[i] == 0 :
                if _type == 1 :
                    num_of_root += 1
                    num_of_root, numbers = self.DfsUntil( visited, former_edge_directions + 1, length + 1, num_of_root, numbers, i)
                elif _type ==0 :
                    num_of_root, numbers = self.DfsUntil( visited, former_edge_directions, length + 1, num_of_root, numbers, i)
        return num_of_root, numbers
    def init_variables(self):
        visited = [0] * (self.num_of_vertices) 
        num_of_root = 0
        numbers = [(0,0)] * (self.num_of_vertices) 
        return visited,num_of_root,numbers
    def Dfs(self,num_of_vs): 
        self.initializing(num_of_vs)
        visited,num_of_root,numbers = self.init_variables()
        visited[0] = 1
        for i, type_of_path in self.graph[0] :
            if type_of_path == 1 :
                num_of_root =num_of_root + 1 
                num_of_root, numbers = self.DfsUntil( visited, type_of_path, 1, num_of_root, numbers, i)
            elif type_of_path == 0:
                num_of_root, numbers = self.DfsUntil( visited, type_of_path, 1, num_of_root, numbers, i)
        return num_of_root, numbers
    
    def initializing(self,num_of_vs):
        for i in range(num_of_vs-1):
            inp_vs = input().split()
            first_v = int(inp_vs[0]) -1
            second_v = int(inp_vs[1])-1
            self.add_edge(first_v,second_v)

def calculate_ans(nums,num_of_root,i):
    paths = num_of_root - nums[i][1] + (nums[i][0] - nums[i][1])
    return paths

def print_ans(paths):
    minimum = min(paths)
    print(minimum)
    for i in range(len(paths)) :
        if paths[i] == minimum :
            print(i + 1, end = " ")

num_of_vs = int(input())
graph = Graph(num_of_vs) 
paths = []
num_of_root, numbers = graph.Dfs(num_of_vs)
paths.append(num_of_root)
for i in range(1, num_of_vs) :
    paths.append(calculate_ans(numbers,num_of_root,i))
print_ans(paths)
