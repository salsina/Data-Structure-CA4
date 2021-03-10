import sys
sys.setrecursionlimit(10**5)
class Graph: 
  
    def __init__(self,num_of_vs): 
        self.num_of_vertices = num_of_vs 
        self.graph = {}
  
    def add_edge(self,u,v,charge): 
        self.graph.setdefault(u,[]).append([v,charge]) 
        self.graph.setdefault(v,[]).append([u,charge]) 

    def DFS_search(self,start_v, prev_length,max_length, visited): 
        visited[start_v] = 1
        temp_length = 0 
        next_to_v = None
        for i in range(len(self.graph[start_v])): 
            next_to_v = self.graph[start_v][i][0]  
            charge_v = self.graph[start_v][i][1]  
            if visited[next_to_v] == 0: 
                temp_length = prev_length + charge_v  
                self.DFS_search(next_to_v, temp_length,max_length, visited) 
            if (max_length[0] < temp_length):  
                max_length[0] = temp_length  
            temp_length = 0

    def longestCable(self, n): 
        max_len = [-float("Inf")]  
        visited = [0] * (n + 1)  
        self.DFS_search(0,0,max_len,visited) 
        return max_len[0]
    
    def get_edges(self,num_of_vs):
        sum_of_all_charges = 0
        for i in range(num_of_vs-1):
            inp_vs = input().split()
            first_v = int(inp_vs[0]) -1
            second_v = int(inp_vs[1])-1
            charge_v = int(inp_vs[2])
            sum_of_all_charges += charge_v
            self.add_edge(first_v,second_v,charge_v)
        return sum_of_all_charges
    
    def print_lowest_charge(self,num_of_vs):
        sum_of_all_charges =  self.get_edges(num_of_vs)
        print(2*sum_of_all_charges -  graph.longestCable(num_of_vs))

num_of_vs = int(input())
graph = Graph(num_of_vs) 
graph.print_lowest_charge(num_of_vs)
