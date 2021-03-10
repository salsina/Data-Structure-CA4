class Graph: 
  
    def __init__(self,num_of_vs,soldiers): 
        self.num_of_vertices = num_of_vs 
        self.soldiers = soldiers
        self.graph = {}
  
    def add_edge(self,u,v): 
        self.graph.setdefault(u,[]).append(v) 
        self.graph.setdefault(v,[]).append(u) 
 
    def BFS(self, s,e): 
        
        soldiers_untill = [0] * (self.num_of_vertices) 
        path_length = [0] * (self.num_of_vertices) 
        visited = [False] * (self.num_of_vertices) 
        queue = [] 
        queue.append(s) 
        visited[s] = True
        soldiers_untill[s] = self.soldiers[s]
        
        while queue: 
            s = queue.pop(0) 
            for i in self.graph[s]:
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True 
                    # prev_soldier = self.soldiers[i]
                    soldiers_untill[i] =self.soldiers[i] + soldiers_untill[s]
                    # prev_path = path_length[i]
                    path_length[i] = path_length[s] + 1
                elif path_length[i] == path_length[s] + 1:
                    if soldiers_untill[i] < self.soldiers[i] + soldiers_untill[s]:
                        soldiers_untill[i] =self.soldiers[i] + soldiers_untill[s]
        
        print(soldiers_untill[e] )


inp = input().split()
num_of_vs = int(inp[0])
num_of_edges = int(inp[1]) 
s = input()
soldiers = list(map(int,s.split()))
graph = Graph(num_of_vs,soldiers) 

for i in range(num_of_edges):
    inp_vs = input().split()
    first_v = int(inp_vs[0]) -1
    second_v = int(inp_vs[1])-1
    graph.add_edge(first_v,second_v)
se =input()
sten = list(map(int,se.split()))
start = int(sten[0]) - 1
end = int(sten[1]) - 1
graph.BFS(start,end)
  
# g.BFS(2) 
