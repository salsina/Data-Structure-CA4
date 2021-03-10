import sys
sys.setrecursionlimit(10**5)
class Graph: 
   
    def __init__(self,num_of_vs): 
        self.num_of_vertices= num_of_vs 
        self.graph = {}
        self.visiting_time = 0
   

    def add_edge(self,u,v): 
        self.graph.setdefault(u,[]).append(v) 
        self.graph.setdefault(v,[]).append(u) 
   
    def check_if_articulation_point(self,u, visited, ar_points, parent_index, lows, discovery_time): 
  
        children =0
        visited[u]= 1
        discovery_time[u] = self.visiting_time 
        lows[u] = self.visiting_time 
        self.visiting_time += 1
  
        for v in self.graph[u]: 
            if visited[v] == 0 : 
                parent_index[v] = u 
                children += 1
                self.check_if_articulation_point(v, visited, ar_points, parent_index, lows, discovery_time) 
                lows[u] = min(lows[u], lows[v]) 
                
                if parent_index[u] == -1 and children > 1: 
                    ar_points[u] = 1
  
                if parent_index[u] != -1 and lows[v] >= discovery_time[u]: 
                    ar_points[u] = 1    
                      
            elif v != parent_index[u]:  
                lows[u] = min(lows[u], discovery_time[v]) 
  
    def initializing(self):
        visited = []
        discoverings = []
        lows = []
        parent_index =[]
        ap = []
        for i in range(self.num_of_vertices):    
            visited.append(0)
            discoverings.append(float("Inf"))
            lows.append(float("Inf"))
            parent_index.append(-1)
            ap.append(0)
        return visited,discoverings,lows,parent_index,ap   
         
    def find_articulation_points(self): 
   
        visited,discoverings,lows,parent_index,ar_points = self.initializing()
  
        for i in range(self.num_of_vertices): 
            if visited[i] == 0: 
                self.check_if_articulation_point(i, visited, ar_points, parent_index, lows, discoverings) 

        return ar_points
    def get_edges(self,num_of_edges):
        for i in range(num_of_edges):
            inp_vs = input().split()
            first_v = int(inp_vs[0]) - 1
            second_v = int(inp_vs[1]) - 1
            graph.add_edge(first_v,second_v)

    def find_ways(self,num_of_edges):
        self.get_edges(num_of_edges)
        num = 0
        ar_points = self.find_articulation_points()
        for i in ar_points:
            if i == 1:
                num +=1
        print(num)
  

inp = input()
num_of_vs = int(inp.split()[0])
num_of_edges = int(inp.split()[1])
graph = Graph(num_of_vs) 
graph.find_ways(num_of_edges) 
